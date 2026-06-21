def contar_envios(database, estado):
    cantidades = {'Standard Class': 0, 'First Class': 0, 'Second Class': 0, 'Same Day': 0}

    
    for clave in database:

        valores = database[clave]
        ship_mode = valores["Ship Mode"]
        state = valores["State"]

        if estado == state:
            cantidades[ship_mode] +=1
        
        
    return cantidades

