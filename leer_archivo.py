import csv

def crear_diccionario_interno(fila : list[str])-> dict:
    '''
    Esta funcion recibe una fila (lista de strings), donde los strings
    representan los valores de la fila de un dataset y 
    devuelve una diccionario, donde las claves son los titulos de las columnas del dataset y 
    los valores el string de la fila que le corresponde a cada columna
    crear_diccionario_interno() ==
    '''

    indice = 0

    columnas = ["Ship Mode","Segment","Country","City","State","Postal Code",
    "Region","Category","Sub-Category","Sales","Quantity","Discount","Profit","Latitude","Longitude"]

    diccionaro_interno = {}

    for valor in fila:
        if (indice != 2) and (indice != 5) and (indice != 11):
            diccionaro_interno[columnas[indice]] = fila[indice]
        indice+=1
    return diccionaro_interno

        


def leer_archivo(data_set):
    filas = []

    next(data_set)

    for linea in data_set:
        valores = linea.strip().split(',')
        diccionario_interno = crear_diccionario_interno(valores)
        filas.append(diccionario_interno)
        
        

    return filas

