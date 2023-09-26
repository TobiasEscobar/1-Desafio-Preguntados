from datos import lista

def guardar_en_sub_listas(lista_preguntas:list):
    sub_listas = []
    for diccionario in lista_preguntas:
        pregunta = diccionario['pregunta']
        opcion_a = diccionario['a']
        opcion_b = diccionario['b']
        opcion_c = diccionario['c']
        respuesta_correcta = diccionario['correcta']
        
        sub_lista = [pregunta, opcion_a, opcion_b, opcion_c, respuesta_correcta]
        
        sub_listas.append(sub_lista)

    return sub_listas