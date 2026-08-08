import datetime
from typing import Optional, Literal
from pydantic import BaseModel


class ElementoOut(BaseModel):
    codigo: str
    nombre: str
    categoria: Optional[str] = None
    estado: str
    notas: Optional[str] = None

    class Config:
        from_attributes = True


class ElementoCreate(BaseModel):
    codigo: str
    nombre: str
    categoria: Optional[str] = None


class ElementoUpdate(BaseModel):
    nuevo_codigo: Optional[str] = None
    nombre: Optional[str] = None
    categoria: Optional[str] = None
    notas: Optional[str] = None


class ProfesorLookupOut(BaseModel):
    encontrado: bool
    materia: Optional[str] = None
    profesor: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None


class PrestamoCreate(BaseModel):
    elemento_codigo: str
    tipo_actividad: Literal["clase", "evento"]

    # si es clase:
    curso: Optional[str] = None
    dia: Optional[str] = None
    hora: Optional[str] = None  # HH:MM, usada para buscar el profesor automáticamente

    # si es evento:
    evento_nombre: Optional[str] = None
    responsable_manual: Optional[str] = None

    cargado_por: Optional[str] = None
    hora_devolver: str
    anotaciones: Optional[str] = None


class PrestamoOut(BaseModel):
    id: int
    fecha_hora: datetime.datetime
    tipo_actividad: str
    curso: Optional[str] = None
    evento_nombre: Optional[str] = None
    profesor_responsable: str
    cargado_por: Optional[str] = None
    elemento_codigo: str
    elemento_nombre: Optional[str] = None
    hora_devolver: str
    fecha_hora_devolucion_real: Optional[datetime.datetime] = None
    estado: str
    anotaciones: Optional[str] = None

    class Config:
        from_attributes = True


class PrestamoBatchCreate(BaseModel):
    elementos_codigos: list[str]
    tipo_actividad: Literal["clase", "evento"]

    # si es clase:
    curso: Optional[str] = None
    dia: Optional[str] = None
    hora: Optional[str] = None  # HH:MM, usada para buscar el profesor automáticamente

    # si es evento:
    evento_nombre: Optional[str] = None
    responsable_manual: Optional[str] = None

    cargado_por: Optional[str] = None
    hora_devolver: str
    anotaciones: Optional[str] = None


class PrestamoBatchItemResult(BaseModel):
    elemento_codigo: str
    ok: bool
    prestamo: Optional[PrestamoOut] = None
    error: Optional[str] = None


class PrestamoBatchOut(BaseModel):
    resultados: list[PrestamoBatchItemResult]


class DevolucionBatchCreate(BaseModel):
    prestamo_ids: list[int]


class DevolucionBatchItemResult(BaseModel):
    prestamo_id: int
    ok: bool
    prestamo: Optional[PrestamoOut] = None
    error: Optional[str] = None


class DevolucionBatchOut(BaseModel):
    resultados: list[DevolucionBatchItemResult]


class NovedadCreate(BaseModel):
    elemento_codigo: str
    clasificacion: str
    comentario: Optional[str] = None


class NovedadLaboratorioCreate(BaseModel):
    laboratorio: str
    comentario: str


class TareaCreate(BaseModel):
    laboratorio: str
    responsable: str
    prioridad: Literal["alta", "media", "baja"]
    descripcion: str


class TareaUpdate(BaseModel):
    realizada: Optional[bool] = None


class CompraCreate(BaseModel):
    cantidad: int
    descripcion: str
    prioridad: Literal["alta", "media", "baja"]
