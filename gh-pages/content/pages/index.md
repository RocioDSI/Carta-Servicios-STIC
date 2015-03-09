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
		<p align = justify style='text-indent: 2em'>
			La Carta de Servicios es un proyecto promovido por el Servicio de Tecnologías de la Información y la Comunicación (STIC) de la Universidad de La Laguna (ULL) que tiene como finalidad el modelado de Carta de Servicios usando técnicas de Arquitectura Empresarial, permitiendo la automatización de tareas a través dicho modelo.
        </p>
    </div>
</div>
<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Arquitectura</li>
    </ul>
    <div class="content">
		<p align = justify style='text-indent: 2em'>
			El modelado de la Carta de Servicios ha sido diseñado de manera que la utilización del proyecto sea independiente de la carta de servicios de la institución, es decir, con sólo exportar el archivo del modelo el proyecto es capaz de interpretarlo y generar toda la estructura web del mismo. Esto permite que el usuario pueda exportar este proyecto de manera fácil y cómoda.
        </p>
		<p align = justify style='text-indent: 2em'>
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
		<p align = justify style='text-indent: 2em'>
			Este proyecto permite convertir modelos de archimate en html. La versión 2.0 soporta tres tipos de objetos: Los grupos, los servicios y los roles. A continuación se muestra el metamodelo sobre el que está construida la aplicación.
		</p> <br> <br>

		<p align="center">
			<img border="1" width='60%' height="60%" src="images/metamodelo.jpg"></img>
		</p> <br> <br>
		
		<p align = justify style='text-indent: 2em'>
			A continuación podemos ver cómo los servicios de una organización se pueden asignar al grupo de servicios al que pertenecen en la vista con nombre <b>Carta de servicios</b>:
		</p> <br> <br>		
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/Cartadeservicios.jpg"></img>
		</p> <br> <br>		

		<p align = justify style='text-indent: 2em'>
			Es frecuente que en una organización clasificar los servicios ofertados según el nivel de criticidad de los mismos. Para ello definimos la vista con nombre <b>Criticidad</b> de la siguiente manera:
		</p> <br> <br>	

		<p align="center">
			<img border="1" width='60%' height="60%" src="images/Criticidad.jpg"></img>
		</p> <br> <br>
				
		<p align = justify style='text-indent: 2em'>
			Es importante restringir el acceso a ciertos servicios por la información que éstos manejan, esto se realiza en la vista con nombre <b>Roles</b>.
		</p> <br> <br>	
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/serviciosroles.jpg"></img>
		</p> <br> <br>	

		<p align = justify style='text-indent: 2em'>
			Además, cada elemento puede contener propiedades que serán también procesadas para mostrarlas en la web.
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/propiedades.png"></img>
		</p>
		<p align = justify style='text-indent: 2em'>
			El resultado de ejecutar el proyecto carta de servicios es una página en la se listan, según alguno de los criterios específicados en las vistas, los servicios con las propiedades que tienen asociadas.
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/html.png"></img>
		</p>
    </div>
</div>
