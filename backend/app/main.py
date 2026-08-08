import datetime
import os
import threading
import time

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import text

from .database import get_db
from . import models, pdf as pdf_utils, excel as excel_utils
from .paths import app_dir
from .routers import prestamos, inventario, novedades, laboratorios, tareas, compras

BASE_DIR = app_dir()

app = FastAPI(title="Préstamos del taller")


@app.middleware("http")
async def sin_cache(request: Request, call_next):
    """Ninguna respuesta (páginas HTML, /api/..., /static/...) debería quedar
    cacheada por el navegador: esta es una app de un solo servidor local donde
    los datos cambian todo el tiempo (préstamos, devoluciones, inventario). Sin
    esto, el navegador puede cachear heurísticamente una página o un pedido a la
    API porque el servidor no manda ningún header de caché por default — eso
    hacía que, por ejemplo, Historial mostrara una foto vieja mientras un
    gráfico que se refresca seguido (con sus propios pedidos "nuevos" que
    igual podían pegarle a la misma caché) mostraba datos más recientes.
    "no-store" fuerza a pedir todo de nuevo siempre; en una red interna con
    pocos usuarios el costo es insignificante comparado con mostrar datos
    viejos sin que se note."""
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    return response


app.include_router(prestamos.router)
app.include_router(inventario.router)
app.include_router(novedades.router)
app.include_router(laboratorios.router)
app.include_router(tareas.router)
app.include_router(compras.router)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

CURSOS = ["1A", "1B", "2A", "2B", "3E", "3I", "4E", "4I", "5E", "5I", "6E", "6I"]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


@app.get("/healthz")
def healthz(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}


@app.post("/api/apagar")
def apagar_aplicacion():
    """Cierra el proceso del servidor (botón "Cerrar aplicación" en la barra
    superior). Da tiempo a que la respuesta le llegue al navegador antes de
    terminar el proceso, para que el .exe empaquetado libere el puerto y no
    quede corriendo en segundo plano sin que se note."""
    def _salir():
        time.sleep(0.3)
        os._exit(0)
    threading.Thread(target=_salir, daemon=True).start()
    return {"ok": True}


@app.get("/", response_class=HTMLResponse)
def mostrador(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "cursos": CURSOS,
            "dias": DIAS,
            "hoy": datetime.datetime.now().strftime("%H:%M"),
            "dia_actual": prestamos.dia_de_hoy(),
        },
    )


def _query_movimientos(
    db: Session,
    curso: str = "",
    profesor: str = "",
    elemento_codigo: str = "",
    desde: str = "",
    hasta: str = "",
    estado: str = "",
    limit: int | None = 500,
):
    q = db.query(models.Movimiento)
    if curso:
        q = q.join(models.Curso, models.Curso.id == models.Movimiento.id_curso).filter(
            models.Curso.nombre == curso
        )
    if profesor:
        q = q.filter(models.Movimiento.profesor_responsable.ilike(f"%{profesor}%"))
    if elemento_codigo:
        q = q.filter(models.Movimiento.elemento_codigo == elemento_codigo)
    if estado:
        q = q.filter(models.Movimiento.estado == estado)
    if desde:
        q = q.filter(models.Movimiento.fecha_hora >= desde)
    if hasta:
        q = q.filter(models.Movimiento.fecha_hora <= hasta + " 23:59:59")
    q = q.order_by(models.Movimiento.fecha_hora.desc())
    if limit is not None:
        q = q.limit(limit)
    return q.all()


@app.get("/historial", response_class=HTMLResponse)
def historial_page(
    request: Request,
    curso: str = "",
    profesor: str = "",
    elemento_codigo: str = "",
    desde: str = "",
    hasta: str = "",
    estado: str = "",
    db: Session = Depends(get_db),
):
    movimientos = _query_movimientos(db, curso, profesor, elemento_codigo, desde, hasta, estado)

    return templates.TemplateResponse(
        request,
        "historial.html",
        {
            "movimientos": movimientos,
            "cursos": CURSOS,
            "filtros": {
                "curso": curso, "profesor": profesor, "elemento_codigo": elemento_codigo,
                "desde": desde, "hasta": hasta, "estado": estado,
            },
        },
    )


@app.get("/historial/pdf")
def historial_pdf(
    curso: str = "",
    profesor: str = "",
    elemento_codigo: str = "",
    desde: str = "",
    hasta: str = "",
    estado: str = "",
    db: Session = Depends(get_db),
):
    movimientos = _query_movimientos(
        db, curso, profesor, elemento_codigo, desde, hasta, estado, limit=None
    )
    filtros = {
        "curso": curso, "profesor": profesor, "elemento_codigo": elemento_codigo,
        "desde": desde, "hasta": hasta, "estado": estado,
    }
    buffer = pdf_utils.generar_pdf_historial(movimientos, filtros)
    nombre = f"historial_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{nombre}"'},
    )


def _query_inventario(
    db: Session,
    q: str = "",
    categoria: str = "",
    estado: str = "",
    limit: int | None = 1000,
):
    query = db.query(models.Inventario)
    if estado:
        query = query.filter(models.Inventario.estado == estado)
    if categoria:
        query = query.filter(models.Inventario.categoria == categoria)
    if q:
        query = query.filter(
            models.Inventario.nombre.ilike(f"%{q}%")
            | models.Inventario.codigo.ilike(f"%{q}%")
            | models.Inventario.categoria.ilike(f"%{q}%")
        )
    query = query.order_by(models.Inventario.nombre)
    if limit is not None:
        query = query.limit(limit)
    return query.all()


def _categorias_existentes(db: Session) -> list[str]:
    filas = (
        db.query(models.Inventario.categoria)
        .filter(models.Inventario.categoria.isnot(None), models.Inventario.categoria != "")
        .distinct()
        .order_by(models.Inventario.categoria)
        .all()
    )
    return [f[0] for f in filas]


@app.get("/inventario", response_class=HTMLResponse)
def inventario_page(
    request: Request, q: str = "", categoria: str = "", estado: str = "", db: Session = Depends(get_db)
):
    elementos = _query_inventario(db, q, categoria, estado)
    return templates.TemplateResponse(
        request,
        "inventario.html",
        {
            "elementos": elementos,
            "q": q,
            "categoria": categoria,
            "estado": estado,
            "categorias": _categorias_existentes(db),
        },
    )


@app.get("/inventario/pdf")
def inventario_pdf(q: str = "", categoria: str = "", estado: str = "", db: Session = Depends(get_db)):
    elementos = _query_inventario(db, q, categoria, estado, limit=None)
    filtros = {"q": q, "categoria": categoria, "estado": estado}
    buffer = pdf_utils.generar_pdf_inventario(elementos, filtros)
    nombre = f"inventario_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{nombre}"'},
    )


@app.get("/novedades", response_class=HTMLResponse)
def novedades_page(request: Request, db: Session = Depends(get_db)):
    novedades_list = db.query(models.Novedad).order_by(models.Novedad.fecha_hora.desc()).limit(200).all()
    novedades_lab = (
        db.query(models.NovedadLaboratorio)
        .order_by(models.NovedadLaboratorio.fecha_hora.desc())
        .limit(200)
        .all()
    )
    return templates.TemplateResponse(
        request,
        "novedades.html",
        {
            "novedades": novedades_list,
            "novedades_lab": novedades_lab,
            "laboratorios": laboratorios.LABORATORIOS,
        },
    )


@app.get("/tareas", response_class=HTMLResponse)
def tareas_page(request: Request, db: Session = Depends(get_db)):
    tareas_list = db.query(models.Tarea).order_by(models.Tarea.fecha_hora.desc()).limit(500).all()
    return templates.TemplateResponse(
        request,
        "tareas.html",
        {"tareas": tareas_list, "laboratorios": laboratorios.LABORATORIOS},
    )


@app.get("/compras", response_class=HTMLResponse)
def compras_page(request: Request, db: Session = Depends(get_db)):
    compras_list = db.query(models.Compra).order_by(models.Compra.fecha_hora.desc()).limit(500).all()
    return templates.TemplateResponse(request, "compras.html", {"compras": compras_list})


@app.get("/compras/excel")
def compras_excel(db: Session = Depends(get_db)):
    compras_list = db.query(models.Compra).order_by(models.Compra.fecha_hora.desc()).all()
    buffer = excel_utils.generar_excel_compras(compras_list)
    nombre = f"compras_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f'attachment; filename="{nombre}"'},
    )
