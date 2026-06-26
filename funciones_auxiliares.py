def lista_palabras(database : list[dict],clave : str)-> list[str]:
    '''
    Esta funcion recibe un dataset, representado como una lista de diccionarios
    que representan a cada fila del dataset, y un string que representa a la clave de la columna del dataset que se busca listar
    y devuelve una lista de strings que representa a todas las ciudades que hay en el dataset
    Ejemplos;
    lista_palabras([],"City") == []
    lista_palabras(leer_archivo(open("ArchivoParaTesting.csv")),"City") == ["Henderson","Los Angeles","Fort Lauderdale"]
    lista_palabras(leer_archivo(open("ArchivoParaTesting.csv")),"State") == ["Kentucky","California","Florida"]
    '''
    palabras : list[str] = []

    for fila in database:
        palabra = fila[clave]
        if palabra not in palabras:
            palabras.append(palabra)

    return palabras



def cuenta_cantidades_enteras(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y dos strings, el primero, clave1, 
    representa al titulo de una columna del dataset,
    el segundo, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    cuenta_cantidades_enteras({},"State","Quantity") == {}
    cuenta_cantidades_enteras(leer_archivo(open("ArchivoParaTesting.csv")),"City","Quantity") == {"Henderson":5,"Los Angeles":22,"Fort Lauderdale":7}
    '''
    cantidades = {}

    for fila in database:
        palabra : str = fila[clave1]
        cantidad : int = int(fila[clave2])

        if palabra not in cantidades:
            cantidades[palabra] = cantidad
        else:
            cantidades[palabra] += cantidad
            
    return cantidades

def cuenta_cantidades_float(database : list[dict],clave1 : str, clave2 : str)->dict:
    '''
    Esta funcion recibe un database, y dos strings, el primero, clave1, 
    representa al titulo de una columna del dataset,
    el segundo, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    cuenta_cantidades_float({},"Ship Mode","Sales") == {}
    cuenta_cantidades_float(leer_archivo(open("ArchivoParaTesting.csv")),"Ship Mode","Sales") == {"Second Class": 1008.52,"Standard Class": 1961.7415}
    '''
    cantidades = {}

    for fila in database:
        palabra : str = fila[clave1]
        cantidad : float = round(float(fila[clave2]),4)

        if palabra not in cantidades:
            cantidades[palabra] = cantidad
        else:
            cantidades[palabra] += cantidad
            cantidades[palabra] = round(cantidades[palabra],4)
            
    return cantidades

def cuenta_cantidades_subcategorias(database : list[dict],categoria : str, clave1 : str, clave2 : str) -> dict:
    '''
    Esta funcion recibe un database, y tres strings, el primero, categoria, representa a una Categoria del database
    el segundo, clave1, representa al titulo de una columna del dataset (una subcategoria en este caso),
    el tercero, clave2, es un string numerable (entero) que representa
    a la columna del dataset a la cual se le suman las cantidades
    y devuelve un diccionario, donde la clave es un string (que representa a la clave1) y
    el valor es la cantidad de clave2 que le corresponde a la clave1
    cuenta_cantidades_subcategorias({},"Furniture","Sub-Category","Quantity") == {}
    cuenta_cantidades_subcategorias(leer_archivo(open("ArchivoParaTesting.csv")),"Furniture","Sub-Category","Quantity") == {"Bookcases": 2,"Chairs": 3,"Tables": 5,"Furnishings": 7}
    '''

    cantidades : dict = {}

    for fila in database:

        if categoria == fila["Category"]:

            palabra : str = fila[clave1]
            cantidad : int = int(fila[clave2])

            if palabra not in cantidades:
                cantidades[palabra] = cantidad
            else:
                cantidades[palabra] += cantidad

    return cantidades