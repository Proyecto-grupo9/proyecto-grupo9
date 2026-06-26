import csv

def crear_diccionario_interno(fila : list[str])-> dict:
    '''
    Esta funcion recibe una fila (lista de strings), donde los strings
    representan los valores de la fila de un dataset y 
    devuelve una diccionario, donde las claves son los titulos de las columnas del dataset y 
    los valores el string de la fila que le corresponde a cada columna
    crear_diccionario_interno([]) == {}
    crear_diccionario_interno(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture",
    "Bookcases","261.96","2","0","41.9136","37.836111","-87.59"]) == 
    {"Ship Mode":"Second Class","Segment":"Consumer","City":"Henderson","State":"Kentucky",
    "Region":"South","Category":"Furniture","Sub-Category":"Bookcases","Sales":"261.96","Quantity":"2",
    "Profit":"41.9136","Latitude":"37.836111","Longitude":"-87.59"}
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
    '''
    Esta funcion recibe un archivo con extension csv y devuelve un
    dataset representado como una lista de diccionarios donde
    cada diccionario representa representan a cada fila del archivo csv
    leer_archivo(leer_archivo(open("ArchivoParaTesting.csv"))) == deberia 
    devolver una lista con los diccionarios correspondientes a las filas de "ArchivoParaTesting"
    '''
    filas = []

    next(data_set)

    for linea in data_set:
        valores = linea.strip().split(',')
        diccionario_interno = crear_diccionario_interno(valores)
        filas.append(diccionario_interno)
        
        

    return filas

