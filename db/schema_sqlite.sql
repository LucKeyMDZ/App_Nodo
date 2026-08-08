-- ============================================================
-- Esquema completo — Sistema de préstamos del taller
-- ============================================================

-- ---------- Horario académico ----------

CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS profesores (
    id INTEGER PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL,
    telefono TEXT
);

CREATE TABLE IF NOT EXISTS horarios (
    id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_curso INTEGER NOT NULL REFERENCES cursos(id),
    id_materia INTEGER NOT NULL REFERENCES materias(id),
    id_profesor INTEGER NOT NULL REFERENCES profesores(id),
    dia TEXT NOT NULL CHECK (dia IN ('Lunes','Martes','Miércoles','Jueves','Viernes')),
    hora_inicio TEXT NOT NULL,   -- 'HH:MM', 24hs
    hora_fin TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_horarios_lookup ON horarios (id_curso, dia, hora_inicio, hora_fin);

-- ---------- Inventario ----------

CREATE TABLE IF NOT EXISTS inventario (
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    categoria TEXT,
    estado TEXT NOT NULL DEFAULT 'disponible'
        CHECK (estado IN ('disponible', 'prestado', 'reparacion', 'baja')),
    notas TEXT
);

-- ---------- Movimientos (préstamos / devoluciones) ----------

CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_actividad TEXT NOT NULL CHECK (tipo_actividad IN ('clase', 'evento')),

    -- si es clase:
    id_curso INTEGER REFERENCES cursos(id),
    dia TEXT,
    -- si es evento especial:
    evento_nombre TEXT,

    -- nombre del responsable en el momento del préstamo (texto fijo, no referencia,
    -- para que el historial no cambie si el profesor se renombra o se reasigna después)
    profesor_responsable TEXT NOT NULL,
    cargado_por TEXT,

    elemento_codigo TEXT NOT NULL REFERENCES inventario(codigo),
    hora_devolver TEXT NOT NULL,          -- 'HH:MM' esperada
    fecha_hora_devolucion_real TEXT, -- NULL mientras sigue afuera

    estado TEXT NOT NULL DEFAULT 'prestado'
        CHECK (estado IN ('prestado', 'devuelto', 'vencido')),
    anotaciones TEXT
);

CREATE INDEX IF NOT EXISTS idx_movimientos_elemento ON movimientos (elemento_codigo);
CREATE INDEX IF NOT EXISTS idx_movimientos_estado ON movimientos (estado);
CREATE INDEX IF NOT EXISTS idx_movimientos_fecha ON movimientos (fecha_hora);

-- ---------- Novedades (bajas / incidentes) ----------

CREATE TABLE IF NOT EXISTS novedades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    elemento_codigo TEXT NOT NULL REFERENCES inventario(codigo),
    clasificacion TEXT NOT NULL,   -- 'retiro', 'reparacion', 'daño', etc. (texto libre, sin restricción dura)
    comentario TEXT
);

CREATE INDEX IF NOT EXISTS idx_novedades_elemento ON novedades (elemento_codigo);

-- ---------- Novedades de laboratorios (no son de un elemento puntual) ----------

CREATE TABLE IF NOT EXISTS novedades_laboratorio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    laboratorio TEXT NOT NULL,
    comentario TEXT NOT NULL
);

-- ---------- Tareas (mantenimiento u otras, por laboratorio) ----------

CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    laboratorio TEXT NOT NULL,
    responsable TEXT NOT NULL,
    prioridad TEXT NOT NULL CHECK (prioridad IN ('alta','media','baja')),
    descripcion TEXT NOT NULL,
    realizada INTEGER NOT NULL DEFAULT 0
);

-- ---------- Lista de compras ----------

CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cantidad INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    prioridad TEXT NOT NULL CHECK (prioridad IN ('alta','media','baja'))
);
