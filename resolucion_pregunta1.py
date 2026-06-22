
def ventas_ganancias(ciudad:str,data_base:dict)->tuple:
    '''
    
    '''
    contador_quantity : int = 0
    ganancias : int = 0
    for fila in data_base:
        if ciudad == data_base["City"]:
            contador_quantity += int(data_base["Quantity"])
            ganancia += float(data_base["Profit"])
    return (contador_quantity,ganancias)

