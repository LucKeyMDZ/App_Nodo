<div align="center">

# 🗂️ NODO — Sistema de Préstamos del Taller

**Reemplazo digital del histórico `Stock.xlsm`**, para registrar préstamos y devoluciones de
elementos del taller, encontrar automáticamente al profesor a cargo y mantener un historial
completo y auditable de todos los movimientos.

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-CC2927?logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-local-003B57?logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-producción-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-.exe%20portable-0078D6?logo=windowsxp&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-en%20uso-brightgreen)

</div>

---

## 📖 Índice

- [¿Qué es NODO?](#-qué-es-nodo)
- [Funcionalidades](#-funcionalidades)
- [Stack tecnológico](#-stack-tecnológico)
- [Instalación rápida (Windows, sin Docker)](#-instalación-rápida-windows-sin-docker)
- [App de escritorio (.exe portable)](#-app-de-escritorio-exe-portable)
- [Despliegue en producción (Docker + PostgreSQL)](#-despliegue-en-producción-docker--postgresql)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Notas de diseño](#-notas-de-diseño)
- [Autor](#-autor)

---

## 🧩 ¿Qué es NODO?

NODO corre entero dentro de la red interna del taller, sin depender de internet. Cualquier
PC de la red abre la app desde el navegador (o desde un ícono de escritorio) y accede a
cuatro pantallas centrales:

| Pantalla | Qué hace |
|---|---|
| 🖥️ **Mostrador** | Escaneás o escribís el código del elemento. Si está disponible, arma el préstamo (clase regular con profesor automático, o evento especial). Si ya estaba afuera, lo ofrece marcar como devuelto. Trabaja en modo "carrito": podés escanear varios elementos seguidos antes de confirmar el lote. |
| 📜 **Historial** | Buscador de todos los movimientos —por curso, profesor, código, fecha o estado— con exportación a **PDF**. El registro nunca se borra: es la auditoría permanente del taller. |
| 📦 **Inventario** | Alta, edición y baja de elementos, con notas libres, filtro por categoría y exportación a PDF del inventario completo. |
| 🛠️ **Novedades** | Registro de bajas, reparaciones e incidentes por elemento. Marcar un retiro pasa el elemento a estado `baja` automáticamente; eliminarla lo revierte si corresponde. |

---

## ✨ Funcionalidades

- 🔎 **Búsqueda automática de profesor** por curso + día + hora, a partir del horario cargado.
- 🛒 **Carga en lote** de préstamos y devoluciones desde el Mostrador, escaneando varios
  códigos seguidos — cada elemento se agrega solo al carrito apenas se completa un código
  válido, sin necesidad de tocar Enter.
- 📊 **Stock en vivo**: panel en el Mostrador que muestra cuántas notebooks y proyectores
  quedan disponibles en este momento, actualizado en tiempo real.
- 🧾 **Exportación a PDF** del historial de movimientos y del inventario completo, respetando
  los filtros aplicados en pantalla.
- 🗑️ **Bajas seguras**: un elemento con préstamos o novedades asociadas no se puede eliminar
  por error — hay que darlo de baja explícitamente, así nunca se pierde el historial real.
- 🔁 **Renombrado de códigos con historial intacto**: si se corrige el código de un elemento,
  todos sus movimientos y novedades pasados lo siguen apuntando correctamente.
- 🌗 **Modo oscuro / claro**, con preferencia recordada por navegador — cada persona del
  taller puede elegir el que prefiera.
- 💻 **App de escritorio portable**: un `.exe` para Windows que no requiere instalar Python
  ni depender de una consola — doble clic y listo.
- 🐘 **Doble motor de base de datos**: SQLite para probar localmente sin instalar nada, y
  PostgreSQL vía Docker para el despliegue real en el servidor del taller.

---

## 🧱 Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| ORM / datos | [SQLAlchemy](https://www.sqlalchemy.org/) — SQLite (local) / PostgreSQL (producción) |
| Plantillas | [Jinja2](https://jinja.palletsprojects.com/) — server-rendered, sin frameworks de frontend |
| PDFs | [ReportLab](https://www.reportlab.com/) |
| Empaquetado desktop | [PyInstaller](https://pyinstaller.org/) |
| Contenedores | Docker + Docker Compose |

---

## 🚀 Instalación rápida (Windows, sin Docker)

Ideal para probar la app o desarrollarla localmente, sin depender de un servidor.

```bash
# 1. Instalá Python 3.11+ (tildá "Add python.exe to PATH" durante la instalación)
#    https://www.python.org/downloads/

# 2. Desde la carpeta del proyecto, corré:
run_local.bat
```

La primera vez crea un entorno virtual, instala las dependencias y arma la base de datos
local en SQLite (`backend/local.db`) a partir de `db/schema_sqlite.sql` y `db/seed.sql`.
Cuando la consola diga `Application startup complete`, abrí:

```
http://localhost:8000
```

> Para arrancar de cero con los datos originales: `python init_local_db.py` (¡borra lo que
> hayas cargado probando!).

---

## 🖥️ App de escritorio (.exe portable)

Para que cualquier compañero del taller la use sin instalar nada:

1. Copiá la carpeta **`NODO/`** a la PC destino (no requiere Python instalado ahí).
2. Doble clic en **`NODO.exe`** — arranca el servidor sin ventanas de consola y abre el
   navegador solo.
3. La primera vez crea la base de datos sola; las siguientes respeta lo ya cargado.
4. Botón **"Cerrar aplicación"** en la barra superior para apagarla de forma prolija al
   terminar el turno.

---

## 🐘 Despliegue en producción (Docker + PostgreSQL)

```bash
# 1. Copiá el proyecto al servidor Linux
git clone <este-repo>   # o scp -r

# 2. Configurá la contraseña de la base de datos
cp .env.example .env
nano .env   # cambiá DB_PASSWORD

# 3. Levantá todo
docker compose up -d --build

# 4. Verificá que esté vivo
curl http://localhost:8000/healthz   # → {"status":"ok"}
```

Abrí `http://IP_DEL_SERVIDOR:8000` desde cualquier PC de la red. Postgres carga
`db/schema.sql` + `db/seed.sql` automáticamente la primera vez (volumen vacío).

**Backups periódicos:**
```bash
docker compose exec -T db pg_dump -U prestamos prestamos > backup_$(date +%F).sql
```

---

## 📁 Estructura del proyecto

```
├── docker-compose.yml
├── .env.example
├── run_local.bat            # instalación y arranque rápido en Windows
├── init_local_db.py         # (re)crea la base local SQLite desde cero
├── db/
│   ├── schema.sql            # esquema PostgreSQL (producción)
│   ├── schema_sqlite.sql     # esquema SQLite (local)
│   └── seed.sql               # cursos, materias, profesores, horarios, inventario inicial
├── NODO/                    # app de escritorio empaquetada (.exe portable)
└── backend/
    ├── Dockerfile
    ├── requirements.txt          # despliegue Docker/Postgres
    ├── requirements-local.txt    # pruebas locales en SQLite
    ├── launcher.py                # entry point del .exe empaquetado
    └── app/
        ├── main.py            # rutas de las páginas
        ├── database.py        # conexión + auto-alta de la base
        ├── models.py           # tablas (SQLAlchemy)
        ├── schemas.py          # validación de entrada/salida (Pydantic)
        ├── pdf.py               # generación de PDFs (historial e inventario)
        ├── routers/            # API: prestamos, inventario, novedades
        ├── templates/          # HTML (Mostrador, Historial, Inventario, Novedades)
        └── static/             # CSS y assets
```

---

## 📝 Notas de diseño

- El **historial de préstamos nunca se borra**: es el registro de auditoría del taller. Las
  únicas bajas posibles son de elementos de inventario sin movimientos asociados, o de
  novedades individuales (con reversión automática del estado del elemento si corresponde).
- El campo `categoria` del inventario migrado del Excel original quedó vacío a propósito
  (el archivo fuente no tenía esa columna) — se puede completar de a poco desde la app.
- La base local (SQLite) y la de producción (PostgreSQL) son independientes: lo que se
  carga probando en una PC no viaja solo al servidor.

---

## 👤 Autor

Desarrollado por **Lucca Rando** & **Daniel Yacante**


<div align="center">

*Hecho a medida para el taller de ETEC.*

</div>
