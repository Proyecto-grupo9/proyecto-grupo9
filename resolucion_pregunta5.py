def mayor_el_lista(lista:list)->int:
    '''
    Dada una lista de numeros enteros, retorna el mayor elemento
    '''
    mayor = 0
    for elemento in list:
        if elemento > mayor:
            mayor = elemento
    return mayor


def contador_subcategoria_furniture(data_base:dict)-> int:
    '''

    '''
    contador_bookcases : int = 0
    contador_chairs : int = 0
    contador_tables : int = 0
    contador_furnishings : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Bookcases":
            contador_bookcases += fila["Quantity"]
        elif fila["Sub-Category"] == "Chairs":
            contador_chairs += fila["Quantity"]
        elif fila["Sub-Category"] == "Tables":
            contador_tables += fila["Quantity"]
        elif fila["Sub-Category"] == "Furnishings":
            contador_furnishings += fila["Quantity"]
    lista_de_contadores = [contador_bookcases,contador_chairs,contador_tables,contador_furnishings]


    return mayor_el_lista(lista_de_contadores)

def def contador_subcategoria_technology(data_base:dict)-> int:
    '''
    
    '''
    contador_phones : int = 0
    contador_accessories : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Phones":
            contador_phones += fila["Quantity"]
        elif fila["Sub-Category"] == "Accessories":
            contador_accessories += fila["Quantity"]
    
    lista_de_contadores = [contador_phones,contador_accessories]

    return mayor_el_lista(lista_de_contadores)


def contador_subcategoria_officesupplies(data_base:dict)-> int:
    '''

    '''
    contador_storage : int = 0
    contador_art : int = 0
    contador_labels : int = 0
    contador_binders : int = 0
    contador_appliances : int = 0
    contador_paper : int = 0
    contador_envelopes : int = 0
    contador_fasteners : int = 0
    for fila in data_base:
        if fila["Sub-Category"] == "Storage":
            contador_storage += fila["Quantity"]
        elif fila["Sub-Category"] == "Art":
            contador_art += fila["Quantity"]
        elif fila["Sub-Category"] == "Labels":
            contador_labels += fila["Quantity"]
        elif fila["Sub-Category"] == "Binders":
            contador_binders += fila["Quantity"]
        elif fila["Sub-Category"] == "Appliances":
            contador_appliances += fila["Quantity"]
        elif fila["Sub-Category"] == "Paper":
            contador_paper += fila["Quantity"]
        elif fila["Sub-Category"] == "Envelopes":
            contador_envelopes += fila["Quantity"]
        elif fila["Sub-Category"] == "Fasteners":
            contador_fasteners += fila["Quantity"]

    lista_de_contadores = [contador_storage,contador_art,contador_labels,contador_binders,contador_appliances,contador_paper,contador_envelopes,contador_fasteners]

    return mayor_el_lista(lista_de_contadores)


def mayor_subcategoria(categoria:str,data_base:dict):
    '''
    falta modificar para que diga que subcategoria es la mas vendida,
    ahora devuelve solo la cantidad
    '''
    retorno = 0
    if categoria == "Furniture":
        retorno = contador_subcategoria_furniture(data_base)
    
    elif categoria == "Office Supplies":
        retorno = contador_subcategoria_officesupplies(data_base)
    
    elif categoria == "Technology":
        retorno = contador_subcategoria_technology(data_base)

    return retorno