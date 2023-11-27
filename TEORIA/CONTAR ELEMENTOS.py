listaFrutas=["Fresa","Naranja","Mango","Pera"]
tuplaFrutas=("Sandia","Melocoton","Uva")
texto="Hola Mundo"

tutor={
    "nombre":"Carlos",
    "edad":27,
    "materias":["Python","PHP","JavaScript"]
}

# len(lista,tupla,string, diccionario) cuenta el numero de elemetos.

print(len(listaFrutas))
print(len(tuplaFrutas))
print(len(texto))
print(len(tutor))

# .count(elemento, valor) cuenta las veces que hay x elemento o letras, no sirve para diccionarios

print(listaFrutas.count("Fresa"))
print(tuplaFrutas.count("Fresa"))
print(texto.count("o"))