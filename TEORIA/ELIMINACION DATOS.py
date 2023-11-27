listaFrutas=["Fresa","Mango","Pera","Fresa"]
listaFrutas1=["Fresa","Mango","Pera"]

diccionarioFrutas={
    "Papaya":"naranja",
    "Uva":"morada",
    "Guayaba":"rosa"
}

# Metodo .pop(lugar) para listas y .popitem(lugar y valor) para diccionarios
"""
print(listaFrutas)
listaFrutas.pop() #si esta vacio quita el ultimo
listaFrutas.pop(1)
print(listaFrutas)

print(listaFrutas1)
fruta=listaFrutas1.pop(1) #le damos a fruta el valor que quitamos de la lista
print(listaFrutas1)
print(fruta)


print(diccionarioFrutas)
diccionarioFrutas.popitem()
print(diccionarioFrutas)

print(diccionarioFrutas)
fruta=diccionarioFrutas.popitem()
print(diccionarioFrutas)
print(fruta)

# Metodo .remove(valor)
print(listaFrutas)
listaFrutas.remove("Fresa") #solo remueve el primero que concuerde con el valor
print(listaFrutas)
"""

# Metodo del

del diccionarioFrutas["Guayaba"]
print(diccionarioFrutas)

print(listaFrutas)
del listaFrutas[1:3]
print(listaFrutas)



