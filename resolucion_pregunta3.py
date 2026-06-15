import leer_archivo

def cantidades_envio_estado(lista:list, estado:str)-> tuple:
    '''
    '''
    cantidad_first_class = 0
    cantidad_second_class = 0
    cantidad_same_day = 0
    cantidad_standard = 0


    for fila in lista:
        if fila[4] == estado:
            if fila[0] == "First Class":
                cantidad_first_class += 1
            elif fila[0] == "Second Class":
                cantidad_second_class += 1
            elif fila[0] == "Same Day":
                cantidad_same_day += 1
            elif fila[0] == "Standard Class":
                cantidad_standard +=1
    return (cantidad_first_class,cantidad_second_class,cantidad_standard,cantidad_same_day)

            