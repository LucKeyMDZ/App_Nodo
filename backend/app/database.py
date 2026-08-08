import os
import sqlite3
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base

from .paths import data_dir, db_sql_dir

# Por defecto usa SQLite (local.db, junto al .exe o en backend/ si se corre desde
# código fuente) para poder probar sin Docker ni Postgres. En el servidor,
# docker-compose.yml define DATABASE_URL apuntando a Postgres y pisa este valor.
_DEFAULT_SQLITE_PATH = data_dir() / "local.db"
_USANDO_DEFAULT = "DATABASE_URL" not in os.environ
DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{_DEFAULT_SQLITE_PATH.as_posix()}")


def _crear_y_sembrar_si_no_existe():
    """Para el .exe empaquetado (o la primera vez que se corre desde código
    fuente sin haber corrido init_local_db.py): si no existe el archivo de la
    base, la crea a partir de schema_sqlite.sql + seed.sql empaquetados. Nunca
    toca una base que ya existe."""
    if _DEFAULT_SQLITE_PATH.exists():
        return
    schema_path = db_sql_dir() / "schema_sqlite.sql"
    seed_path = db_sql_dir() / "seed.sql"
    conn = sqlite3.connect(_DEFAULT_SQLITE_PATH)
    try:
        conn.executescript(schema_path.read_text(encoding="utf-8"))
        conn.executescript(seed_path.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()


if _USANDO_DEFAULT:
    _crear_y_sembrar_si_no_existe()

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def _ensure_schema_migrations():
    """Altas de columnas agregadas después del schema.sql original, para no romper
    bases (SQLite o Postgres) ya creadas antes de que existieran. Es un no-op en
    instalaciones nuevas, donde schema.sql/schema_sqlite.sql ya traen la columna."""
    insp = inspect(engine)
    if "inventario" not in insp.get_table_names():
        return  # todavía no se corrió schema.sql; nada que migrar
    columnas = {c["name"] for c in insp.get_columns("inventario")}
    if "notas" not in columnas:
        with engine.begin() as conn:
            conn.execute(text("ALTER TABLE inventario ADD COLUMN notas TEXT"))
    tablas_existentes = insp.get_table_names()
    tablas_nuevas = {
        "novedades_laboratorio": "NovedadLaboratorio",
        "tareas": "Tarea",
        "compras": "Compra",
    }
    faltantes = [nombre_clase for tabla, nombre_clase in tablas_nuevas.items() if tabla not in tablas_existentes]
    if faltantes:
        from . import models  # import diferido: evita el ciclo con database.Base
        for nombre_clase in faltantes:
            getattr(models, nombre_clase).__table__.create(bind=engine, checkfirst=True)


_ensure_schema_migrations()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
