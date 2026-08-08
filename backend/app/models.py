import datetime

from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, TIMESTAMP, CheckConstraint, Boolean
)
from sqlalchemy.orm import relationship

from .database import Base


class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, unique=True, nullable=False)


class Materia(Base):
    __tablename__ = "materias"
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, unique=True, nullable=False)


class Profesor(Base):
    __tablename__ = "profesores"
    id = Column(Integer, primary_key=True)
    nombre = Column(Text, unique=True, nullable=False)
    telefono = Column(Text, nullable=True)


class Horario(Base):
    __tablename__ = "horarios"
    id_horario = Column(Integer, primary_key=True)
    id_curso = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    id_materia = Column(Integer, ForeignKey("materias.id"), nullable=False)
    id_profesor = Column(Integer, ForeignKey("profesores.id"), nullable=False)
    dia = Column(Text, nullable=False)
    hora_inicio = Column(Text, nullable=False)
    hora_fin = Column(Text, nullable=False)

    curso = relationship("Curso")
    materia = relationship("Materia")
    profesor = relationship("Profesor")


class Inventario(Base):
    __tablename__ = "inventario"
    codigo = Column(Text, primary_key=True)
    nombre = Column(Text, nullable=False)
    categoria = Column(Text, nullable=True)
    estado = Column(Text, nullable=False, default="disponible")
    notas = Column(Text, nullable=True)

    __table_args__ = (
        CheckConstraint("estado IN ('disponible','prestado','reparacion','baja')"),
    )


class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True)
    # default (Python, hora local) en vez de server_default=func.now(): en SQLite
    # CURRENT_TIMESTAMP devuelve UTC, no la hora local — con la app corriendo en
    # Argentina (UTC-3) eso hacía que todo quedara registrado ~3hs adelantado.
    fecha_hora = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    tipo_actividad = Column(Text, nullable=False)

    id_curso = Column(Integer, ForeignKey("cursos.id"), nullable=True)
    dia = Column(Text, nullable=True)
    evento_nombre = Column(Text, nullable=True)

    profesor_responsable = Column(Text, nullable=False)
    cargado_por = Column(Text, nullable=True)

    elemento_codigo = Column(Text, ForeignKey("inventario.codigo"), nullable=False)
    hora_devolver = Column(Text, nullable=False)
    fecha_hora_devolucion_real = Column(TIMESTAMP, nullable=True)

    estado = Column(Text, nullable=False, default="prestado")
    anotaciones = Column(Text, nullable=True)

    curso = relationship("Curso")
    elemento = relationship("Inventario")

    __table_args__ = (
        CheckConstraint("tipo_actividad IN ('clase','evento')"),
        CheckConstraint("estado IN ('prestado','devuelto','vencido')"),
    )


class Novedad(Base):
    __tablename__ = "novedades"
    id = Column(Integer, primary_key=True)
    # default (Python, hora local) en vez de server_default=func.now(): en SQLite
    # CURRENT_TIMESTAMP devuelve UTC, no la hora local — con la app corriendo en
    # Argentina (UTC-3) eso hacía que todo quedara registrado ~3hs adelantado.
    fecha_hora = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    elemento_codigo = Column(Text, ForeignKey("inventario.codigo"), nullable=False)
    clasificacion = Column(Text, nullable=False)
    comentario = Column(Text, nullable=True)

    elemento = relationship("Inventario")


class NovedadLaboratorio(Base):
    """Novedades sobre un laboratorio/aula en sí (no sobre un elemento del
    inventario) — p. ej. "no anda el proyector fijo del Lab. E1"."""
    __tablename__ = "novedades_laboratorio"
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    laboratorio = Column(Text, nullable=False)
    comentario = Column(Text, nullable=False)


class Tarea(Base):
    """Tareas de mantenimiento u otras, asignadas a un laboratorio."""
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    laboratorio = Column(Text, nullable=False)
    responsable = Column(Text, nullable=False)
    prioridad = Column(Text, nullable=False)
    descripcion = Column(Text, nullable=False)
    realizada = Column(Boolean, nullable=False, default=False)

    __table_args__ = (
        CheckConstraint("prioridad IN ('alta','media','baja')"),
    )


class Compra(Base):
    """Lista de compras: qué hace falta, cuánto, y con qué prioridad."""
    __tablename__ = "compras"
    id = Column(Integer, primary_key=True)
    fecha_hora = Column(TIMESTAMP, nullable=False, default=datetime.datetime.now)
    cantidad = Column(Integer, nullable=False)
    descripcion = Column(Text, nullable=False)
    prioridad = Column(Text, nullable=False)

    __table_args__ = (
        CheckConstraint("prioridad IN ('alta','media','baja')"),
    )
