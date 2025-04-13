import sys
import os
import csv



# Agregamos el path si se necesitan módulos de ../Data
sys.path.append(os.path.abspath("../data"))

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=";")
        return list(reader)

def procesar_archivos(ruta, tipo="hogar"):
    datos_unificados = []
    cabecera = None

    for nombre_archivo in os.listdir(ruta):
        if tipo in nombre_archivo and nombre_archivo.endswith(".txt"):
            ruta_archivo = os.path.join(ruta, nombre_archivo)
            filas = leer_archivo(ruta_archivo)

            if not filas:
                continue

            if cabecera is None:
                cabecera = filas[0]
                datos_unificados.extend(filas[1:])
            else:
                if filas[0] == cabecera:
                    datos_unificados.extend(filas[1:])
                else:
                    print(f"⚠️ Cabecera diferente en: {nombre_archivo}")

    return [cabecera] + datos_unificados if cabecera else []

def guardar_en_txt(datos, ruta_destino, nombre_archivo="hogares_unificados.txt"):
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    os.makedirs(ruta_destino, exist_ok=True)

    with open(ruta_completa, mode='w', encoding='utf-8', newline='') as archivo_txt:
        writer = csv.writer(archivo_txt, delimiter=";")
        writer.writerows(datos)

    print(f"✅ Archivo TXT guardado en: {ruta_completa}")

def add_columns_header(header, *args):
    """
    Agrega columnas a una lista.

    Args:
    :param header: Lista a la que se le agregarán las columnas.
    :param *args: Columnas a agregar.
    """

    header.extend(args)