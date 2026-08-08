from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from .. import schemas

router = APIRouter(prefix="/api", tags=["novedades"])

CLASIFICACIONES_QUE_DAN_DE_BAJA = {"retiro", "baja"}


@router.post("/novedades")
def crear_novedad(body: schemas.NovedadCreate, db: Session = Depends(get_db)):
    elemento = db.query(models.Inventario).filter(
        models.Inventario.codigo == body.elemento_codigo
    ).first()
    if not elemento:
        raise HTTPException(404, f"No existe ningún elemento con el código {body.elemento_codigo!r}")

    novedad = models.Novedad(
        elemento_codigo=body.elemento_codigo,
        clasificacion=body.clasificacion,
        comentario=body.comentario,
    )
    db.add(novedad)

    if body.clasificacion.lower() in CLASIFICACIONES_QUE_DAN_DE_BAJA:
        elemento.estado = "baja"
    elif body.clasificacion.lower() in ("reparacion", "reparación"):
        elemento.estado = "reparacion"

    db.commit()
    db.refresh(novedad)
    return {
        "id": novedad.id,
        "elemento_codigo": novedad.elemento_codigo,
        "clasificacion": novedad.clasificacion,
        "comentario": novedad.comentario,
        "estado_elemento": elemento.estado,
    }


@router.get("/novedades")
def listar_novedades(db: Session = Depends(get_db)):
    novedades = db.query(models.Novedad).order_by(models.Novedad.fecha_hora.desc()).limit(500).all()
    return [
        {
            "id": n.id,
            "fecha_hora": n.fecha_hora,
            "elemento_codigo": n.elemento_codigo,
            "elemento_nombre": n.elemento.nombre if n.elemento else None,
            "clasificacion": n.clasificacion,
            "comentario": n.comentario,
        }
        for n in novedades
    ]


def _estado_segun_clasificacion(clasificacion: str) -> str | None:
    clasif = clasificacion.lower()
    if clasif in CLASIFICACIONES_QUE_DAN_DE_BAJA:
        return "baja"
    if clasif in ("reparacion", "reparación"):
        return "reparacion"
    return None


@router.delete("/novedades/{novedad_id}")
def eliminar_novedad(novedad_id: int, db: Session = Depends(get_db)):
    novedad = db.query(models.Novedad).filter(models.Novedad.id == novedad_id).first()
    if not novedad:
        raise HTTPException(404, "No existe esa novedad")

    elemento = db.query(models.Inventario).filter(
        models.Inventario.codigo == novedad.elemento_codigo
    ).first()
    estado_de_esta_novedad = _estado_segun_clasificacion(novedad.clasificacion)

    db.delete(novedad)

    # Si esta novedad era la que había puesto al elemento en ese estado, al
    # borrarla se revierte: al estado que indique la novedad vigente más
    # reciente que quede, o a "disponible" si no queda ninguna.
    if elemento and estado_de_esta_novedad and elemento.estado == estado_de_esta_novedad:
        restantes = (
            db.query(models.Novedad)
            .filter(models.Novedad.elemento_codigo == elemento.codigo, models.Novedad.id != novedad_id)
            .order_by(models.Novedad.fecha_hora.desc())
            .all()
        )
        nuevo_estado = "disponible"
        for n in restantes:
            estado_n = _estado_segun_clasificacion(n.clasificacion)
            if estado_n:
                nuevo_estado = estado_n
                break

        # El préstamo real manda por sobre lo que diga la novedad: si el
        # elemento tiene un movimiento sin devolver, no puede "volver a estar
        # disponible" solo porque se borró una novedad — en la realidad sigue
        # afuera. Sin este chequeo, un elemento prestado que además tenía una
        # novedad de baja/reparación podía quedar marcado "disponible" al
        # borrar esa novedad, mientras el préstamo seguía abierto.
        tiene_prestamo_abierto = (
            db.query(models.Movimiento)
            .filter(
                models.Movimiento.elemento_codigo == elemento.codigo,
                models.Movimiento.fecha_hora_devolucion_real.is_(None),
            )
            .first()
            is not None
        )
        if tiene_prestamo_abierto:
            nuevo_estado = "prestado"

        elemento.estado = nuevo_estado

    db.commit()
    return {"ok": True}
