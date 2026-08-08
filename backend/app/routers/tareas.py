from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from .laboratorios import LABORATORIOS

router = APIRouter(prefix="/api", tags=["tareas"])


def _tarea_a_dict(t: models.Tarea) -> dict:
    return {
        "id": t.id,
        "fecha_hora": t.fecha_hora,
        "laboratorio": t.laboratorio,
        "responsable": t.responsable,
        "prioridad": t.prioridad,
        "descripcion": t.descripcion,
        "realizada": t.realizada,
    }


@router.post("/tareas")
def crear_tarea(body: schemas.TareaCreate, db: Session = Depends(get_db)):
    if body.laboratorio not in LABORATORIOS:
        raise HTTPException(422, f"Laboratorio inválido: {body.laboratorio!r}")
    responsable = body.responsable.strip()
    descripcion = body.descripcion.strip()
    if not responsable:
        raise HTTPException(422, "Falta indicar quién tiene que hacer la tarea")
    if not descripcion:
        raise HTTPException(422, "Falta describir la tarea")

    tarea = models.Tarea(
        laboratorio=body.laboratorio,
        responsable=responsable,
        prioridad=body.prioridad,
        descripcion=descripcion,
    )
    db.add(tarea)
    db.commit()
    db.refresh(tarea)
    return _tarea_a_dict(tarea)


@router.get("/tareas")
def listar_tareas(db: Session = Depends(get_db)):
    tareas = db.query(models.Tarea).order_by(models.Tarea.fecha_hora.desc()).limit(500).all()
    return [_tarea_a_dict(t) for t in tareas]


@router.patch("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: int, body: schemas.TareaUpdate, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(404, "No existe esa tarea")
    if body.realizada is not None:
        tarea.realizada = body.realizada
    db.commit()
    db.refresh(tarea)
    return _tarea_a_dict(tarea)


@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not tarea:
        raise HTTPException(404, "No existe esa tarea")
    db.delete(tarea)
    db.commit()
    return {"ok": True}
