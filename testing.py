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
#  TESTING FUNCIONES DEL ARCHIVO: "leer_archivo.py"
# -----------------------------------------------------------
def test_crear_diccionario_interno():
    assert crear_diccionario_interno([]) == {}
    assert crear_diccionario_interno(["Second Class","Consumer","United States","Henderson","Kentucky","42420","South","Furniture",
    "Bookcases","261.96","2","0","41.9136","37.836111","-87.59"]) == {"Ship Mode":"Second Class","Segment":"Consumer","City":"Henderson","State":"Kentucky",
    "Region":"South","Category":"Furniture","Sub-Category":"Bookcases","Sales":"261.96","Quantity":"2",
    "Profit":"41.9136","Latitude":"37.836111","Longitude":"-87.59"}

def test_leer_archivo():
    with open("ArchivoParaTesting.csv") as archivo:
        resultado = leer_archivo(archivo)

    assert resultado == [{"Ship Mode":"Second Class","Segment":"Consumer","City":"Henderson","State":"Kentucky",
    "Region":"South","Category":"Furniture","Sub-Category":"Bookcases","Sales":"261.96","Quantity":"2",
    "Profit":"41.9136","Latitude":"37.836111","Longitude":"-87.59"},
    {"Ship Mode":"Second Class","Segment":"Consumer","City":"Henderson","State":"Kentucky",
    "Region":"South","Category":"Furniture","Sub-Category":"Chairs","Sales":"731.94","Quantity":"3",
    "Profit":"219.582","Latitude":"37.836111","Longitude":"-87.59"},
    {"Ship Mode":"Second Class","Segment":"Corporate","City":"Los Angeles","State":"California",
    "Region":"West","Category":"Office Supplies","Sub-Category":"Labels","Sales":"14.62","Quantity":"2",
    "Profit":"6.8714","Latitude":"33.973093","Longitude":"-118.247896"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Fort Lauderdale","State":"Florida",
    "Region":"South","Category":"Furniture","Sub-Category":"Tables","Sales":"957.5775","Quantity":"5",
    "Profit":"-383.031","Latitude":"26.121561","Longitude":"-80.128778"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Fort Lauderdale","State":"Florida",
    "Region":"South","Category":"Office Supplies","Sub-Category":"Storage","Sales":"22.368","Quantity":"2",
    "Profit":"2.5164","Latitude":"26.121561","Longitude":"-80.128778"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Los Angeles","State":"California",
    "Region":"West","Category":"Furniture","Sub-Category":"Furnishings","Sales":"48.86","Quantity":"7",
    "Profit":"14.1694","Latitude":"33.973093","Longitude":"-118.247896"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Los Angeles","State":"California",
    "Region":"West","Category":"Office Supplies","Sub-Category":"Art","Sales":"7.28","Quantity":"4",
    "Profit":"1.9656","Latitude":"33.973093","Longitude":"-118.247896"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Los Angeles","State":"California",
    "Region":"West","Category":"Technology","Sub-Category":"Phones","Sales":"907.152","Quantity":"6",
    "Profit":"90.7152","Latitude":"33.973093","Longitude":"-118.247896"},
    {"Ship Mode":"Standard Class","Segment":"Consumer","City":"Los Angeles","State":"California",
    "Region":"West","Category":"Office Supplies","Sub-Category":"Binders","Sales":"18.504","Quantity":"3",
    "Profit":"5.7825","Latitude":"33.973093","Longitude":"-118.247896"}]
    


# -----------------------------------------------------------
#  TESTING FUNCIONES DEL ARCHIVO: "funciones_auxiliares.py"
# -----------------------------------------------------------
def test_lista_palabras():
    assert lista_palabras([],"City") == []
    assert lista_palabras(leer_archivo(open("ArchivoParaTesting.csv")),"City") == ["Henderson","Los Angeles","Fort Lauderdale"]
    assert lista_palabras(leer_archivo(open("ArchivoParaTesting.csv")),"State") == ["Kentucky","California","Florida"]

def test_cuenta_cantidades_enteras():
    assert cuenta_cantidades_enteras({},"State","Quantity") == {}
    assert cuenta_cantidades_enteras(dataset_prueba,"City","Quantity") == {"Henderson":5,"Los Angeles":22,"Fort Lauderdale":7}

def test_cuenta_cantidades_float():
    assert cuenta_cantidades_float({},"Ship Mode","Sales") == {}
    assert cuenta_cantidades_float(dataset_prueba,"Ship Mode","Sales") == {"Second Class": 1008.52,"Standard Class": 1961.7415}

def test_cuenta_cantidades_subcategorias():
    assert cuenta_cantidades_subcategorias({},"Furniture","Sub-Category","Quantity") == {}
    assert cuenta_cantidades_subcategorias(dataset_prueba,"Furniture","Sub-Category","Quantity") == {"Bookcases": 2,"Chairs": 3,"Tables": 5,"Furnishings": 7}


# -----------------------------------------------------------
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta1.py"
# -----------------------------------------------------------
def test_ciudades():
    assert ciudades([]) == []
    assert ciudades(dataset_prueba) == ["Henderson","Los Angeles","Fort Lauderdale"]

def test_ventas_ganancia():
    assert ventas_ganancias("Los Angeles",[]) == (0,0.0)
    assert ventas_ganancias("",leer_archivo(open("ArchivoParaTesting.csv"))) == (0,0.0)
    assert ventas_ganancias("Henderson",leer_archivo(open("ArchivoParaTesting.csv"))) == (5,261.4956)


# -----------------------------------------------------------
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta2.py"
# -----------------------------------------------------------
def test_estados_paquetes():
    assert estados_paquetes([]) == {}
    assert estados_paquetes(leer_archivo(open("ArchivoParaTesting.csv"))) == {"Kentucky":5,"California":22,"Florida":7}

def test_estado_que_mas_recibio():
    assert estado_que_mas_recibio({}) == ["",0]
    assert estado_que_mas_recibio({"Kentucky":5,"California":22,"Florida":7}) == ["California",22]
    assert estado_que_mas_recibio({"Kentucky":0,"California":0,"Florida":0}) == ["",0]


# -----------------------------------------------------------
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta3.py"
# -----------------------------------------------------------
def test_contar_envio():
    assert contar_envios([],"California") == {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}
    assert contar_envios(dataset_prueba,"") == {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}
    assert contar_envios(dataset_prueba,"California") == {'Standard Class': 4, 'First Class': 0, 'Second Class': 1, 'Same Day': 0}

def test_lista_estados_disponibles():
    assert lista_estados_disponibles([]) == []
    assert lista_estados_disponibles(dataset_prueba) == ["Kentucky","California","Florida"]

def test_lat_lon_estado():
    assert lat_lon_estado([],"California") == {}
    assert lat_lon_estado(dataset_prueba,"California") == {"lat":[33.973093],"lon":[-118.247896]}


# -----------------------------------------------------------
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta4.py"
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
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta5.py"
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
#  TESTING FUNCIONES DEL ARCHIVO: "resolucion_pregunta6.py"
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
    