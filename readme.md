# Análisis Bioinformático del Factor de Crecimiento Insulino-símil 1 (IGF-1)

## Descripción del Proyecto
Este proyecto integrador tiene como objetivo automatizar la descarga, procesamiento y visualización estructural del IGF-1 humano (estructura cristalográfica PDB: 1GZR). Se implementan scripts en Python para la recuperación de datos desde bases del NCBI, el cálculo de métricas de secuencias y la identificación de motivos biológicos mediante expresiones regulares. Finalmente, se mapea la topología de la proteína enfatizando sus puentes disulfuro y los dominios C y D de la superficie molecular.

## Prerrequisitos
Para reproducir este análisis se requiere el siguiente entorno de software:
* **Sistema Operativo:** Entorno Linux (o Windows Subsystem for Linux - WSL).
* **Lenguaje:** Python 3.x
* **Librerías:** Biopython (`Bio`), módulo estándar `re`.
* **Software Estructural:** UCSF ChimeraX.

## Instrucciones de Ejecución
1. Clonar el repositorio localmente.
2. Navegar al directorio raíz del proyecto.
3. Ejecutar el script principal de descarga y expresiones regulares:
   ```bash
   python3 data/analisis_igf1.py
