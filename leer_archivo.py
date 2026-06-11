import csv


def leer_archivo():
    
    '''
    filas : list[str]
    la funcion toma el archivo con extension csv y lo representa como una lista de filas
    cada fila es una lista de strings, donde cada elemento corresponde a una columna del data-set
    '''
    data_base = open("SampleSuperstore_geo.csv")
    lista = []
    for linea in data_base:

        lista.append(linea.strip("\n").split(","))
        
        

    data_base.close()
    return lista


leer_archivo()




