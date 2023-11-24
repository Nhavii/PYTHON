listaFrutas=["Fresa","Mango","Pera"]

diccionarioFrutas={
    "Papaya":"naranja",
    "Uva":"morada",
    "Guayaba":"rosa"
}

# Para Diccionarios

print(diccionarioFrutas)
diccionarioFrutas["Fresa"]="roja"
print(diccionarioFrutas)

# Metodo .append() ,es decir, listas 

print(listaFrutas)
listaFrutas.append("Limon")
print(listaFrutas)

# Metodo insert(lugar,valor)
print(listaFrutas)
listaFrutas.insert(1,"Limon")
print(listaFrutas)