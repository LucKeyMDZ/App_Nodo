import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, backup_excel
from ..database import get_db

router = APIRouter(prefix="/api", tags=["prestamos"])

DIAS_ES = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


def dia_de_hoy() -> str:
    idx = datetime.datetime.now().weekday()  # 0=Lunes
    return DIAS_ES[idx] if idx < 5 else DIAS_ES[0]


@router.get("/horario/profesor", response_model=schemas.ProfesorLookupOut)
def buscar_profesor(curso: str, dia: str | None = None, hora: str | None = None,
                     db: Session = Depends(get_db)):
    """Dado un curso (+ día/hora opcionales, por defecto ahora), busca quién da clase."""
    dia = dia or dia_de_hoy()
    hora = hora or datetime.datetime.now().strftime("%H:%M")

    row = (
        db.query(models.Horario, models.Materia, models.Profesor)
        .join(models.Curso, models.Curso.id == models.Horario.id_curso)
        .join(models.Materia, models.Materia.id == models.Horario.id_materia)
        .join(models.Profesor, models.Profesor.id == models.Horario.id_profesor)
        .filter(
            models.Curso.nombre == curso,
            models.Horario.dia == dia,
            models.Horario.hora_inicio <= hora,
            models.Horario.hora_fin > hora,
        )
        .first()
    )
    if not row:
        return schemas.ProfesorLookupOut(encontrado=False)
    horario, materia, profesor = row
    return schemas.ProfesorLookupOut(
        encontrado=True,
        materia=materia.nombre,
        profesor=profesor.nombre,
        hora_inicio=horario.hora_inicio,
        hora_fin=horario.hora_fin,
    )


def _prestamo_to_out(m: models.Movimiento) -> schemas.PrestamoOut:
    return schemas.PrestamoOut(
        id=m.id,
        fecha_hora=m.fecha_hora,
        tipo_actividad=m.tipo_actividad,
        curso=m.curso.nombre if m.curso else None,
        evento_nombre=m.evento_nombre,
        profesor_responsable=m.profesor_responsable,
        cargado_por=m.cargado_por,
        elemento_codigo=m.elemento_codigo,
        elemento_nombre=m.elemento.nombre if m.elemento else None,
        hora_devolver=m.hora_devolver,
        fecha_hora_devolucion_real=m.fecha_hora_devolucion_real,
        estado=m.estado,
        anotaciones=m.anotaciones,
    )


def _resolver_responsable(
    db: Session,
    tipo_actividad: str,
    curso: str | None,
    dia: str | None,
    hora: str | None,
    evento_nombre: str | None,
    responsable_manual: str | None,
) -> tuple[int | None, str | None, str]:
    """Valida los datos de curso/evento (comunes a todo un lote) y devuelve
    (id_curso, dia, profesor_responsable)."""
    if tipo_actividad == "clase":
        if not curso:
            raise HTTPException(422, "Falta el curso")
        curso_row = db.query(models.Curso).filter(models.Curso.nombre == curso).first()
        if not curso_row:
            raise HTTPException(404, f"No existe el curso {curso!r}")
        dia = dia or dia_de_hoy()
        hora = hora or datetime.datetime.now().strftime("%H:%M")

        lookup = buscar_profesor(curso=curso, dia=dia, hora=hora, db=db)
        if not lookup.encontrado:
            raise HTTPException(
                404,
                f"No se encontró clase para {curso} el {dia} a las {hora}. "
                "Si es correcto, cargalo como 'evento' en vez de 'clase'.",
            )
        return curso_row.id, dia, lookup.profesor
    else:  # evento
        if not evento_nombre or not responsable_manual:
            raise HTTPException(422, "Para un evento hace falta el nombre del evento y el responsable")
        return None, None, responsable_manual


def _crear_prestamo_uno(
    db: Session,
    elemento_codigo: str,
    tipo_actividad: str,
    id_curso: int | None,
    dia: str | None,
    evento_nombre: str | None,
    profesor_responsable: str,
    cargado_por: str | None,
    hora_devolver: str,
    anotaciones: str | None,
) -> models.Movimiento:
    elemento = db.query(models.Inventario).filter(
        models.Inventario.codigo == elemento_codigo
    ).first()
    if not elemento:
        raise HTTPException(404, f"No existe ningún elemento con el código {elemento_codigo!r}")
    if elemento.estado == "baja":
        raise HTTPException(409, "Este elemento está dado de baja, no se puede prestar")

    # Chequeo contra el movimiento real, no solo contra el campo estado del
    # elemento: estado es un valor "cacheado" que alguna otra lógica (p. ej.
    # una novedad borrada) podría haber dejado desincronizado. Esta es la
    # verificación que de verdad importa — nunca debe poder haber dos
    # préstamos abiertos del mismo elemento al mismo tiempo.
    prestamo_abierto = (
        db.query(models.Movimiento)
        .filter(
            models.Movimiento.elemento_codigo == elemento_codigo,
            models.Movimiento.fecha_hora_devolucion_real.is_(None),
        )
        .first()
    )
    if prestamo_abierto:
        raise HTTPException(409, "Este elemento ya figura como prestado")

    mov = models.Movimiento(
        tipo_actividad=tipo_actividad,
        id_curso=id_curso,
        dia=dia,
        evento_nombre=evento_nombre if tipo_actividad == "evento" else None,
        profesor_responsable=profesor_responsable,
        cargado_por=cargado_por,
        elemento_codigo=elemento_codigo,
        hora_devolver=hora_devolver,
        estado="prestado",
        anotaciones=anotaciones,
    )
    db.add(mov)
    elemento.estado = "prestado"
    db.commit()
    db.refresh(mov)

    backup_excel.registrar(
        tipo="SALIDA",
        elemento_codigo=mov.elemento_codigo,
        elemento_nombre=elemento.nombre,
        curso_evento=mov.curso.nombre if mov.curso else mov.evento_nombre,
        responsable=mov.profesor_responsable,
        hora_devolver=mov.hora_devolver,
        cargado_por=mov.cargado_por,
        momento=mov.fecha_hora,
    )
    return mov


@router.post("/prestamos", response_model=schemas.PrestamoOut)
def crear_prestamo(body: schemas.PrestamoCreate, db: Session = Depends(get_db)):
    id_curso, dia, profesor_responsable = _resolver_responsable(
        db, body.tipo_actividad, body.curso, body.dia, body.hora,
        body.evento_nombre, body.responsable_manual,
    )
    mov = _crear_prestamo_uno(
        db, body.elemento_codigo, body.tipo_actividad, id_curso, dia,
        body.evento_nombre, profesor_responsable, body.cargado_por,
        body.hora_devolver, body.anotaciones,
    )
    return _prestamo_to_out(mov)


@router.post("/prestamos/batch", response_model=schemas.PrestamoBatchOut)
def crear_prestamos_batch(body: schemas.PrestamoBatchCreate, db: Session = Depends(get_db)):
    if not body.elementos_codigos:
        raise HTTPException(422, "No hay elementos para prestar")

    # Datos comunes a todo el lote (curso/profesor o evento): se validan una sola vez.
    id_curso, dia, profesor_responsable = _resolver_responsable(
        db, body.tipo_actividad, body.curso, body.dia, body.hora,
        body.evento_nombre, body.responsable_manual,
    )

    resultados = []
    for codigo in body.elementos_codigos:
        try:
            mov = _crear_prestamo_uno(
                db, codigo, body.tipo_actividad, id_curso, dia,
                body.evento_nombre, profesor_responsable, body.cargado_por,
                body.hora_devolver, body.anotaciones,
            )
            resultados.append(schemas.PrestamoBatchItemResult(
                elemento_codigo=codigo, ok=True, prestamo=_prestamo_to_out(mov),
            ))
        except HTTPException as e:
            db.rollback()
            resultados.append(schemas.PrestamoBatchItemResult(
                elemento_codigo=codigo, ok=False, error=str(e.detail),
            ))

    return schemas.PrestamoBatchOut(resultados=resultados)


@router.get("/prestamos/abierto/{codigo}", response_model=schemas.PrestamoOut | None)
def prestamo_abierto(codigo: str, db: Session = Depends(get_db)):
    """Busca si hay un préstamo sin devolver para ese código (para el flujo de devolución)."""
    mov = (
        db.query(models.Movimiento)
        .filter(models.Movimiento.elemento_codigo == codigo, models.Movimiento.estado != "devuelto")
        .order_by(models.Movimiento.fecha_hora.desc())
        .first()
    )
    if not mov:
        return None
    return _prestamo_to_out(mov)


def _devolver_uno(db: Session, prestamo_id: int) -> models.Movimiento:
    mov = db.query(models.Movimiento).filter(models.Movimiento.id == prestamo_id).first()
    if not mov:
        raise HTTPException(404, "No existe ese préstamo")
    if mov.estado == "devuelto":
        raise HTTPException(409, "Ese préstamo ya estaba devuelto")

    ahora = datetime.datetime.now()
    mov.fecha_hora_devolucion_real = ahora
    hora_actual = ahora.strftime("%H:%M")
    mov.estado = "vencido" if hora_actual > mov.hora_devolver else "devuelto"

    elemento = db.query(models.Inventario).filter(
        models.Inventario.codigo == mov.elemento_codigo
    ).first()
    if elemento and elemento.estado == "prestado":
        elemento.estado = "disponible"

    db.commit()
    db.refresh(mov)

    backup_excel.registrar(
        tipo="ENTRADA",
        elemento_codigo=mov.elemento_codigo,
        elemento_nombre=elemento.nombre if elemento else None,
        curso_evento=mov.curso.nombre if mov.curso else mov.evento_nombre,
        responsable=mov.profesor_responsable,
        momento=mov.fecha_hora_devolucion_real,
    )
    return mov


@router.post("/prestamos/{prestamo_id}/devolver", response_model=schemas.PrestamoOut)
def devolver(prestamo_id: int, db: Session = Depends(get_db)):
    mov = _devolver_uno(db, prestamo_id)
    return _prestamo_to_out(mov)


@router.post("/prestamos/devolver/batch", response_model=schemas.DevolucionBatchOut)
def devolver_batch(body: schemas.DevolucionBatchCreate, db: Session = Depends(get_db)):
    if not body.prestamo_ids:
        raise HTTPException(422, "No hay préstamos para devolver")

    resultados = []
    for prestamo_id in body.prestamo_ids:
        try:
            mov = _devolver_uno(db, prestamo_id)
            resultados.append(schemas.DevolucionBatchItemResult(
                prestamo_id=prestamo_id, ok=True, prestamo=_prestamo_to_out(mov),
            ))
        except HTTPException as e:
            db.rollback()
            resultados.append(schemas.DevolucionBatchItemResult(
                prestamo_id=prestamo_id, ok=False, error=str(e.detail),
            ))

    return schemas.DevolucionBatchOut(resultados=resultados)


@router.get("/historial", response_model=list[schemas.PrestamoOut])
def historial(
    curso: str | None = None,
    profesor: str | None = None,
    elemento_codigo: str | None = None,
    desde: str | None = None,   # YYYY-MM-DD
    hasta: str | None = None,   # YYYY-MM-DD
    estado: str | None = None,
    db: Session = Depends(get_db),
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

    q = q.order_by(models.Movimiento.fecha_hora.desc()).limit(500)
    return [_prestamo_to_out(m) for m in q.all()]
