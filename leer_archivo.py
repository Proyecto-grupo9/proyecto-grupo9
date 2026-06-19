import csv

def leer_archivo()->list:
    '''
    data_set : str
    fila : list[str]
    filas : list[fila]
    La funcion toma el archivo con exstension csv, es decir el data-set y lo representa como una 
    lista de filas, es decir, como una lista de listas de strings, donde cada string de la fila 
    representa a una columna del data-set
    '''
    data_set = open("SampleSuperstore_geo.csv")
    filas = []
    for linea in data_set:
        filas.append(linea.strip("\n").split(","))

    data_set.close()
    return filas


