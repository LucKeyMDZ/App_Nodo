from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api", tags=["laboratorios"])

# Lista fija: son 5 laboratorios físicos del taller, no una tabla de la base
# (mismo criterio que CURSOS en main.py, que tampoco sale de una tabla propia).
LABORATORIOS = ["Lab. E1", "Lab. E2", "Lab. Info. 1", "Lab. Info. 2", "Lab. Cn"]


@router.post("/novedades-laboratorio")
def crear_novedad_laboratorio(body: schemas.NovedadLaboratorioCreate, db: Session = Depends(get_db)):
    if body.laboratorio not in LABORATORIOS:
        raise HTTPException(422, f"Laboratorio inválido: {body.laboratorio!r}")
    comentario = body.comentario.strip()
    if not comentario:
        raise HTTPException(422, "Falta describir el problema detectado")

    novedad = models.NovedadLaboratorio(laboratorio=body.laboratorio, comentario=comentario)
    db.add(novedad)
    db.commit()
    db.refresh(novedad)
    return {
        "id": novedad.id,
        "fecha_hora": novedad.fecha_hora,
        "laboratorio": novedad.laboratorio,
        "comentario": novedad.comentario,
    }


@router.get("/novedades-laboratorio")
def listar_novedades_laboratorio(db: Session = Depends(get_db)):
    filas = (
        db.query(models.NovedadLaboratorio)
        .order_by(models.NovedadLaboratorio.fecha_hora.desc())
        .limit(200)
        .all()
    )
    return [
        {"id": n.id, "fecha_hora": n.fecha_hora, "laboratorio": n.laboratorio, "comentario": n.comentario}
        for n in filas
    ]


@router.delete("/novedades-laboratorio/{novedad_id}")
def eliminar_novedad_laboratorio(novedad_id: int, db: Session = Depends(get_db)):
    novedad = db.query(models.NovedadLaboratorio).filter(models.NovedadLaboratorio.id == novedad_id).first()
    if not novedad:
        raise HTTPException(404, "No existe esa novedad")
    db.delete(novedad)
    db.commit()
    return {"ok": True}
