#list crea una lista
lista =list([56,85,34,False,99,45,69,45,23,56,True])

#len cuenta la cantidad de elementos de una lista

cantidad_elementos = len (lista)

#append agrega un elemento a la lista
lista.append (65)

#insert agrega un elemento a la lista en el indice especificado
lista.insert(2,36) #primero declaramos el lugar

#extend agrega varios elementos a la lista
lista.extend([58,98]) #se agrega en formato de lista

#pop elimina un elemento de la lista, pide indice y devuelve valor
lista.pop(0) #el elemento -1 es el ultimo elemento

#remove remueve un elemento de una lista, pide valor
lista.remove(34)

#clear elimina todos los elementos de una lista
#lista.clear ()

#sort ordena una lista de forma ascendente a descendente, sin texto
lista.sort()
lista.sort(reverse=True) #ordena en reversa

#reverse invierte los elementos de una lista
lista.reverse() #si no usamos sort antes la revierte desordenada 

print(lista)

