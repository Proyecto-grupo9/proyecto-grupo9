from funciones_auxiliares import *

def contar_envios(database : list[dict], estado : str)->dict:
    '''
    Estado: es un string que representa un Estado de USA.
    La función recibe un database y un Estado y devuelve las cantidades de cada tipo de envío que se hayan
    utilizado para transportar la mercadería al Estado seleccionado.
    Esta función se diseñó para mostrar las cantidades de cada tipo de envío a cada Estado. Es decir,
    muestra cuantos envíos se hicieron por Standar Class, cuantos por First Class, cuantos por Second
    Class y cuantos por Same Day.
    Ejemplos:
    contar_envios([],"California") == {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}
    contar_envios(leer_archivo(open("ArchivoParaTesting.csv")),"") == 
    {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}
    contar_envios(leer_archivo(open("ArchivoParaTesting.csv")),"California") ==
    {'Standard Class': 4, 'First Class': 0, 'Second Class': 1, 'Same Day': 0}
    '''
    cantidades : dict = {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}

    
    for fila in database:

        ship_mode : str = fila["Ship Mode"]
        state : str = fila["State"]

        if estado == state:
            cantidades[ship_mode] +=1
        
        
    return cantidades

def lista_estados_disponibles(database : list[dict])->list[str]:
    '''
    La función recibe un database y devuelve que Estados están en el archivo.
    La función fue diseñada para obtener los Estados nombrados en la tabla de la 
    superstore.
    Ejemplos:
    lista_estados_disponibles([]) == []
    lista_estados_disponibles(leer_archivo(open("ArchivoParaTesting.csv"))) == ["Kentucky","California","Florida"]

    '''
    estados_disponibles : list[str] = lista_palabras(database,"State")
    return estados_disponibles

def lat_lon_estado(database : list[dict],estado : str)->dict:
    '''
    La función recibe un database y un Estado y devuelve las coordenadas de el mismo.
    Diseñamos esta función para saber las latitudes y longitudes de cada Estado
    Ejemplos:
    lat_lon_estado()
    lat_lon_estado()
    lat_lon_estado()
    '''
    coordenadas : dict = {}
    for fila in database:
        state : str = fila["State"]
        
        if state == estado:
            longitud : float = float(fila["Longitude"])
            latitud : float = float(fila["Latitude"])
            
            coordenadas["lat"] = [latitud]
            coordenadas["lon"] = [longitud]
            break

    return coordenadas

