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
- [Mejoras y Actualizaciones](#-mejoras-y-actualizaciones)
- [Stack tecnológico](#-stack-tecnológico)
- [Instalación rápida (Windows, sin Docker)](#-instalación-rápida-windows-sin-docker)
- [App de escritorio (.exe portable)](#-app-de-escritorio-exe-portable)
- [Despliegue en producción (Docker + PostgreSQL)](#-despliegue-en-producción-docker--postgresql)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Notas de diseño](#-notas-de-diseño)
- [Autores](#-autores)

---

## 🧩 ¿Qué es NODO?

NODO corre entero dentro de la red interna del taller, sin depender de internet. Cualquier
PC de la red abre la app desde el navegador (o desde un ícono de escritorio) y accede a
seis pantallas centrales:

| Pantalla | Qué hace |
|---|---|
| 🖥️ **Mostrador** | Dividido en **Salidas** y **Devoluciones**. Escaneás o escribís el código del elemento y se agrega solo al carrito correspondiente, sin tocar Enter. Si algo que sale ya estaba afuera, cierra ese préstamo viejo solo y lo vuelve a prestar en el mismo movimiento. Incluye stock en vivo y un gráfico de notebooks prestadas por curso, ambos actualizados en tiempo real. |
| 📜 **Historial** | Buscador de todos los movimientos —por curso, profesor, código, fecha o estado—, con columnas ordenables con un clic y exportación a **PDF**. El registro nunca se borra: es la auditoría permanente del taller. |
| 📦 **Inventario** | Alta, edición y baja de elementos, con notas libres, filtro por categoría y exportación a PDF del inventario completo. |
| 🛠️ **Novedades** | Registro de bajas, reparaciones e incidentes por elemento, y por separado, novedades a nivel de **laboratorio** (Lab. E1, E2, Info. 1, Info. 2, Cn). Marcar un retiro pasa el elemento a estado `baja` automáticamente; eliminarla lo revierte si corresponde. |
| ✅ **Tareas** | Asignación de tareas de mantenimiento por laboratorio, con responsable, prioridad (alta/media/baja, con color) y check de "realizada". Ordenable por prioridad o fecha de carga. |
| 🛒 **Compras** | Lista de lo que hace falta comprar, con cantidad y prioridad, exportable a **Excel** con un clic. |

---

## ✨ Funcionalidades

- 🔎 **Búsqueda automática de profesor** por curso + día + hora, a partir del horario cargado.
- 🛒 **Carga en lote** de préstamos y devoluciones desde el Mostrador, escaneando varios
  códigos seguidos — cada elemento se agrega solo al carrito apenas se completa un código
  válido, sin necesidad de tocar Enter.
- 🔄 **Re-préstamo en un solo escaneo**: si un elemento que sigue afuera se vuelve a escanear
  en Salidas, la app cierra ese préstamo viejo sola y lo deja listo para salir de nuevo —
  pensado para cuando vuelven muchos elementos juntos al terminar una clase.
- 📊 **Stock y movimientos en vivo**: paneles en el Mostrador con cuántas notebooks y
  proyectores quedan disponibles, más un gráfico de notebooks prestadas por curso en este
  momento — todo se actualiza solo, sin recargar la página.
- 🧾 **Exportación a PDF** del historial de movimientos y del inventario completo, y a
  **Excel** de la lista de compras, respetando los filtros aplicados en pantalla.
- 💾 **Respaldo automático en Excel**: cada salida y entrada también queda anotada en
  `BacKup.xlsx`, en paralelo a la base de datos — para tener control manual si el servidor
  llegara a caerse.
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

## 🆕 Mejoras y Actualizaciones

Resumen de lo que se trabajó entre ayer y hoy, sobre la base que ya estaba funcionando.

**Mostrador**
- Rediseño en dos columnas — **Salidas** y **Devoluciones** — cada una con su propio
  escaneo, en vez de un único cuadro que adivinaba qué hacer.
- El formulario de "para quién" (curso/día/hora o evento) quedó siempre visible arriba, en
  vez de aparecer recién después de escanear algo.
- El día se autocompleta solo, igual que la hora — con elegir el curso ya alcanza para que
  se complete el profesor y la hora a devolver.
- Un elemento que ya está afuera y se vuelve a escanear en Salidas cierra su préstamo
  viejo solo y queda listo para el nuevo, en un solo movimiento.
- Nuevo gráfico en vivo de notebooks prestadas por curso, hecho a medida a partir de un
  boceto — sube cuando sale una y baja cuando vuelve.

**Historial**
- Columnas ordenables con un clic (fecha, elemento, estado, etc.).
- Se corrigió un error de horario: los movimientos quedaban registrados con 3 horas de más
  por una diferencia entre la hora UTC de la base y la hora real de Argentina.

**Novedades**
- Se agregó **Novedades de laboratorios**, separado de las novedades por elemento — para
  reportar problemas de un laboratorio en general (Lab. E1, E2, Info. 1, Info. 2, Cn), no
  de un elemento puntual.

**Nuevo: Tareas y Compras**
- Pantalla de **Tareas**: asignación por laboratorio, responsable, prioridad con color y
  check de realizada, ordenable.
- Pantalla de **Compras**: cantidad, qué comprar y prioridad, con descarga en Excel.

**Confiabilidad de los datos**
- Se encontró y corrigió un error real: al eliminar una novedad, un elemento que seguía
  prestado podía quedar marcado como "disponible" por error. Se reforzó además la
  verificación para que nunca puedan existir dos préstamos abiertos del mismo elemento al
  mismo tiempo, sin importar la causa.
- Se eliminó un problema de caché del navegador que podía mostrar páginas desactualizadas
  (Historial, Inventario, etc.) mientras otros datos ya estaban al día.
- **Respaldo automático en Excel** (`BacKup.xlsx`): cada salida y entrada se anota también
  ahí, en paralelo a la base de datos, pensado para cuando la app corra en el servidor del
  trabajo — si algo se cae, ese Excel queda como historial de respaldo y se puede seguir
  anotando a mano sin perder lo que ya había.

**Experiencia de uso**
- Se corrigió el contraste del modo oscuro al pasar el mouse por las tablas.
- Botón para cerrar la aplicación de forma prolija, y detección de si ya está corriendo en
  segundo plano (evita quedar "colgada" sin abrir nada al hacer doble clic de nuevo).

---

## 🧱 Stack tecnológico:

| Capa | Tecnología |
|---|---|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| ORM / datos | [SQLAlchemy](https://www.sqlalchemy.org/) — SQLite (local) / PostgreSQL (producción) |
| Plantillas | [Jinja2](https://jinja.palletsprojects.com/) — server-rendered, sin frameworks de frontend |
| PDFs | [ReportLab](https://www.reportlab.com/) |
| Excel | [openpyxl](https://openpyxl.readthedocs.io/) |
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

Para que cualquier compañero del Nodo la use sin instalar nada:

1. Copiá la carpeta **`NODO/`** a la PC destino (no requiere Python instalado ahí).
2. Doble clic en **`NODO.exe`** — arranca el servidor sin ventanas de consola y abre el
   navegador solo.
3. La primera vez crea la base de datos sola; las siguientes respeta lo ya cargado.
4. Botón **"Cerrar aplicación"** en la barra superior para apagarla de forma prolija al
   terminar el turno. Si te olvidás y volvés a abrir el ícono, simplemente te lleva a la
   app que ya estaba corriendo.

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

## 📁 Estructura del proyecto:

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
│   └── BacKup.xlsx           # respaldo automático de salidas/entradas
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
        ├── excel.py             # generación de Excel (compras)
        ├── backup_excel.py      # respaldo BacKup.xlsx de cada salida/entrada
        ├── routers/            # API: prestamos, inventario, novedades, laboratorios, tareas, compras
        ├── templates/          # HTML de cada pantalla
        └── static/             # CSS, JS y assets
```

---

## 📝 Notas de diseño:

- El **historial de préstamos nunca se borra**: es el registro de auditoría del taller. Las
  únicas bajas posibles son de elementos de inventario sin movimientos asociados, o de
  novedades individuales (con reversión automática del estado del elemento si corresponde).
- El campo `categoria` del inventario migrado del Excel original quedó vacío a propósito
  (el archivo fuente no tenía esa columna) — se puede completar de a poco desde la app.
- La base local (SQLite) y la de producción (PostgreSQL) son independientes: lo que se
  carga probando en una PC no viaja solo al servidor.
- El respaldo en Excel (`BacKup.xlsx`) solo agrega filas, nunca reescribe: así, si alguien
  anota movimientos a mano mientras la app está caída, nada de eso se pierde cuando vuelve.

---

## 👤 Autores:

Desarrollado por **Lucca Rando** & **Daniel Yacante**

<div align="center">

*Hecho a medida para el taller de ETEC.*

</div>
