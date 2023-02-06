diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs" : 10000
}

#Keys() devuelve las claves, tambien nos sirve para iterar, sino lo encuentra devielve error
claves = diccionario.keys()

#get() devuelve el valor de una clave, sino encuentra devuelve none
valor_de_nombre=diccionario.get("nombre")

#clear() elimina todos los elementos
#diccionario.clear()

#pop() elimina un elemento o los que quieras (,)
diccionario.pop("apellido")

#items() obteniendo un elemento dict_items iterable
diccionario_iterable=diccionario.items()

print(diccionario_iterable)