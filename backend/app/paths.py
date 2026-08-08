"""Resolución de rutas que funciona tanto corriendo desde el código fuente
(python/uvicorn normal) como empaquetado con PyInstaller en un .exe."""
import sys
from pathlib import Path


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def _bundle_root() -> Path:
    # PyInstaller define sys._MEIPASS tanto en modo --onefile (carpeta temporal
    # que se extrae en cada arranque) como en --onedir (la carpeta del propio .exe).
    return Path(getattr(sys, "_MEIPASS", Path(sys.executable).parent))


def app_dir() -> Path:
    """Carpeta con templates/ y static/: solo lectura, se puede empaquetar."""
    if is_frozen():
        return _bundle_root() / "app"
    return Path(__file__).resolve().parent


def db_sql_dir() -> Path:
    """Carpeta con schema_sqlite.sql y seed.sql (para el alta inicial de la base)."""
    if is_frozen():
        return _bundle_root() / "db"
    return Path(__file__).resolve().parent.parent.parent / "db"


def data_dir() -> Path:
    """Carpeta donde vive local.db: tiene que ser escribible y persistir entre
    ejecuciones, así que nunca es la carpeta temporal de --onefile."""
    if is_frozen():
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent
