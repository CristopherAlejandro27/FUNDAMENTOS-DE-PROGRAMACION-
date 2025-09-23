#lista de alumnos.
lista = ["Juan","Ivan","Adrian","Jair" ]
print (lista)
#Añade un elemento al final de la lista.
print(lista[2])
#Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se ínsertará.
lista.append ("Alexa")
print (lista)
lista.insert (1,"Javier")
print (lista)

lista.remove("Juan")
#Elimina el elemento de la posición indicada en la lista y lo devuelve.
lista.pop(1)
