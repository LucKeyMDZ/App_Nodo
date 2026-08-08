from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/api", tags=["compras"])


def _compra_a_dict(c: models.Compra) -> dict:
    return {
        "id": c.id,
        "fecha_hora": c.fecha_hora,
        "cantidad": c.cantidad,
        "descripcion": c.descripcion,
        "prioridad": c.prioridad,
    }


@router.post("/compras")
def crear_compra(body: schemas.CompraCreate, db: Session = Depends(get_db)):
    descripcion = body.descripcion.strip()
    if not descripcion:
        raise HTTPException(422, "Falta indicar qué hay que comprar")
    if body.cantidad < 1:
        raise HTTPException(422, "La cantidad tiene que ser al menos 1")

    compra = models.Compra(cantidad=body.cantidad, descripcion=descripcion, prioridad=body.prioridad)
    db.add(compra)
    db.commit()
    db.refresh(compra)
    return _compra_a_dict(compra)


@router.get("/compras")
def listar_compras(db: Session = Depends(get_db)):
    compras = db.query(models.Compra).order_by(models.Compra.fecha_hora.desc()).limit(500).all()
    return [_compra_a_dict(c) for c in compras]


@router.delete("/compras/{compra_id}")
def eliminar_compra(compra_id: int, db: Session = Depends(get_db)):
    compra = db.query(models.Compra).filter(models.Compra.id == compra_id).first()
    if not compra:
        raise HTTPException(404, "No existe ese ítem")
    db.delete(compra)
    db.commit()
    return {"ok": True}
