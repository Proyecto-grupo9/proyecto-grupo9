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
    esta funci贸n dada una fila, retorna la cantidad de veces que aparece "Second Class"
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
    esta funci贸n dada una fila, retorna la cantidad de veces que aparece "same_day"
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
        if estado == estado:
            cantidad_first_class = cuenta_first_class(fila)
            cantidad_second_class = cuenta_second_class(fila)
            cantidad_same_day = cuenta_same_day(fila)
            cantidad_standard = cuenta_standard_class(fila)
    
        
    return (cantidad_first_class,cantidad_second_class,cantidad_standard,cantidad_same_day)
