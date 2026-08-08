"""
Crea backend/local.db (SQLite) a partir de db/schema_sqlite.sql y db/seed.sql.
Se puede correr las veces que haga falta: si local.db ya existe, la borra y la
vuelve a crear de cero con los datos originales.

Uso (desde la carpeta raíz del proyecto):
    python init_local_db.py
"""
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "backend" / "local.db"
SCHEMA_PATH = BASE_DIR / "db" / "schema_sqlite.sql"
SEED_PATH = BASE_DIR / "db" / "seed.sql"

if DB_PATH.exists():
    DB_PATH.unlink()
    print(f"Base anterior eliminada: {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON")
conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
conn.executescript(SEED_PATH.read_text(encoding="utf-8"))
conn.commit()

cur = conn.cursor()
for tabla in ["cursos", "materias", "profesores", "horarios", "inventario", "novedades"]:
    cur.execute(f"SELECT COUNT(*) FROM {tabla}")
    print(f"  {tabla}: {cur.fetchone()[0]} filas")
conn.close()

print(f"\nListo. Base creada en: {DB_PATH}")
