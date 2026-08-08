from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, or_, text
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api", tags=["inventario"])

# Grupos que se muestran como "stock destacado" en el Mostrador: se agrupan por
# palabras que aparecen en el nombre porque la mayoría de los 207 elementos
# migrados no tienen categoría cargada todavía (ver categoria == NULL). Si en el
# futuro se cargan categorías, esto se puede migrar a filtrar por categoria.
PATRONES_NOTEBOOK = ["notebook", "netbook"]

STOCK_DESTACADO = [
    {"etiqueta": "Notebooks", "patrones": PATRONES_NOTEBOOK},
    {"etiqueta": "Proyectores", "patrones": ["proyector"]},
]


@router.get("/inventario/stock-destacado")
def stock_destacado(db: Session = Depends(get_db)):
    resultados = []
    for grupo in STOCK_DESTACADO:
        filtro_nombre = or_(*[models.Inventario.nombre.ilike(f"%{p}%") for p in grupo["patrones"]])
        disponibles = (
            db.query(models.Inventario)
            .filter(filtro_nombre, models.Inventario.estado == "disponible")
            .count()
        )
        total = (
            db.query(models.Inventario)
            .filter(filtro_nombre, models.Inventario.estado != "baja")
            .count()
        )
        resultados.append({"etiqueta": grupo["etiqueta"], "disponibles": disponibles, "total": total})
    return resultados


@router.get("/inventario/movimientos-notebook-por-curso")
def movimientos_notebook_por_curso(db: Session = Depends(get_db)):
    """Cantidad de notebooks prestadas AHORA MISMO (sin devolver todavía),
    agrupada por curso — sube cuando sale una y baja cuando vuelve. Los
    préstamos de tipo "evento" (sin curso) se agrupan en "Otro"."""
    filtro_nombre = or_(*[models.Inventario.nombre.ilike(f"%{p}%") for p in PATRONES_NOTEBOOK])

    conteos = dict(
        db.query(models.Movimiento.id_curso, func.count(models.Movimiento.id))
        .join(models.Inventario, models.Inventario.codigo == models.Movimiento.elemento_codigo)
        .filter(filtro_nombre, models.Movimiento.fecha_hora_devolucion_real.is_(None))
        .group_by(models.Movimiento.id_curso)
        .all()
    )

    cursos = db.query(models.Curso).order_by(models.Curso.id).all()
    salida = [{"curso": c.nombre, "cantidad": conteos.get(c.id, 0)} for c in cursos]
    salida.append({"curso": "Otro", "cantidad": conteos.get(None, 0)})
    return salida


@router.get("/elementos/{codigo}", response_model=schemas.ElementoOut)
def obtener_elemento(codigo: str, db: Session = Depends(get_db)):
    elemento = db.query(models.Inventario).filter(models.Inventario.codigo == codigo).first()
    if not elemento:
        raise HTTPException(404, f"No existe ningún elemento con el código {codigo!r}")
    return elemento


@router.get("/inventario", response_model=list[schemas.ElementoOut])
def listar_inventario(
    estado: str | None = None,
    categoria: str | None = None,
    q: str | None = None,
    db: Session = Depends(get_db),
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
    return query.order_by(models.Inventario.nombre).limit(1000).all()


@router.post("/inventario", response_model=schemas.ElementoOut, status_code=201)
def crear_elemento(body: schemas.ElementoCreate, db: Session = Depends(get_db)):
    codigo = body.codigo.strip()
    nombre = body.nombre.strip()
    if not codigo or not nombre:
        raise HTTPException(422, "Faltan el código o el nombre")
    if db.query(models.Inventario).filter(models.Inventario.codigo == codigo).first():
        raise HTTPException(409, f"Ya existe un elemento con el código {codigo!r}")

    elemento = models.Inventario(
        codigo=codigo,
        nombre=nombre,
        categoria=(body.categoria or "").strip() or None,
    )
    db.add(elemento)
    db.commit()
    db.refresh(elemento)
    return elemento


@router.patch("/inventario/{codigo}", response_model=schemas.ElementoOut)
def actualizar_elemento(codigo: str, body: schemas.ElementoUpdate, db: Session = Depends(get_db)):
    elemento = db.query(models.Inventario).filter(models.Inventario.codigo == codigo).first()
    if not elemento:
        raise HTTPException(404, f"No existe ningún elemento con el código {codigo!r}")

    nuevo_codigo = (body.nuevo_codigo or "").strip()
    if nuevo_codigo and nuevo_codigo != codigo:
        if db.query(models.Inventario).filter(models.Inventario.codigo == nuevo_codigo).first():
            raise HTTPException(409, f"Ya existe un elemento con el código {nuevo_codigo!r}")
        # Se actualizan primero las tablas que referencian el código (hijas) y
        # recién después el inventario (padre), para no violar la FK en Postgres.
        db.execute(
            text("UPDATE movimientos SET elemento_codigo = :nuevo WHERE elemento_codigo = :actual"),
            {"nuevo": nuevo_codigo, "actual": codigo},
        )
        db.execute(
            text("UPDATE novedades SET elemento_codigo = :nuevo WHERE elemento_codigo = :actual"),
            {"nuevo": nuevo_codigo, "actual": codigo},
        )
        db.execute(
            text("UPDATE inventario SET codigo = :nuevo WHERE codigo = :actual"),
            {"nuevo": nuevo_codigo, "actual": codigo},
        )
        db.commit()
        codigo = nuevo_codigo
        elemento = db.query(models.Inventario).filter(models.Inventario.codigo == codigo).first()

    if body.nombre is not None:
        nombre = body.nombre.strip()
        if not nombre:
            raise HTTPException(422, "El nombre no puede quedar vacío")
        elemento.nombre = nombre
    if body.categoria is not None:
        elemento.categoria = body.categoria.strip() or None
    if body.notas is not None:
        elemento.notas = body.notas.strip() or None

    db.commit()
    db.refresh(elemento)
    return elemento


@router.delete("/inventario/{codigo}")
def eliminar_elemento(codigo: str, db: Session = Depends(get_db)):
    elemento = db.query(models.Inventario).filter(models.Inventario.codigo == codigo).first()
    if not elemento:
        raise HTTPException(404, f"No existe ningún elemento con el código {codigo!r}")

    tiene_historial = (
        db.query(models.Movimiento).filter(models.Movimiento.elemento_codigo == codigo).first()
        or db.query(models.Novedad).filter(models.Novedad.elemento_codigo == codigo).first()
    )
    if tiene_historial:
        raise HTTPException(
            409,
            "Este elemento ya tiene préstamos o novedades registradas: eliminarlo borraría ese "
            "historial. Marcalo como 'baja' desde Novedades en vez de eliminarlo.",
        )

    db.delete(elemento)
    db.commit()
    return {"ok": True}
