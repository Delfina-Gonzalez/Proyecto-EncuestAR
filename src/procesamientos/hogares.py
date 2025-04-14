import sys
import os
import csv



# PROCESAMIENTO HOGARES
def clasificar_hogar_hab(cant_personas):
    personas = int(cant_personas)
    
    if personas == 1:
        tipo = "Unipersonal"
    elif 2 <= personas <= 4:
        tipo = "Nuclear"
    elif personas >= 5:
        tipo = "Extendido"
    return tipo

def clasificar_hogar_techo(material_nro):
    
    material_nro = int(material_nro)
    
    if 1 <= material_nro <= 4:
        tipo = "Material durable"
    elif 5 <= material_nro <= 7:
        tipo = "Material precario"
    elif material_nro == 9:
        tipo = "No aplica"
    return tipo

def clasificar_hogar_densidad_hab(cant_personas, cant_hab):
    cant_hab=int(cant_hab)
    cant_personas=int(cant_personas)
        # Intentamos dividir las variables
    personas_por_hab = float(cant_personas / cant_hab)

        # Clasificación según la densidad
    if personas_por_hab < 1:
        tipo = "Bajo"
    elif 1 <= personas_por_hab <= 2:
        tipo = "Medio"
    elif personas_por_hab > 2:
        tipo = "Alto"
        
    return tipo

def clasificar_hogar_habitabilidad(agua, origen_agua, baño, ubi_baño, tipo_baño, desague, techo_material, piso_material):
 
    agua=int(agua)
    origen_agua=int(origen_agua)
    baño=int(baño)
    tipo_baño=int(tipo_baño)
    desague=int(desague)
    piso_material=int(piso_material)
    
    problemas = 0
    
    # 1. Agua 
    if agua == 2:  # Agua fuera de la vivienda, pero dentro del terreno
        problemas += 2
    elif agua == 3:  # Agua fuera del terreno
        problemas += 3

    # 2. Origen del agua
    if origen_agua == 2:  # Perforación con bomba a motor
        problemas += 1
    elif origen_agua == 3:  # Perforación con bomba manual
        problemas += 2
    elif origen_agua == 4:  # Otra fuente
        problemas += 3

    # 3. Baño
    if baño == 2:
        return 'Insuficiente'

    # 4. Ubicación del baño
    if  ubi_baño == 2:  # Baño fuera de la vivienda, pero dentro del terreno
        problemas += 1
    elif ubi_baño == 3:   # Baño fuera del terreno
        problemas += 2

    # 5. Tipo de baño
    if tipo_baño == 1:  # Inodoro con arrastre de agua
        problemas += 0
    elif tipo_baño == 2:  # Inodoro sin arrastre de agua
        problemas += 3
    else:  # Letrina
        problemas += 4

    # 6. Desagüe del baño
    if desague == 2:  # Desagüe a cámara séptica o pozo ciego
        problemas += 1
    elif desague == 3:  # Desagüe solo a pozo ciego
        problemas += 2
    elif desague == 4:  # Desagüe a hoyo/excavación
        problemas += 3

    # 7. Material del techo
    if techo_material == "Material precario":
        problemas += 6

    # 8. Material del piso
    if piso_material == 2:
        problemas += 1
    else:  # Material precario
        problemas += 2

    # Clasificación final según los problemas
    if problemas >= 10:
        return "Insuficiente"
    elif 6 <= problemas < 10:
        return "Regular"
    elif 4 <= problemas < 6:
        return "Saludable"
    else:
        return "Buena"

def proceso_hogar_fila(fila):        
    #7. Se debe generar una nueva columna llamada TIPO_HOGAR en funcion de la cant hab
    fila['TIPO_HOGAR']=clasificar_hogar_hab(fila['IX_TOT'])

    #8. Se debe generar una nueva columna llamada MATERIAL_TECHUMBRE
    fila['MATERIAL_TECHUMBRE']=clasificar_hogar_techo(fila['V4'])

    #9. Se debe generar una nueva columna llamada DENSIDAD_HOGAR
    fila['DENSIDAD_HOGAR']=clasificar_hogar_densidad_hab(fila['IX_TOT'],fila['IV2'])

    #10. Condiciones de habitabilidad
    fila['CONDICION_DE_HABITABILIDAD']=clasificar_hogar_habitabilidad(fila['IV6'],fila['IV7'],fila['IV8'],fila['IV9'],fila['IV10'],fila['IV11'],fila['MATERIAL_TECHUMBRE'],fila['IV3'])
    return fila
