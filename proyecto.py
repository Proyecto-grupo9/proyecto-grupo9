import csv

# Funcion para leer el archivo.

def leer_archivo():
    
    '''
    fila : list[str]
    la funcion toma el archivo con extension csv y lo representa como una lista de filas,
    cada fila es una lista de strings, donde cada elemento corresponde a una columna del data-set.
    '''
    data_base = open("SampleSuperstore_geo.csv")
    lista = []
    for fila in data_base:

        fila.append(fila.strip("\n").split(","))
        
        

    data_base.close()
    return lista



# Funciones resolucion pregunta 6

def cantidades_ventas_segment(list:list(list)):
    '''
    cantidades_ventas_segment: list -> tuple
    cantidad_ventas_consumer: Int
    cantidad_ventas_corporate: Int
    cantidad_ventas_homeoffice: Int

    Dada una lista de listas, devuelve las cantidades de ventas cada 
    segmento representadas en una tupla

    '''
    cantidad_ventas_consumer = 0
    cantidad_ventas_corporate = 0
    cantidad_ventas_homeoffice = 0
    '''
    Hacemos un bucle for para que, cada vez que encuentre en la columna 2 "Consumer",
    "Corporate" o "Home Office", aumente el valor de sus cantidades segun lo que diga
    la columna 11, lo cual es un string estrictamente numérico, por lo tanto, convertimos
    el string en un int.
    '''

    for l in list:
        if l[1] == "Consumer":
            cantidad_ventas_consumer += int(l[10])
        elif l[1] == "Corporate":
            cantidad_ventas_corporate += int(l[10])
        elif l[1] == "Home Office":
            cantidad_ventas_homeoffice += int(l[10])
    tuple =(cantidad_ventas_consumer, cantidad_ventas_corporate, cantidad_ventas_homeoffice)

    return tuple


# Funciones resolucion pregunta 3

def cuenta_first_class(fila:list)->int:
    '''
    una fila es una lista de strings : list[str]
    contador_first_class es un entero : int
    esta función dada una fila, retorna la cantidad de veces que aparece "First Class"
    ejemplos:
    cuenta_first_class(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture","Bookcases","261.96","2","0.0","41.9136","37.836111","-87.59"]) == 0
    '''
    contador_first_class = 0
    if fila[0] == "First Class":
        contador_first_class += 1
    return contador_first_class


def cuenta_second_class(fila:list)->int:
    '''
    una fila es una lista de strings : list[str]
    contador_second_class es un entero : int
    esta función dada una fila, retorna la cantidad de veces que aparece "Second Class"
    ejemplos:
    cuenta_second_class(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture","Bookcases","261.96","2","0.0","41.9136","37.836111","-87.59"]) == 1
    '''
    contador_second_class = 0
    if fila[0] == "Second Class":
        contador_second_class += 1
    return contador_second_class


def cuenta_standard_class(fila:list)->int:
    '''
    una fila es una lista de strings : list[str]
    contador_standard_class es un entero : int
    esta función dada una fila, retorna la cantidad de veces que aparece "standard_class"
    ejemplos:
    cuenta_standard_class(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture","Bookcases","261.96","2","0.0","41.9136","37.836111","-87.59"]) == 0
    '''
    contador_standard_class = 0
    if fila[0] == "Standard Class":
        contador_standard_class += 1
    return contador_standard_class


def cuenta_same_day(fila:list)->int:
    '''
    una fila es una lista de strings : list[str]
    contador_same_day es un entero : int
    esta función dada una fila, retorna la cantidad de veces que aparece "same_day"
    ejemplos:
    cuenta_same_day(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture","Bookcases","261.96","2","0.0","41.9136","37.836111","-87.59"]) == 0
    '''
    contador_same_day = 0
    if fila[0] == "Same Day":
        contador_same_day += 1
    return contador_same_day

def cantidades_envio_estado(lista:list, estado:str)-> tuple:
    '''
    Representamos el dataset como una lista de listas(filas), donde a
    cada fila del dataset la representamos como una lista.
    Represetamos los estados como strings.

    cantidad_first_class: int 
    cantidad_second_class: int
    cantidad_same_day: int
    cantidad_standard: int

    La función recibe un dataset y un estado, devuelve una tupla con 
    las cantidades de cada tipo de envio pedido por el estado.
    '''
    cantidad_first_class = 0
    cantidad_second_class = 0
    cantidad_same_day = 0
    cantidad_standard = 0

    for fila in lista:
        if estado == fila[4]:
            cantidad_first_class += cuenta_first_class(fila)
            cantidad_second_class += cuenta_second_class(fila)
            cantidad_same_day += cuenta_same_day(fila)
            cantidad_standard += cuenta_standard_class(fila)
    

    return (cantidad_first_class,cantidad_second_class,cantidad_standard,cantidad_same_day)