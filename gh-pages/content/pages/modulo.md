Title: Módulos adicionales de la aplicación
menulabel: Módulos
save_as: modulo.html
URL: Carta-Servicios-STIC/modulo.html
sortorder: 3

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Generador web de páginas estáticas</li>
    </ul>
    <div class="content">
		<p align = justify style='text-indent: 2em'>
			Se ha desarrollado un módulo que permite generar páginas web personalizadas, a partir de un modelo Archimate y una imagen. Para ello, sólo hay que acceder a la web Uploads.
		</p> <br> <br>		
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/uploads.png"></img>
		</p> <br>
			
		<p align = justify>
			En la anterior imagen se aprecian los siguientes elementos:
		</p>
				
		<p align = justify style='text-indent: 2em'>
			<ul>
				<li><b>Nombre de Universidad Corto:</b> Siglas representativas de la universidad.</li>
				<li><b>Nombre Universidad:</b> Nombre completo de la universidad.</li>
				<li><b>Modelo Archimate:</b> Este será nuestro fichero Archimate con la carta de servicios.</li>
				<li><b>Logo:</b> El logo de nuestra universidad.</li>
			</ul>
		</p> <br>
		<p align = justify style='text-indent: 2em'>
			Tras rellenar los campos, seleccionar los archivos y hacer click en Submit, se generará una página Web estática, lista para ser visualizada en local. Dicha página comenzará automáticamente su descarga como un archivo comprimido.
		</p> <br>	
    </div>
</div>

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Generador de Modelo Archimate a partir de Documento Excel</li>
    </ul>
    <div class="content">
		<p align = justify style='text-indent: 2em'>
			Hemos desarrollado un módulo capaz de generar código de Archimate a partir de una hoja de cálculo, lo que permite la introducción de grandes volúmenes de datos de una forma eficiente. Para ello, debemos contar con un documento de Excel que siga la siguiente distribución:
		</p> <br> <br>		
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/formatoexcel.png"></img>
		</p> <br> <br>		

		<p align = justify style='text-indent: 2em'>
			Para que nuestro módulo generador pueda trabajar sobre la hoja de cálculo, es necesario exportarla como fichero XML:
		</p> <br> <br>	

		<p align="center">
			<img border="1" width='60%' height="60%" src="images/saveasxml.png"></img>
		</p> <br> <br>
		<p>
			<div class="alert alert-danger">
				<b>Para que el XML se genere correctamente, </b> el fichero Excel debe cumplir con <b>el formato indicado</b>. 
			</div>
        </p>
				
		<p align = justify style='text-indent: 2em'>
			Una vez generado el XML, podemos ejecutar nuestro módulo CSV_to_Archimate.py. El resultado de esta ejecución será un fichero Archi.archimate, cuyo contenido será un plantilla de archimate que ahora contendrá toda la información recogida en el archivo excel.
		</p>	
    </div>
</div>
