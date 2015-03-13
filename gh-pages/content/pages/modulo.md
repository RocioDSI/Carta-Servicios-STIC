Title: Módulos adicionales de la aplicación
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
		</p> <br> <br>	
    </div>
</div>
