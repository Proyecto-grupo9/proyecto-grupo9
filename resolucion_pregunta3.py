def contar_envios(database, estado):
    '''
    Estado: es un string que representa un Estado de USA.
    La función recibe un database y un Estado y devuelve las cantidades de cada tipo de envío que se hayan
    utilizado para transportar la mercadería al Estado seleccionado.
    Esta función se diseñó para mostrar las cantidades de cada tipo de envío a cada Estado. Es decir,
    muestra cuantos envíos se hicieron por Standar Class, cuantos por First Class, cuantos por Second
    Class y cuantos por Same Day.
    Ejemplos:
    test_contar_envios( ):
    test_contar_envios( ):
    test_contar_envios( ):
    '''
    cantidades = {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}

    
    for clave in database:

        valores = database[clave]
        ship_mode = valores["Ship Mode"]
        state = valores["State"]

        if estado == state:
            cantidades[ship_mode] +=1
        
        
    return cantidades

