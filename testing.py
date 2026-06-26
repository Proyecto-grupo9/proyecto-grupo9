from leer_archivo import *
from resolucion_pregunta1 import *
from resolucion_pregunta2 import *
from resolucion_pregunta3 import *
from resolucion_pregunta4 import *
from resolucion_pregunta5 import *
from resolucion_pregunta6 import *

# Abrimos el archivo "ArchivoParaTesting.csv" y lo guardamos en una variable para usarlo en los distintos testings:

archivo_prueba = open("ArchivoParaTesting.csv")

dataset_prueba = leer_archivo(archivo_prueba)

archivo_prueba.close()

# -----------------------------------------------------------
# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta1.py"
# -----------------------------------------------------------
def test_ciudades():
    assert ciudades([]) == []
    assert ciudades(dataset_prueba) == ["Henderson","Los Angeles","Fort Lauderdale"]

def test_ventas_ganancia():
    assert ventas_ganancias("Los Angeles",[]) == (0,0.0)
    assert ventas_ganancias("",leer_archivo(open("ArchivoParaTesting.csv"))) == (0,0.0)
    assert ventas_ganancias("Henderson",leer_archivo(open("ArchivoParaTesting.csv"))) == (5,261.4956)


# -----------------------------------------------------------
# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta2.py"
# -----------------------------------------------------------
def test_estados_paquetes():
    assert estados_paquetes([]) == {}
    assert estados_paquetes(leer_archivo(open("ArchivoParaTesting.csv"))) == {"Kentucky":5,"California":22,"Florida":7}

def test_estado_que_mas_recibio():
    assert estado_que_mas_recibio({}) == ["",0]
    assert estado_que_mas_recibio({"Kentucky":5,"California":22,"Florida":7}) == ["California",22]
    assert estado_que_mas_recibio({"Kentucky":0,"California":0,"Florida":0}) == ["",0]

# -----------------------------------------------------------
# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta4.py"
# -----------------------------------------------------------
def test_diccionario_ciudad():
    assert diccionario_ciudad([]) == {}
    assert diccionario_ciudad(dataset_prueba) == {"Henderson":993.9,"Los Angeles":996.416,"Fort Lauderdale":979.9455}

def test_mayor_sales():
    assert mayor_sales({}) == ("",0)
    assert mayor_sales({"Henderson":0,"Los Angeles":0,"Fort Lauderdale":0}) == ("",0)
    assert mayor_sales({"Henderson":993.9,"Los Angeles":996.416,"Fort Lauderdale":979.9455}) == ("Los Angeles",996.416)

def test_ganancias_region():
    ganancias_region([]) == {}
    ganancias_region(dataset_prueba) == {"South":-119.019,"West":119.5041}


# -----------------------------------------------------------
# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta5.py"
# -----------------------------------------------------------
def test_subcategoria_mas_vendida():
    assert subcategoria_mas_vendida({}) == {"":0}
    assert subcategoria_mas_vendida({"Bookcases":0,"Chairs":321,"Tables":12}) == {"Chairs":321}
    assert subcategoria_mas_vendida({"Bookcases":0,"Chairs":0,"Tables":0}) == {"":0}

def test_contador_subcategoria_furniture():
    assert contador_subcategoria_furniture([]) == {"":0}
    assert contador_subcategoria_furniture(dataset_prueba) == {"Furnishings":7}

def test_contador_subcategoria_technology():
    assert contador_subcategoria_technology([]) == {"":0}
    assert contador_subcategoria_technology(dataset_prueba) == {"Phones":6}

def test_contador_subcategoria_officesupplies():
    assert contador_subcategoria_officesupplies([]) == {"":0}
    assert contador_subcategoria_officesupplies(dataset_prueba) == {"Art":4}

def test_mayor_subcategoria():
    assert mayor_subcategoria("Furniture",dataset_prueba) == "La subcategoria mas vendida es: Furnishings y la cantidad de ventas es: 7"
    assert mayor_subcategoria("Technology",dataset_prueba) == "La subcategoria mas vendida es: Phones y la cantidad de ventas es: 6"
    assert mayor_subcategoria("Office Supplies",dataset_prueba) == "La subcategoria mas vendida es: Art y la cantidad de ventas es: 4"
    assert mayor_subcategoria("",dataset_prueba) == ""



# -----------------------------------------------------------
# TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta6.py"
# -----------------------------------------------------------
def test_cuenta_segments():
    assert cuenta_segments([]) == {}
    assert cuenta_segments(dataset_prueba) == {"Consumer":32, "Corporate": 2}

def test_division_para_porcentaje():   
    assert division_para_porcentaje(12,0) == 0
    assert division_para_porcentaje(12,4) == 300
    assert division_para_porcentaje(4,13) == 31
    assert division_para_porcentaje(4,7) == 57

def test_calcula_porcentaje():
    assert calcula_porcentaje({}) == []
    assert calcula_porcentaje({"Consumer":0,"Corporate":0,"Home Office":0}) == [0,0,0]
    assert calcula_porcentaje({"Consumer":3,"Corporate":0,"Home Office":0}) == [100,0,0]
    assert calcula_porcentaje({"Consumer":3,"Corporate":0,"Home Office":1}) == [75,0,25]
    assert calcula_porcentaje({"Consumer":32,"Corporate":2,"Home Office":0}) == [94,6,0]
    assert calcula_porcentaje({"Consumer":3,"Corporate":6,"Home Office":1}) == [30,60,10]


def test_segment_y_cantidad():
    assert segment_y_cantidad({}) == []
    assert segment_y_cantidad({'Consumer': 19521, 'Corporate': 11608, 'Home Office': 6744})==["Consumer (19521)","Corporate (11608)","Home Office (6744)"]
    assert segment_y_cantidad(cuenta_segments(dataset_prueba)) == ["Consumer (32)","Corporate (2)"]
    