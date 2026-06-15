#Importamos el codigo principal
import proyecto.py


def main():
    #Resolucion pregunta 6
    print(cantidades_ventas_segment(leer_archivo()))
    #Resolucion pregunta 3
    estado_x = input("Ingrese un estado de USA: \n")
    print(cantidades_envio_estado(leer_archivo(), estado_x))



    return 0

if __name__ == "__main__":
    main()
