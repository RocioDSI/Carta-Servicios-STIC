Title: Carta de Servicios STIC
menulabel: Módulos
save_as: modulo.html
URL: Carta-Servicios-STIC/modulo.html
sortorder: 3

<div class="section">
    <ul class="nav nav-tabs header">
        <li class="active">Generador de Modelo Archimate a partir de Documento Excel</li>
    </ul>
    <div class="content">
		<p align = justify style='text-indent: 2em'>
			Hemos desarrollado un módulo capaz de generar código de Archimate, lo que permite la introducción de grandes volúmenes de datos de una forma eficiente.
		</p> <br> <br>

		<p align="center">
			<img border="1" width='60%' height="60%" src="images/metamodelo.jpg"></img>
		</p> <br> <br>
		
		<p align = justify style='text-indent: 2em'>
			Para ello, debemos contar con un documento de Excel que siga la siguiente distribución:
		</p> <br> <br>		
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/formatoexcel.png"></img>
		</p> <br> <br>		

		<p align = justify style='text-indent: 2em'>
			Para que nuestro módulo generador pueda trabajar sobre la hoja de cálculo, es necesario exportarla como fichero XML:
		</p> <br> <br>	

		<p align="center">
			<img border="1" width='60%' height="60%" src="images/saveasxml.jpg"></img>
		</p> <br> <br>
		<p>
			<div class="alert alert-danger">
				<b>Para que el XML se genere correctamente, </b> el fichero Excel debe cumplir con <b>el formato indicado</b>. 
			</div>
        </p>
				
		<p align = justify style='text-indent: 2em'>
			Una vez generado el XML, podemos ejecutar nuestro módulo generamodelo.py. El resultado de esta ejecución serán los ficheros servicios.xml y groups.xml, cuyo contenido debe ser similar al de las siguientes imágenes de ejemplo:
		</p> <br> <br>	
		
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/groups.jpg"></img>
		</p> <br> <br>	
       <p align="center">
			<img border="1" width='60%' height="60%" src="images/services.jpg"></img>
		</p> <br> <br>
		<p>
			<div class="alert alert-danger">
				La generación de los ficheros servicios.xml y groups.xml debe realizarse simultáneamente. Ficheros de ejecuciones distintas no proporcionan los resultados esperados, debido a la generación aleatoria de ID asociado a cada grupo y servicio.  
			</div>
        </p>
		<p align = justify style='text-indent: 2em'>
			Este código debe de incluirse en el fichero de Archimate. La siguiente imagen muestra en qué lugar del fichero se ha de pegar el contenido de cada fichero:
		</p>
		<p align="center">
			<img border="1" width='60%' height="60%" src="images/archiwhere.png"></img>
		</p>
		<p align = justify style='text-indent: 2em'>
			
		</p>
    </div>
</div>
