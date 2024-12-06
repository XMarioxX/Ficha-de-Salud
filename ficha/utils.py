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

    packet.drawString(fecha_dia_x, fecha_y, f"{dia_str}")
    packet.drawString(fecha_mes_x, fecha_y, f"{mes_str}")
    packet.drawString(fecha_año_x, fecha_y, f"{anio_str}")

    tabla_datos_identificacion_izquierda_x = 125
    y_nombre = 680
    y_provincia = 670
    y_cum = 660

    packet.drawString(tabla_datos_identificacion_izquierda_x, y_nombre, data['nombre'])
    packet.drawString(tabla_datos_identificacion_izquierda_x, y_provincia, data['provincia'])
    packet.drawString(tabla_datos_identificacion_izquierda_x, y_cum, data['cum'])

    tabla_datos_identificacion_derecha_x = 500
    y_fecha_nacimiento = 680
    y_grupo = 670
    y_seccion = 660

    packet.drawString(tabla_datos_identificacion_derecha_x, y_fecha_nacimiento, data['fecha_nacimiento'])
    packet.drawString(tabla_datos_identificacion_derecha_x, y_grupo, data['grupo'])
    packet.drawString(tabla_datos_identificacion_derecha_x, y_seccion, data['seccion'])

    tabla_alerta_x = 51
    tabla_alerta_y = 640

    packet.drawString(tabla_alerta_x, tabla_alerta_y, data['alerta'])

    tabla_datos_generales_x = 130
    y_grupoRH = 609
    y_peso = 594
    y_talla = 579
    y_imc = 569
    y_alimentacion = 559


    packet.drawString(tabla_datos_generales_x, y_grupoRH, data['grupoRH'])
    packet.drawString(tabla_datos_generales_x, y_peso, data['peso'])
    packet.drawString(tabla_datos_generales_x, y_talla, data['talla'])
    packet.drawString(tabla_datos_generales_x, y_imc, data['imc'])
    packet.drawString(tabla_datos_generales_x, y_alimentacion, data['alimentacion'])

    tabla_datos_generales_afiliaciones_x = 330
    y_nombre_Instituciones= 580
    y_numero_poliza_Instituciones = 570
    y_derecho_habiencia_Instituciones=560
    y_observaciones_Instituciones = 550
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_nombre_Instituciones, data['nombreProveedorInstituciones'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_numero_poliza_Instituciones, data['numeroPolizaProveedorInstituciones'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_derecho_habiencia_Instituciones, data['derechoHabienciaProveedorInstituciones'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_observaciones_Instituciones, data['observacionesProveedorInstituciones'])

    tabla_datos_generales_afiliaciones_x = 420
    y_nombre_Aseguradoras= 580
    y_numero_poliza_Aseguradoras = 570
    y_derecho_habiencia_Aseguradoras=560
    y_observaciones_Aseguradoras = 550

    packet.drawString(tabla_datos_generales_afiliaciones_x, y_nombre_Aseguradoras, data['nombreProveedorAseguradoras'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_numero_poliza_Aseguradoras, data['numeroPolizaProveedorAseguradoras'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_derecho_habiencia_Aseguradoras, data['derechoHabienciaProveedorAseguradoras'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_observaciones_Aseguradoras, data['observacionesProveedorAseguradoras'])

    tabla_datos_generales_afiliaciones_x = 515
    y_nombre_Particular= 580
    y_numero_poliza_Particular = 570
    y_derecho_habiencia_Particular=560
    y_observaciones_Particular = 550

    packet.drawString(tabla_datos_generales_afiliaciones_x, y_nombre_Particular, data['nombreProveedorParticular'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_numero_poliza_Particular, data['numeroPolizaProveedorParticular'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_derecho_habiencia_Particular, data['derechoHabienciaProveedorParticular'])
    packet.drawString(tabla_datos_generales_afiliaciones_x, y_observaciones_Particular, data['observacionesProveedorParticular'])

    tabla_alergias_x = 51
    y_alergias= 520

    packet.drawString(tabla_alergias_x, y_alergias, data['alergias'])

    tabla_tratamientos_x = 51
    y_tratamientos= 478

    packet.drawString(tabla_tratamientos_x, y_tratamientos, data['tratamientosActuales'])

    tabla_historial_medico_1_x = 215
    tabla_historial_medico_especifique_1_x = 245
    y_diabates= 414
    y_hipertension =404
    y_eventoEpileptico =394
    y_problemaCardiaco =384
    y_desmayoMareo =373
    y_asma =363
    y_toxicomanias =353
    y_cirugiaReciente =343
    y_embarazoPuerperio =333
    y_transfucion =322
    y_lesionMusculoEsqueletica =312
    y_ortopedicos =302

    packet.drawString(tabla_historial_medico_1_x, y_diabates, data['diabetes'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_diabates, data['diabetesEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_hipertension, data['hipertension'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_hipertension, data['hipertensionEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_eventoEpileptico, data['eventoEpileptico'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_eventoEpileptico, data['eventoEpilepticoEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_problemaCardiaco, data['problemaCardiaco'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_problemaCardiaco, data['problemaCardiacoEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_desmayoMareo, data['desmayoMareo'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_desmayoMareo, data['desmayoMareoEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_asma, data['asma'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_asma, data['asmaEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_toxicomanias, data['toxicomanias'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_toxicomanias, data['toxicomaniasEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_cirugiaReciente, data['cirugiaReciente'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_cirugiaReciente, data['cirugiaRecienteEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_embarazoPuerperio, data['embarazoPuerperio'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_embarazoPuerperio, data['embarazoPuerperioEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_transfucion, data['transfucion'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_transfucion, data['transfucionEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_lesionMusculoEsqueletica, data['lesionMusculoEsqueletica'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_lesionMusculoEsqueletica, data['lesionMusculoEsqueleticaEspecifique'])
    packet.drawString(tabla_historial_medico_1_x, y_ortopedicos, data['ortopedicos'])
    packet.drawString(tabla_historial_medico_especifique_1_x, y_ortopedicos, data['ortopedicosEspecifique'])

    tabla_historial_medico_2_x = 450
    tabla_historial_medico_especifique_2_x = 480
    y_respiratorios= 414
    y_oftalmicos =404
    y_narizOidos =394
    y_neurologicos =384
    y_hematologicos =373
    y_hepaticos =363
    y_aparatoDigestivo =353
    y_tiroideo =343
    y_dermatologico =333
    y_inmunologicos =322
    y_urinarios =312
    y_covid =302

    packet.drawString(tabla_historial_medico_2_x, y_respiratorios, data['respiratorios'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_respiratorios, data['respiratoriosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_oftalmicos, data['oftalmicos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_oftalmicos, data['oftalmicosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_narizOidos, data['narizOidos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_narizOidos, data['narizOidosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_neurologicos, data['neurologicos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_neurologicos, data['neurologicosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_hematologicos, data['hematologicos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_hematologicos, data['hematologicosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_hepaticos, data['hepaticos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_hepaticos, data['hepaticosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_aparatoDigestivo, data['aparatoDigestivo'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_aparatoDigestivo, data['aparatoDigestivoEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_tiroideo, data['tiroideo'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_tiroideo, data['tiroideoEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_dermatologico, data['dermatologico'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_dermatologico, data['dermatologicoEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_inmunologicos, data['inmunologicos'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_inmunologicos, data['inmunologicosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_urinarios, data['urinarios'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_urinarios, data['urinariosEspecifique'])
    packet.drawString(tabla_historial_medico_2_x, y_covid, data['covid'])
    packet.drawString(tabla_historial_medico_especifique_2_x, y_covid, data['covidEspecifique'])

    tabla_antecedentes_piscologicos_1_x = 215
    tabla_antecedentes_psicologicos_especifique_1_x = 245
    y_cambioAlimentacion= 262
    y_aislamientoPersonal =251
    y_sensacionVacio =236
    y_impotenciaDesesperanza =221
    y_confunsion =206
    y_pensamiento =186
    y_pensarLastimarse =166
    

    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_cambioAlimentacion, data['cambioAlimentacion'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_cambioAlimentacion, data['cambioAlimentacionEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_aislamientoPersonal, data['aislamientoPersonal'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_aislamientoPersonal, data['aislamientoPersonalEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_sensacionVacio, data['sensacionVacio'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_sensacionVacio, data['sensacionVacioEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_impotenciaDesesperanza, data['impotenciaDesesperanza'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_impotenciaDesesperanza, data['impotenciaDesesperanzaEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_confunsion, data['confunsion'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_confunsion, data['confunsionEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_pensamiento, data['pensamiento'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_pensamiento, data['pensamientoEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_1_x, y_pensarLastimarse, data['pensarLastimarse'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_1_x, y_pensarLastimarse, data['pensarLastimarseEspecifique'])

    tabla_antecedentes_piscologicos_2_x = 485
    tabla_antecedentes_psicologicos_especifique_2_x = 515
    y_alteracionesSueño= 262
    y_agotamientoExcesivo =251
    y_doloresInexplicables =236
    y_aumentoToxicomania =221
    y_cambioHumor =206
    y_escucharVoces =186
    y_dificultadTareasDiarias =166

    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_alteracionesSueño, data['alteracionesSueño'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_alteracionesSueño, data['alteracionesSueñoEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_agotamientoExcesivo, data['agotamientoExcesivo'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_agotamientoExcesivo, data['agotamientoExcesivoEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_doloresInexplicables, data['doloresInexplicables'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_doloresInexplicables, data['doloresInexplicablesEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_aumentoToxicomania, data['aumentoToxicomania'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_aumentoToxicomania, data['aumentoToxicomaniaEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_cambioHumor, data['cambioHumor'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_cambioHumor, data['cambioHumorEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_escucharVoces, data['escucharVoces'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_escucharVoces, data['escucharVocesEspecifique'])
    packet.drawString(tabla_antecedentes_piscologicos_2_x, y_dificultadTareasDiarias, data['dificultadTareasDiarias'])
    packet.drawString(tabla_antecedentes_psicologicos_especifique_2_x, y_dificultadTareasDiarias, data['dificultadTareasDiariasEspecifique'])

    tabla_descripcion_tratamiento_medico_x = 55
    y_descripcionTratamientoMedico= 120

    packet.drawString(tabla_descripcion_tratamiento_medico_x, y_descripcionTratamientoMedico, data['descripcionTratamientoMedico'])

    packet.save()

def modify_existing_pdf(input_pdf, output_pdf, data):
    reader = PdfReader(input_pdf)
    overlay_pdf_path = "temp_overlay.pdf"
    create_overlay_pdf(overlay_pdf_path, data)
    overlay_pdf = PdfReader(overlay_pdf_path).pages[0]
    PageMerge(reader.pages[0]).add(overlay_pdf).render()
    writer = PdfWriter()
    writer.write(output_pdf, reader)
