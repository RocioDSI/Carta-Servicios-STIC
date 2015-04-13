menulabel: Instalación
title: Instalación de Carta de Servicios
save_as: instalacion.html
URL: Carta-Servicios-STIC/instalacion.html
sortorder: 2

<div class="container-fluid">
    <div class="row">
        <div class="col-md-9" role="main">

    <section id="content" class="body">
        
        <div class="entry-content">
			<p align = justify style='text-indent: 2em'>
				La presente guía de instalación proporciona el paso a paso de la instalación y configuración del proyecto bajo un entorno con sistema operativo GNU/Linux, concretamente Ubuntu.
			</p>
		</div>
			</section>
		</div>
</div>

<div class="section">
	<br>
    <ul class="nav nav-tabs header">
        <li class="active">1. Instalar Python.</li>
    </ul>
    <div class="content">
		<div class="alert alert-danger">
			Debido a problemas de compatibilidad entre Django y el intérprete de Python 3.0, es importante instalar la version 2.7.X para evitar posibles errores.
		</div>
	<p align = justify style='text-indent: 2em'>
    Django es un framework de python y, por tanto, necesitamos tenerlo instalado antes de empezar. 
    Para la instalación de dependencias de módulos Python se emplea <i>pip</i>. 
            Se recomienda el uso de <i>virtualenv</i> junto con esta herramienta,
            en las instrucciones no se entrará a explicar su funcionamiento. 
	</p>

        <pre>sudo apt-get install python-pip</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">2. Instalación del Framework Django.</li>
    </ul>
    <div class="content">
        <pre>sudo pip install django</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">3. Instalación de Git.</li>
    </ul>
    <div class="content">
        <pre>sudo apt-get install git</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">4. Clonar el repositorio.</li>
    </ul>
    <div class="content">
        <pre>git clone https://github.com/RocioDSI/Carta-Servicios-STIC.git</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">5. Añadir la plantilla.</li>
    </ul>
    <div class="content">
        <p align = justify style='text-indent: 2em'>Colocar la plantilla con el nombre "plantilla.html" dentro del directorio "servicios/servicios_stic/templates"</p>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">6. Ejecutar el proyecto usando el Rakefile.</li>
    </ul>
    <div class="content">
        <div class="alert alert-danger">
			Si utiliza los comandos descritos para este fichero no es necesario que realice los pasos 7, 8 y 9. Por defecto el fichero de archimate que utiliza el Rakefile para generar las páginas web es Archi_Upload.archimate. Si desea utilizar otro fichero realice el paso 7.
		</div>
        <p align = justify>Si aún no tiene instalado rake ejecute: </p>		
		<pre>sudo apt-get install rake</pre>
		<p align = justify>Puede ver un listado de las tareas definidas en este fichero usando: </p>		
		<pre>rake -T</pre>
        <p align = justify>En el Rakefile están definidas 3 tareas:</p>
        <ol>
			<li><b>runapp:</b> Esta tarea permite crear las páginas html, correr el servidor y abrir el navegador con la URL del index.</li>
			<li><b>server:</b> Esta tarea lanza el servidor local en el puerto 8000.</li>
			<li><b>recargar:</b> Esta tarea actualiza los ficheros html, volviendolos a crear de manera automática.</li>
			<li><b>upload:</b> Esta tarea ejecuta el proyecto junto con el módulo upload y abre el navegador con la URL del módulo.</li>
			<li><b>test:</b> Ejecuta los test de selenium y los de UniTest.</li>
        </ol>
        <p align = justify style='text-indent: 2em'>Para utilizar este fichero simplemente escriba en la consola el siguiente comando:</p>       
        <pre>rake nombre_de_tarea</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">7. Procesar el modelo.</li>
    </ul>
    <div class="content">
        <p align = justify style='text-indent: 2em'>Desde el directorio "servicios" que está situado a nivel superior del proyecto ejecutar el siguiente comando (El nombre del fichero es opcional, si no se especifica se utiliza Archi_Upload.archimate):</p>
        <pre>python main.py nombre_de_fichero</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">8. Ejecutar el servidor.</li>
    </ul>
    <div class="content">
        <p align = justify style='text-indent: 2em'>Desde el directorio "servicios" que está situado a nivel superior del proyecto ejecutar el siguiente comando:</p>
        <pre>python manage.py runserver</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">9. Acceder al contenido.</li>
    </ul>
    <div class="content">
        <p align = justify style='text-indent: 2em'>Visitar el sitio web en la dirección:</p>
        <pre>http://127.0.0.1:8000/</pre>
    </div> <br>
</div>
