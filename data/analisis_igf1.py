#análisis de IGF-1
#Objetivo principal: automatizar la descarga, filtrado y cálculo de métricas (ARNm y proteína)
#=====================================================

#----------------------------------------------------
#Importación de módulos 
#----------------------------------------------------

import sys #módulo estándar del sistema
import re #módulo para utilizar expresiones regulares

#Módulos de Biopython para análisis de datos biológicos
from Bio import Entrez #para comunicarnos con NCBI
from Bio import SeqIO #para manejo de archivos FASTA/GENBANK

#-----------------------------------------------------------
#Configuración de conexión al NCBI
#-----------------------------------------------------------
#NCBI requiere un correo eléctronico válido 

Entrez.email = "ivaafoletto13@gmail.com"

#---------------------------------------------------------
#Función de descarga automatizada
#---------------------------------------------------------

def descargar_desde_ncbi(db_name, acc_id, file_format, output_filename):
	"""
	Función para descargar secuencias utilizando Entrez.efetch.
	db_name: base de datos (nuccore o protein)
	acc_id: número de acceso 
	file_format: formato deseado (fasta, gb, gp)
	output filename: nombre del archivo donde se guardará la información
	"""

	print(f"Conectanco a NCBI... descargando {acc_id} en formato {file_format}")
	try:
		#consultamos la base de datos y traemos el registro solicitado con efetch
		handle = Entrez.efetch(db=db_name, id=acc_id, rettype=file_format, retmode="text")
		datos= handle.read() #lectura del contenido
		#guardamos en un archivo local
		with open(output_filename, "w") as archivo_salida:
			archivo_salida.write(datos)

		handle.close()
		print(f"[EXITO] Archivo guardado commo: {output_filename}\n")
	
	except Exception as e:
		print(f"[ERROR] No se pudo descargar {acc_id}.")

#-------------------------------------------------------------
#BLOQUE DE EJECUCION
#-------------------------------------------------------------
if __name__ == "__main__":
	print("--- INICIANDO ANÁLISIS PARA IGF-1---")
	#1. Descarga la secuencia de nucleótidos
	descargar_desde_ncbi(db_name= "nuccore", acc_id="NM_000618.5", file_format= "fasta", output_filename= "igf1_nucleotide.fasta")

	#2. Descarga la secuencia de proteína precursora
	descargar_desde_ncbi(db_name= "protein", acc_id= "NP_000609.1", file_format= "fasta", output_filename= "igf1_protein.fasta")
