
from django.shortcuts import render_to_response
from servicios_stic.forms import UploadForm
from servicios_stic.models import Document
from django.shortcuts import render, redirect
from django.http import HttpResponse

import main
import os 
import zipfile

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save(form)
            newimg = Document(imagefile = request.FILES['imagefile'])
            newimg.save(form)
            nombreuni = request.POST.get('Nombre_Universidad')
            nombrecorto = request.POST.get('Nombre_Universidad_Corto')
            main.main(nombreuni,nombrecorto)
            zf = zipfile.ZipFile((""+ str(nombrecorto) + ".zip"), "w")
            for dirname, subdirs, files in os.walk("servicios_stic/templates/"+ nombrecorto):
              zf.write(dirname)
              for filename in files:
               zf.write(os.path.join(dirname, filename))
            zf.close()

            response = HttpResponse(open(""+nombrecorto+".zip").read(),content_type="application/zip")  
            response["Content-Disposition"] = "attachment; filename="+ nombrecorto +".zip"  
            return response
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form}) 
    
def index(request):
 response = render_to_response('index.html')
 return response
  
def soporte_tic_a_la_docencia(request):
 response = render_to_response('soporte_tic_a_la_docencia.html')
 return response
	   
	   
def soporte_tic_a_la_investigacion(request):
 response = render_to_response('soporte_tic_a_la_investigacion.html')
 return response
	   
	   
def soporte_tic_a_la_gestion(request):
 response = render_to_response('soporte_tic_a_la_gestion.html')
 return response
	   
	   
def correo_y_colaboracion(request):
 response = render_to_response('correo_y_colaboracion.html')
 return response
	   
	   
def publicacion_web(request):
 response = render_to_response('publicacion_web.html')
 return response
	   
	   
def soporte_a_equipamiento_puesto_de_trabajo(request):
 response = render_to_response('soporte_a_equipamiento_puesto_de_trabajo.html')
 return response
	   
	   
def comunicaciones(request):
 response = render_to_response('comunicaciones.html')
 return response
	   
	   
def gestion_de_identidades(request):
 response = render_to_response('gestion_de_identidades.html')
 return response
	   
	   
def alta(request):
 response = render_to_response('alta.html')
 return response
	   
	   
def baja(request):
 response = render_to_response('baja.html')
 return response
	   
	   
def pdi(request):
 response = render_to_response('pdi.html')
 return response
	   
	   
def pas(request):
 response = render_to_response('pas.html')
 return response
	   
	   
def exalumnos(request):
 response = render_to_response('exalumnos.html')
 return response
	   
	   
def alumnos(request):
 response = render_to_response('alumnos.html')
 return response
	   
	   
def aaaaull(request):
 response = render_to_response('aaaaull.html')
 return response
	   
	   
def docencia_virtual(request):
 response = render_to_response('docencia_virtual.html')
 return response
	   
	   
def soporte_a_aulas_de_informatica_de_libre_acceso(request):
 response = render_to_response('soporte_a_aulas_de_informatica_de_libre_acceso.html')
 return response
	   
	   
def soporte_a_aulas_de_informatica_de_uso_docente(request):
 response = render_to_response('soporte_a_aulas_de_informatica_de_uso_docente.html')
 return response
	   
	   
def soporte_a_aulas_multimedia(request):
 response = render_to_response('soporte_a_aulas_multimedia.html')
 return response
	   
	   
def soporte_a_la_elaboracion_de_contenidos_docentes(request):
 response = render_to_response('soporte_a_la_elaboracion_de_contenidos_docentes.html')
 return response
	   
	   
def soporte_a_realizacion_y_correccion_de_examenes(request):
 response = render_to_response('soporte_a_realizacion_y_correccion_de_examenes.html')
 return response
	   
	   
def gestion_de_licencias_software_para_docencia(request):
 response = render_to_response('gestion_de_licencias_software_para_docencia.html')
 return response
	   
	   
def supercomputacion(request):
 response = render_to_response('supercomputacion.html')
 return response
	   
	   
def alojamiento_de_infraestructuras(request):
 response = render_to_response('alojamiento_de_infraestructuras.html')
 return response
	   
	   
def gestion_de_licencias_software_para_investigacion(request):
 response = render_to_response('gestion_de_licencias_software_para_investigacion.html')
 return response
	   
	   
def asesoramiento_adquisicion_infraestructuras_y_servicios_tic_para_investigacion(request):
 response = render_to_response('asesoramiento_adquisicion_infraestructuras_y_servicios_tic_para_investigacion.html')
 return response
	   
	   
def gestion_academica(request):
 response = render_to_response('gestion_academica.html')
 return response
	   
	   
def gestion_academica_acceso_a_grado(request):
 response = render_to_response('gestion_academica_acceso_a_grado.html')
 return response
	   
	   
def gestion_academica_acceso_a_postgrado(request):
 response = render_to_response('gestion_academica_acceso_a_postgrado.html')
 return response
	   
	   
def gestion_academica_actas(request):
 response = render_to_response('gestion_academica_actas.html')
 return response
	   
	   
def gestion_academica_automatricula(request):
 response = render_to_response('gestion_academica_automatricula.html')
 return response
	   
	   
def gestion_academica_becas(request):
 response = render_to_response('gestion_academica_becas.html')
 return response
	   
	   
def gestion_academica_deposito_de_titulos(request):
 response = render_to_response('gestion_academica_deposito_de_titulos.html')
 return response
	   
	   
def gestion_academica_ensenanzas_propias(request):
 response = render_to_response('gestion_academica_ensenanzas_propias.html')
 return response
	   
	   
def gestion_academica_gestion_de_horarios(request):
 response = render_to_response('gestion_academica_gestion_de_horarios.html')
 return response
	   
	   
def gestion_academica_gestion_de_postgrado(request):
 response = render_to_response('gestion_academica_gestion_de_postgrado.html')
 return response
	   
	   
def gestion_academica_guias_docentes(request):
 response = render_to_response('gestion_academica_guias_docentes.html')
 return response
	   
	   
def gestion_academica_movilidad_internacional(request):
 response = render_to_response('gestion_academica_movilidad_internacional.html')
 return response
	   
	   
def gestion_academica_necesidades_educativas_especiales(request):
 response = render_to_response('gestion_academica_necesidades_educativas_especiales.html')
 return response
	   
	   
def gestion_academica_plan_docente(request):
 response = render_to_response('gestion_academica_plan_docente.html')
 return response
	   
	   
def gestion_academica_secretaria_virtual(request):
 response = render_to_response('gestion_academica_secretaria_virtual.html')
 return response
	   
	   
def gestion_academica_tesis(request):
 response = render_to_response('gestion_academica_tesis.html')
 return response
	   
	   
def gestion_academica_practicas_de_empresa(request):
 response = render_to_response('gestion_academica_practicas_de_empresa.html')
 return response
	   
	   
def gestion_de_la_investigacion(request):
 response = render_to_response('gestion_de_la_investigacion.html')
 return response
	   
	   
def gestion_economica(request):
 response = render_to_response('gestion_economica.html')
 return response
	   
	   
def gestion_economica_contabilidad_analitica(request):
 response = render_to_response('gestion_economica_contabilidad_analitica.html')
 return response
	   
	   
def gestion_economica_contratacion(request):
 response = render_to_response('gestion_economica_contratacion.html')
 return response
	   
	   
def gestion_economica_tesoreria(request):
 response = render_to_response('gestion_economica_tesoreria.html')
 return response
	   
	   
def gestion_economica_gestion_de_fondos_feder(request):
 response = render_to_response('gestion_economica_gestion_de_fondos_feder.html')
 return response
	   
	   
def gestion_economica_patrimonio_e_inventario(request):
 response = render_to_response('gestion_economica_patrimonio_e_inventario.html')
 return response
	   
	   
def gestion_economica_ingresos(request):
 response = render_to_response('gestion_economica_ingresos.html')
 return response
	   
	   
def gestion_economica_presupuestos(request):
 response = render_to_response('gestion_economica_presupuestos.html')
 return response
	   
	   
def gestion_rrhh(request):
 response = render_to_response('gestion_rrhh.html')
 return response
	   
	   
def gestion_rrhh_convocartorias_de_acceso(request):
 response = render_to_response('gestion_rrhh_convocartorias_de_acceso.html')
 return response
	   
	   
def gestion_rrhh_diseno_de_plantilla(request):
 response = render_to_response('gestion_rrhh_diseno_de_plantilla.html')
 return response
	   
	   
def gestion_rrhh_control_horario(request):
 response = render_to_response('gestion_rrhh_control_horario.html')
 return response
	   
	   
def gestion_rrhh_valoracion_del_desempeno(request):
 response = render_to_response('gestion_rrhh_valoracion_del_desempeno.html')
 return response
	   
	   
def gestion_rrhh_formacion(request):
 response = render_to_response('gestion_rrhh_formacion.html')
 return response
	   
	   
def gestion_rrhh_prevencion(request):
 response = render_to_response('gestion_rrhh_prevencion.html')
 return response
	   
	   
def gestion_rrhh_retribuciones(request):
 response = render_to_response('gestion_rrhh_retribuciones.html')
 return response
	   
	   
def extension_universitaria(request):
 response = render_to_response('extension_universitaria.html')
 return response
	   
	   
def extension_universitaria_actividades_deportivas(request):
 response = render_to_response('extension_universitaria_actividades_deportivas.html')
 return response
	   
	   
def extension_universitaria_bolsa_de_alojamiento(request):
 response = render_to_response('extension_universitaria_bolsa_de_alojamiento.html')
 return response
	   
	   
def extension_universitaria_ensenanza_no_reglada(request):
 response = render_to_response('extension_universitaria_ensenanza_no_reglada.html')
 return response
	   
	   
def extension_universitaria_prestamo_de_bicicletas(request):
 response = render_to_response('extension_universitaria_prestamo_de_bicicletas.html')
 return response
	   
	   
def secretaria_general(request):
 response = render_to_response('secretaria_general.html')
 return response
	   
	   
def secretaria_general_archivo_universitario(request):
 response = render_to_response('secretaria_general_archivo_universitario.html')
 return response
	   
	   
def secretaria_general_protocolo(request):
 response = render_to_response('secretaria_general_protocolo.html')
 return response
	   
	   
def secretaria_general_registro(request):
 response = render_to_response('secretaria_general_registro.html')
 return response
	   
	   
def secretaria_general_gestor_documental(request):
 response = render_to_response('secretaria_general_gestor_documental.html')
 return response
	   
	   
def secretaria_general_convenios(request):
 response = render_to_response('secretaria_general_convenios.html')
 return response
	   
	   
def secretaria_general_normativa(request):
 response = render_to_response('secretaria_general_normativa.html')
 return response
	   
	   
def secretaria_general_elecciones_universitarias(request):
 response = render_to_response('secretaria_general_elecciones_universitarias.html')
 return response
	   
	   
def gestion_infraestructuras(request):
 response = render_to_response('gestion_infraestructuras.html')
 return response
	   
	   
def gestion_infraestructuras_control_de_acceso(request):
 response = render_to_response('gestion_infraestructuras_control_de_acceso.html')
 return response
	   
	   
def gestion_infraestructuras_gestion_de_almacen(request):
 response = render_to_response('gestion_infraestructuras_gestion_de_almacen.html')
 return response
	   
	   
def gestion_infraestructuras_prevencion_de_riesgos_laborales(request):
 response = render_to_response('gestion_infraestructuras_prevencion_de_riesgos_laborales.html')
 return response
	   
	   
def gestion_infraestructuras_gestion_de_espacios(request):
 response = render_to_response('gestion_infraestructuras_gestion_de_espacios.html')
 return response
	   
	   
def biblioteca_universitaria(request):
 response = render_to_response('biblioteca_universitaria.html')
 return response
	   
	   
def biblioteca_universitaria_repositorio_institucional(request):
 response = render_to_response('biblioteca_universitaria_repositorio_institucional.html')
 return response
	   
	   
def comunicacion_carteleria_digital(request):
 response = render_to_response('comunicacion_carteleria_digital.html')
 return response
	   
	   
def comunicacion_eventos(request):
 response = render_to_response('comunicacion_eventos.html')
 return response
	   
	   
def comunicacion_prensa_universitaira(request):
 response = render_to_response('comunicacion_prensa_universitaira.html')
 return response
	   
	   
def gestion_calidad(request):
 response = render_to_response('gestion_calidad.html')
 return response
	   
	   
def gestion_calidad_encuestas(request):
 response = render_to_response('gestion_calidad_encuestas.html')
 return response
	   
	   
def gestion_calidad_evaluacion_de_la_actividad_docente_del_profesorado(request):
 response = render_to_response('gestion_calidad_evaluacion_de_la_actividad_docente_del_profesorado.html')
 return response
	   
	   
def gestion_calidad_herramienta_para_evaluacion_efqm(request):
 response = render_to_response('gestion_calidad_herramienta_para_evaluacion_efqm.html')
 return response
	   
	   
def analisis_de_datos(request):
 response = render_to_response('analisis_de_datos.html')
 return response
	   
	   
def atencion_al_usuario__cau_(request):
 response = render_to_response('atencion_al_usuario__cau_.html')
 return response
	   
	   
def gestion_de_publicaciones(request):
 response = render_to_response('gestion_de_publicaciones.html')
 return response
	   
	   
def correo_electronico_pdi_y_pas(request):
 response = render_to_response('correo_electronico_pdi_y_pas.html')
 return response
	   
	   
def correo_electronico_estudiantes(request):
 response = render_to_response('correo_electronico_estudiantes.html')
 return response
	   
	   
def correo_electronico_preuniversitarios(request):
 response = render_to_response('correo_electronico_preuniversitarios.html')
 return response
	   
	   
def correo_electronico_egresados(request):
 response = render_to_response('correo_electronico_egresados.html')
 return response
	   
	   
def notificaciones_listas_de_distribucion(request):
 response = render_to_response('notificaciones_listas_de_distribucion.html')
 return response
	   
	   
def notificaciones_sms(request):
 response = render_to_response('notificaciones_sms.html')
 return response
	   
	   
def notificaciones_redes_sociales(request):
 response = render_to_response('notificaciones_redes_sociales.html')
 return response
	   
	   
def espacios_web_colaborativos(request):
 response = render_to_response('espacios_web_colaborativos.html')
 return response
	   
	   
def intercambio_de_ficheros_ftp(request):
 response = render_to_response('intercambio_de_ficheros_ftp.html')
 return response
	   
	   
def intercambio_de_ficheros_ficheros_gran_volumen(request):
 response = render_to_response('intercambio_de_ficheros_ficheros_gran_volumen.html')
 return response
	   
	   
def videoconferencia_web(request):
 response = render_to_response('videoconferencia_web.html')
 return response
	   
	   
def videoconferencia_sala(request):
 response = render_to_response('videoconferencia_sala.html')
 return response
	   
	   
def videoconferencia_inmersion(request):
 response = render_to_response('videoconferencia_inmersion.html')
 return response
	   
	   
def web_institucional(request):
 response = render_to_response('web_institucional.html')
 return response
	   
	   
def sede_electronica(request):
 response = render_to_response('sede_electronica.html')
 return response
	   
	   
def intranet(request):
 response = render_to_response('intranet.html')
 return response
	   
	   
def intranet_portal_del_investigador(request):
 response = render_to_response('intranet_portal_del_investigador.html')
 return response
	   
	   
def intranet_portal_del_empleado(request):
 response = render_to_response('intranet_portal_del_empleado.html')
 return response
	   
	   
def intranet_portal_del_estudiante_o_secretaria_virtual(request):
 response = render_to_response('intranet_portal_del_estudiante_o_secretaria_virtual.html')
 return response
	   
	   
def contenidos_digitales_material_audiovisual(request):
 response = render_to_response('contenidos_digitales_material_audiovisual.html')
 return response
	   
	   
def contenidos_digitales_material_fotografico(request):
 response = render_to_response('contenidos_digitales_material_fotografico.html')
 return response
	   
	   
def contenidos_digitales_contenidos_docentes(request):
 response = render_to_response('contenidos_digitales_contenidos_docentes.html')
 return response
	   
	   
def contenidos_digitales_contenidos_docentes_de_acceso_abierto(request):
 response = render_to_response('contenidos_digitales_contenidos_docentes_de_acceso_abierto.html')
 return response
	   
	   
def grabacion_y_difusion_de_eventos(request):
 response = render_to_response('grabacion_y_difusion_de_eventos.html')
 return response
	   
	   
def servicio_de_provision_y_renovacion_del_puesto_de_trabajo(request):
 response = render_to_response('servicio_de_provision_y_renovacion_del_puesto_de_trabajo.html')
 return response
	   
	   
def mantenimiento_de_equipamiento_informatico_corporativo(request):
 response = render_to_response('mantenimiento_de_equipamiento_informatico_corporativo.html')
 return response
	   
	   
def mantenimiento_de_software_corporativo(request):
 response = render_to_response('mantenimiento_de_software_corporativo.html')
 return response
	   
	   
def impresion_corporativa(request):
 response = render_to_response('impresion_corporativa.html')
 return response
	   
	   
def seguridad_integral_en_el_puesto_de_trabajo(request):
 response = render_to_response('seguridad_integral_en_el_puesto_de_trabajo.html')
 return response
	   
	   
def asesoramiento_para_adquisicion_de_equipamiento_informatico_y_software(request):
 response = render_to_response('asesoramiento_para_adquisicion_de_equipamiento_informatico_y_software.html')
 return response
	   
	   
def soporte_a_eventos_especiales(request):
 response = render_to_response('soporte_a_eventos_especiales.html')
 return response
	   
	   
def telefonia_fija(request):
 response = render_to_response('telefonia_fija.html')
 return response
	   
	   
def telefonia_movil(request):
 response = render_to_response('telefonia_movil.html')
 return response
	   
	   
def fax(request):
 response = render_to_response('fax.html')
 return response
	   
	   
def consulta_tarificacion_telefonica(request):
 response = render_to_response('consulta_tarificacion_telefonica.html')
 return response
	   
	   
def conexion_a_red_cableada(request):
 response = render_to_response('conexion_a_red_cableada.html')
 return response
	   
	   
def conexion_a_red_inalambrica(request):
 response = render_to_response('conexion_a_red_inalambrica.html')
 return response
	   
	   
def conexion_externo_a_red_de_comunicaciones(request):
 response = render_to_response('conexion_externo_a_red_de_comunicaciones.html')
 return response
	   
	   
def directorio(request):
 response = render_to_response('directorio.html')
 return response
	   
	   
def gestion_de_credenciales(request):
 response = render_to_response('gestion_de_credenciales.html')
 return response
	   
	   
def tarjeta_universitaria_inteligente(request):
 response = render_to_response('tarjeta_universitaria_inteligente.html')
 return response
	   
	   
def autenticacion_centralizada(request):
 response = render_to_response('autenticacion_centralizada.html')
 return response
	   
	   
def gestion_de_certificados(request):
 response = render_to_response('gestion_de_certificados.html')
 return response
	   
	   