from pdfrw import PdfReader, PdfWriter, PageMerge
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

def create_overlay_pdf(overlay_pdf_path, data):
    packet = canvas.Canvas(overlay_pdf_path, pagesize=letter)
    packet.setFont("Times-Roman", 10)
    fecha_actual = datetime.now()
    dia = fecha_actual.day
    mes = fecha_actual.month
    anio = fecha_actual.year
    dia_str = str(dia)
    anio_str = str(anio)[-2:]
    meses = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    mes_str = meses[mes]

    fecha_dia_x = 445
    fecha_mes_x = 510
    fecha_año_x = 575
    fecha_y = 701

    tabla_datos_identificacion_izquierda_x = 125
    y_nombre = 680
    y_provincia = 670
    y_cum = 660

    tabla_datos_identificacion_derecha_x = 500
    y_fecha_nacimiento = 680
    y_grupo = 670
    y_seccion = 660

    tabla_alerta_x = 51
    tabla_alerta_y = 640


    packet.drawString(fecha_dia_x, fecha_y, f"{dia_str}")
    packet.drawString(fecha_mes_x, fecha_y, f"{mes_str}")
    packet.drawString(fecha_año_x, fecha_y, f"{anio_str}")

    packet.drawString(tabla_datos_identificacion_izquierda_x, y_nombre, data['nombre'])
    packet.drawString(tabla_datos_identificacion_izquierda_x, y_provincia, data['provincia'])
    packet.drawString(tabla_datos_identificacion_izquierda_x, y_cum, data['cum'])

    packet.drawString(tabla_datos_identificacion_derecha_x, y_fecha_nacimiento, data['fecha_nacimiento'])
    packet.drawString(tabla_datos_identificacion_derecha_x, y_grupo, data['grupo'])
    packet.drawString(tabla_datos_identificacion_derecha_x, y_seccion, data['seccion'])


    packet.drawString(tabla_alerta_x, tabla_alerta_y, data['alerta'])



    packet.save()

def modify_existing_pdf(input_pdf, output_pdf, data):
    reader = PdfReader(input_pdf)
    overlay_pdf_path = "temp_overlay.pdf"
    create_overlay_pdf(overlay_pdf_path, data)
    overlay_pdf = PdfReader(overlay_pdf_path).pages[0]
    PageMerge(reader.pages[0]).add(overlay_pdf).render()
    writer = PdfWriter()
    writer.write(output_pdf, reader)
