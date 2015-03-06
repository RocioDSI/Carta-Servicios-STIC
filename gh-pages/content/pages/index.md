Title: Carta de Servicios STIC
menulabel: Inicio
save_as: index.html
URL: Carta-Servicios-STIC/index.html
sortorder: 0

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">En que consiste la Carta de Servicios</li>
    </ul>
    <div class="content">
        <p>
			La Carta de Servicios es un proyecto promovido por el Servicio de Tecnologías de la Información y la Comunicación (STIC) de la Universidad de La Laguna (ULL) que tiene como finalidad el modelado de Carta de Servicios usando técnicas de Arquitectura Empresarial, permitiendo la automatización de tareas a través dicho modelo.
        </p>
    </div>
</div>
<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Arquitectura</li>
    </ul>
    <div class="content">
        <p>
			El modelado de la Carta de Servicios ha sido diseñado de manera que la utilización del proyecto sea independiente de la carta de servicios de la institución, es decir, con sólo exportar el archivo del modelo el proyecto es capaz de interpretarlo y generar toda la estructura web del mismo. Esto permite que el usuario pueda exportar este proyecto de manera fácil y cómoda.
        </p>
        <p> 
			La arquitectura Modelo-Vista-Controlador (MVC) que provee el framework <a href="https://www.djangoproject.com/" target="_blank">Django</a> facilita la creación de
            aplicaciones o módulos que agrupan un conjunto de características asociadas al mismo concepto con capacidad de configuración propia.
        </p>
        <p>
			<div class="alert alert-danger">
				<b>La Imagen Corporativa y signos distintivos de la Universidad de La Laguna</b> están sujetos a derechos de <b>Propiedad Intelectual</b>, por lo que deberán ser reemplazados. 
			</div>
        </p>
    </div>
</div>
<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Características y Funcionalidades</li>
    </ul>
    <div class="content">
		<p>
			El modelado de la Carta de Servicios nos permite realizar modificaciones en un modelo, como el que vemos en la imagen de abajo, y que éstas se vean reflejadas en la web de nuestra institución. En este caso hemos añadido un nuevo grupo de servicios llamado “Soporte TIC a la gestión” que contiene un servicio llamado “Gestión académica”.
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/modelo_ampliado.png"></img>
		</p>
		<p>
			Además, cada servicio puede contener propiedades que serán también procesadas para mostrarlas en la web. En este caso el servicio "Gestión académica" tiene las siguientes propiedades:
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/propiedades.png"></img>
		</p>
		<p>
			El resultado de ejecutar el proyecto carta de servicios es una página en la que se recoge el nuevo grupo de servicios, el nuevo servicio y sus propiedades:
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/modelo_ampliado_html.png"></img>
		</p>
    </div>
</div>
