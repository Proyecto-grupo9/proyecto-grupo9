#¿Cuales fueron las ganancias de cada región y cuál fue la ciudad que realizó más compras?

from funciones_auxiliares import *

def diccionario_ciudad(dataset : list[dict])->dict:
    '''
    Esta funcion recibe un dataset, y devuelve un diccionario, donde las claves son strings (que representan a las ciudades) y
    los valores son float (que representa a las ventas).
    diccionario_ciudad([]) == {}
    diccionario_ciudad(leer_archivo(open("ArchivoParaTesting.csv"))) == {"Henderson":993.9,"Los Angeles":996.416,"Fort Lauderdale":979.9455}
    '''
    
    ciudades : dict = cuenta_cantidades_float(dataset,"City","Sales")

    return ciudades

def mayor_sales(diccionario : list[dict])->tuple:
    '''
    Esta funcion recibe un diccionario, donde las claves son str (que representan a las ciudades) y los valores son
    valores numericos, float o int(que representan a las ventas) y devuelve una tupla donde el primer valor es la ciudad
    y el segundo es la cantidad de ventas.
    esta funcion determina la ciudad con la mayor cantidad de ventas.
    mayor_sales({}) == ("",0)
    mayor_sales({"Henderson":0,"Los Angeles":0,"Fort Lauderdale":0}) == ("",0)
    mayor_sales({"Henderson":993.9,"Los Angeles":996.416,"Fort Lauderdale":979.9455}) == ("Los Angeles",996.416)
    '''
    ventas = 0
    mayor_ciudad = ""
    for city in diccionario:
        if diccionario[city] > ventas:
            ventas = diccionario[city]
            mayor_ciudad : str = city
    return (mayor_ciudad,ventas)

def ganancias_region(dataset: list[dict])-> dict:
    '''
    Esta funcion recibe un dataset y devuelve un diccionario, donde las claves son str (que representan a las regiones) y
    los valores son float (que representan a las ganancias de cada region).
    ganancias_region([]) == {}
    ganancias_region(leer_archivo(open("ArchivoParaTesting.csv)))) == {"South":-119.019,"West":119.5041}
    '''
    ganancias : dict = cuenta_cantidades_float(dataset,"Region","Profit")

    return ganancias
