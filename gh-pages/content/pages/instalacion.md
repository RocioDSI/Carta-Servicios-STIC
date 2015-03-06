menulabel: Instalacion
title: Instalación de Carta de Servicios
save_as: instalacion.html
URL: Carta-Servicios-STIC/instalacion.html
sortorder: 2

<div class="container-fluid">
    <div class="row">
        <div class="col-md-9" role="main">

    <section id="content" class="body">
        
        <div class="entry-content">
			<p>
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
    <p>
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
        <pre>git clone git@github.com:RocioDSI/Carta-Servicios-STIC.git</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">5. Añadir la plantilla.</li>
    </ul>
    <div class="content">
        <p>Colocar la plantilla con el nombre "plantilla.html" dentro del directorio "servicios/servicios_stic/templates"</p>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">6. Procesar el modelo.</li>
    </ul>
    <div class="content">
        <p>Desde el directorio "servicios" que está situado a nivel superior del proyecto ejecutar el siguiente comando:</p>
        <pre>python main.py</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">7. Procesar el modelo.</li>
    </ul>
    <div class="content">
        <p>Desde el directorio "servicios" que está situado a nivel superior del proyecto ejecutar el siguiente comando:</p>
        <pre>python manage.py runserver</pre>
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">8. Acceder al contenido.</li>
    </ul>
    <div class="content">
        <p>Visitar el sitio web en la dirección:</p>
        <pre>http://127.0.0.1:8000/</pre>
    </div>
</div>
