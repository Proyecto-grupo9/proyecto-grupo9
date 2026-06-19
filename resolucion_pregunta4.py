#¿Cuales fueron las ganancias de cada región y cuál fue la ciudad que realizó más compras?

def ganancias_por_region(archivo:list[list[str]])-> dict:
    '''
    ganancias_region: dict

    Creamos un diccionario donde las claves seran las regiones, y sus valores seran las respectivas
    ganancias de cada region.


    Dado una lista de listas de strings (Data-base), checkeamos por fila si la region encontrada en la
    columna correspondiente a las regiones está añadida al diccionario, en dicho caso, aumentamos el 
    valor de la region con respecto a la fila profit, que podemos convertirlo en float al siempre ser 
    un string numerico. En caso de que no este en el diccionario, simplemente añadimos la region con 
    el valor correspondiente.
    '''
    ganancias_region = {}

    for fila in archivo:
        
        region = fila[6]

        profit = float(fila[12])

        if region not in ganancias_region:

            ganancias_region[region] = profit

        else: ganancias_region[region] += profit

    return ganancias_region




def ciudades_ventas(archivo:list[list[str]])-> dict:
    '''
    ciudades: dict

    Creamos un diccionario donde las claves seran el nombre de la ciudad (columna City),
    y el valor sera las ventas (columna Sales).

    Recorremos todas las filas, en cada fila que encuentra una ciudad, verifica primero que 
    no esté ya incluida en el diccionario, si no esta incluida, la agrega dandole el valor 
    de la columa Sales, si la ciudad ya esta incluida, simplemente modifica el valor 
    con respecto a la columa Sales.
    
    '''
    ciudades = {}

    for fila in archivo:
        columna_ciudad = fila[3]
        columna_sales = float(fila[9])
        if fila[3] not in ciudades:
            ciudades[columna_ciudad] = columna_sales
        else: ciudades[columna_ciudad] += columna_sales

    return ciudades
