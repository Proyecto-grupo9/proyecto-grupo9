#Importamos el dataset
import leer_archivo

#Importamos los archivos de la resolucion de la pregunta 6
import cantidades_ventas_segment

#Importamos los archivos de la resolucion de la pregunta 3
import resolucion_pregunta3


def main()
    #Resolucion pregunta 6
    print(cantidades_ventas_segment(leer_archivo()))
    #Resolucion pregunta 3
    estado_x = input("Ingrese un estado de USA: \n")
    print(cantidades_envio_estado(leer_archivo(), estado_x))



    return 0

if __name__ == "__main__":
    main()
