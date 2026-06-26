from funciones_auxiliares import *

def estados_paquetes(database : list[dict])->dict:
    '''
    Esta funcion recibe un database, y devuelve un diccionario, donde la clave es un string (que representa a los estados) y
    el valor es la cantidad de paquetes que recibió cada estado.
    estados_paquetes([]) == {}
    estados_paquetes(leer_archivo(open("ArchivoParaTesting.csv"))) == {"Kentucky":5,"California":22,"Florida":7}
    '''
    cantidades : dict = cuenta_cantidades_enteras(database, "State","Quantity")
    return cantidades

def estado_que_mas_recibio(cantidades_estados : dict)->list:
    '''
    Esta funcion recibe un diccionario, donde la clave es un string (que representa a los estados) y
    el valor es la cantidad de paquetes que recibió cada estado y devuelve una lista, donde estado es el estado que mas paquetes recibio y 
    valor es la cantidad de paquetes recibidos.
    La funcion calcula cual es el estado que mas paquetes recibió.
    estado_que_mas_recibio({}) == ["",0]
    estado_que_mas_recibio({"Kentucky":5,"California":22,"Florida":7}) == ["California",22]
    estado_que_mas_recibio({"Kentucky":0,"California":0,"Florida":0}) == ["",0]
    '''
    estado : str = ""
    valor : int = 0
    for clave in cantidades_estados:
        if cantidades_estados[clave] > valor:
            valor = cantidades_estados[clave]
            estado = clave
    return [estado, valor]

