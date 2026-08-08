import datetime
import io

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from . import models

ESTADO_COLORES = {
    "prestado": colors.HexColor("#b8860b"),
    "devuelto": colors.HexColor("#1f7a3d"),
    "vencido": colors.HexColor("#b02a2a"),
    "disponible": colors.HexColor("#1f7a3d"),
    "reparacion": colors.HexColor("#b8860b"),
    "baja": colors.HexColor("#b02a2a"),
}

FILTRO_LABELS = {
    "curso": "Curso",
    "profesor": "Profesor / responsable",
    "elemento_codigo": "Código del elemento",
    "desde": "Desde",
    "hasta": "Hasta",
    "estado": "Estado",
    "q": "Búsqueda",
    "categoria": "Categoría",
}


def _filtros_aplicados(filtros: dict, nombre_universo: str = "movimientos") -> str:
    partes = [f"{FILTRO_LABELS[k]}: {v}" for k, v in filtros.items() if v]
    return " · ".join(partes) if partes else f"Sin filtros (todos los {nombre_universo})"


def generar_pdf_historial(movimientos: list["models.Movimiento"], filtros: dict) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        leftMargin=1.2 * cm,
        rightMargin=1.2 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
        title="Historial de préstamos - Taller",
    )
    styles = getSampleStyleSheet()

    elementos = [
        Paragraph("Historial de préstamos — Taller ETEC", styles["Title"]),
        Paragraph(
            f"Generado el {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles["Normal"],
        ),
        Paragraph(_filtros_aplicados(filtros), styles["Normal"]),
        Spacer(1, 0.5 * cm),
    ]

    encabezado = [
        "Salida", "Elemento", "Código", "Curso / evento",
        "Responsable", "Hora a devolver", "Devuelto", "Estado",
    ]
    filas = [encabezado]
    estados_fila = []
    for m in movimientos:
        filas.append([
            m.fecha_hora.strftime("%d/%m/%Y %H:%M"),
            m.elemento.nombre if m.elemento else "-",
            m.elemento_codigo,
            m.curso.nombre if m.curso else (m.evento_nombre or "-"),
            m.profesor_responsable,
            m.hora_devolver,
            m.fecha_hora_devolucion_real.strftime("%d/%m/%Y %H:%M")
            if m.fecha_hora_devolucion_real else "—",
            m.estado,
        ])
        estados_fila.append(m.estado)

    if len(filas) == 1:
        elementos.append(Paragraph("No hay movimientos que coincidan con la búsqueda.", styles["Normal"]))
    else:
        tabla = Table(filas, repeatRows=1)
        estilo = [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f4f4")]),
        ]
        for i, estado in enumerate(estados_fila, start=1):
            color = ESTADO_COLORES.get(estado)
            if color:
                estilo.append(("TEXTCOLOR", (7, i), (7, i), color))
                estilo.append(("FONTNAME", (7, i), (7, i), "Helvetica-Bold"))
        tabla.setStyle(TableStyle(estilo))
        elementos.append(tabla)
        elementos.append(Spacer(1, 0.3 * cm))
        elementos.append(Paragraph(f"Total de movimientos: {len(movimientos)}", styles["Normal"]))

    doc.build(elementos)
    buffer.seek(0)
    return buffer


def generar_pdf_inventario(items: list["models.Inventario"], filtros: dict) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        leftMargin=1.2 * cm,
        rightMargin=1.2 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
        title="Inventario - Taller",
    )
    styles = getSampleStyleSheet()
    celda_normal = styles["Normal"]

    elementos = [
        Paragraph("Inventario — Taller ETEC", styles["Title"]),
        Paragraph(
            f"Generado el {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}",
            styles["Normal"],
        ),
        Paragraph(_filtros_aplicados(filtros, "elementos"), styles["Normal"]),
        Spacer(1, 0.5 * cm),
    ]

    encabezado = ["Código", "Nombre", "Categoría", "Estado", "Notas"]
    filas = [encabezado]
    estados_fila = []
    for e in items:
        filas.append([
            e.codigo,
            e.nombre,
            e.categoria or "—",
            e.estado,
            Paragraph(e.notas or "—", celda_normal),
        ])
        estados_fila.append(e.estado)

    if len(filas) == 1:
        elementos.append(Paragraph("No hay elementos que coincidan con la búsqueda.", styles["Normal"]))
    else:
        tabla = Table(filas, repeatRows=1, colWidths=[3.2 * cm, 5.5 * cm, 3.5 * cm, 2.5 * cm, None])
        estilo = [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2c3e50")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f4f4")]),
        ]
        for i, estado in enumerate(estados_fila, start=1):
            color = ESTADO_COLORES.get(estado)
            if color:
                estilo.append(("TEXTCOLOR", (3, i), (3, i), color))
                estilo.append(("FONTNAME", (3, i), (3, i), "Helvetica-Bold"))
        tabla.setStyle(TableStyle(estilo))
        elementos.append(tabla)
        elementos.append(Spacer(1, 0.3 * cm))
        elementos.append(Paragraph(f"Total de elementos: {len(items)}", styles["Normal"]))

    doc.build(elementos)
    buffer.seek(0)
    return buffer
