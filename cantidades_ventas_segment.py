


def cantidades_ventas_segment(list:list(list)):
    '''
    cantidades_ventas_segment: list -> tuple
    cantidad_ventas_consumer: Int
    cantidad_ventas_corporate: Int
    cantidad_ventas_homeoffice: Int

    Dada una lista de listas, devuelve las cantidades de ventas cada 
    segmento representadas en una tupla

    '''
    cantidad_ventas_consumer = 0
    cantidad_ventas_corporate = 0
    cantidad_ventas_homeoffice = 0

    for l in list:
        if l[1] == "Consumer":
            cantidad_ventas_consumer += int(l[10])
        elif l[1] == "Corporate":
            cantidad_ventas_corporate += int(l[10])
        elif l[1] == "Home Office":
            cantidad_ventas_homeoffice += int(l[10])
    tuple =(cantidad_ventas_consumer, cantidad_ventas_corporate, cantidad_ventas_homeoffice)

    return tuple









    




