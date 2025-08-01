from pathlib import Path

# Dirección del proyecto
PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()

DATA_DIR = PROJECT_ROOT / "data"
DATA_SOURCE_DIR = DATA_DIR / "raw"
DATA_PROCESSED_DIR = DATA_DIR / "processed"

FILENAME_HOGARES_PROCESSED = "hogares_procesados.txt"
FILENAME_INDIVIDUOS_PROCESSED = "individuos_procesados.txt"

RUTA_ARCHIVO_CANASTA = Path('data') / 'Extras' / 'valores-canasta-basica-alimentos-canasta-basica-total-mensual-2016.csv'

# Direcciones para los archivos procesados
HOGARES_PROCESSED_DIR = DATA_PROCESSED_DIR / FILENAME_HOGARES_PROCESSED
INDIVIDUOS_PROCESSED_DIR = DATA_PROCESSED_DIR / FILENAME_INDIVIDUOS_PROCESSED

#Archivo JSON MAPA
COORDENADAS_AGLOMERADOS=PROJECT_ROOT/"data" / "Extras"/"aglomerados_coordenadas.json"

# Este diccionario contiene los nombres de los aglomerados según su número
AGLOMERADOS_NOMBRES = {
    2: "Gran La Plata",
    3: "Bahía Blanca - Cerri",
    4: "Gran Rosario",
    5: "Gran Santa Fe",
    6: "Gran Paraná",
    7: "Posadas",
    8: "Gran Resistencia",
    9: "Comodoro Rivadavia - Rada Tilly",
    10: "Gran Mendoza",
    12: "Corrientes",
    13: "Gran Córdoba",
    14: "Concordia",
    15: "Formosa",
    17: "Neuquén - Plottier",
    18: "Santiago del Estero - La Banda",
    19: "Jujuy - Palpalá",
    20: "Río Gallegos",
    22: "Gran Catamarca",
    23: "Gran Salta",
    25: "La Rioja",
    26: "Gran San Luis",
    27: "Gran San Juan",
    29: "Gran Tucumán - Tafí Viejo",
    30: "Santa Rosa - Toay",
    31: "Ushuaia - Río Grande",
    32: "Ciudad Autónoma de Buenos Aires",
    33: "Partidos del GBA",
    34: "Mar del Plata",
    36: "Río Cuarto",
    38: "San Nicolás - Villa Constitución",
    91: "Rawson - Trelew",
    93: "Viedma - Carmen de Patagones"
}

# Este diccionario contiene los nombres de los aglomerados según su número
REGIONES_NOMBRES = {
    1: "Gran Buenos Aires",
    40: "Noroeste",
    41: "Noreste",
    42: "Cuyo",
    43: "Pampeana",
    44: "Patagonia"}

# Definición de los niveles educativos
NIVELES_EDUCATIVOS = {
    1: "Primario incompleto / Ed. especial",
    2: "Primario completo",
    3: "Secundario incompleto",
    4: "Secundario completo",
    5: "Superior universitario incompleto",
    6: "Superior universitario completo",
    7: "Sin instrucción"
}

# Meses en cada trimestre
TRIMESTRES = {
    1: (1,2,3),
    2: (4,5,6),
    3: (7,8,9),
    4: (10,11,12)
}

