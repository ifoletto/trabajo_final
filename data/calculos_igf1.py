from Bio import SeqIO

#---------------------------------------------------------
#ANALISIS SOBRE NUCLEOTIDOS
#---------------------------------------------------------
def calcular_metricas_nucleotidos(archivo_fasta):
	"""Lee el archivo FASTA del ARMm y calcula la longitud y el porcentraje de GC"""
	print(f"\n --- Métricas de nucleótidos ({archivo_fasta}) ---")
	#Iteramos sobre las secuencias del archivo con SeqIO.parse
	for registro in SeqIO.parse(archivo_fasta, "fasta"):
		secuencia = str(registro.seq).upper()
		longitud = len(secuencia)

		#Cálculo %GC contando las bases
		c_count = secuencia.count('C')
		g_count = secuencia.count('G')
		gc_porcentaje = ((c_count + g_count)/ longitud) * 100

		print(f"ID: {registro.id}")
		print(f"Longitud: {longitud} pb")
		print(f"Contenido GC: {gc_porcentaje:.2f}%")

		return secuencia #Retorno de la secuencia como texto para usarla en Regex

def calcular_composicion_aminoacidos(archivo_fasta):
	"""Lee el FASTA de la proteína y calcula su composición de aminoacidos"""
	print(f"\n MÉTRICAS DE LA PROTEÍNA ({archivo_fasta})---")
	for registro in SeqIO.parse(archivo_fasta, "fasta"):
		secuencia = str(registro.seq).upper()
		longitud = len(secuencia)
		print(f"ID: {registro.id}")
		print(f"Longitud: {longitud} aa")
		print("composición aminoácidos: ")

		conteo_aa ={}
		for aa in secuencia:
			conteo_aa[aa] = conteo_aa.get(aa, 0) + 1

		for aa, cantidad in sorted(conteo_aa.items()):
			porcentaje = (cantidad / longitud) *100
			print(f" {aa}: {cantidad} ({porcentaje:.2f}%)")

if __name__ == "__main__":
	calcular_metricas_nucleotidos("igf1_nucleotide.fasta")
	calcular_composicion_aminoacidos("igf1_protein.fasta")
