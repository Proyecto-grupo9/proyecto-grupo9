#Importamos el codigo principal
from proyecto import *


def main():

    estado_x = input("Ingrese un estado: \n")
    print(cantidades_envio_estado(leer_archivo(),estado_x))

    return 0