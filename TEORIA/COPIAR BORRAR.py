listaFrutas=["Fresa","Naranja","Mango","Pera"]

tutor={
    "nombre":"Carlos",
    "edad":27,
    "materias":["Python","PHP","JavaScript"]
}

# .copy() nos permite copiar listas y diccionarios

nuevaLista=listaFrutas.copy()  # nuevaLista=list(listaFrutas)

nuevoDiccionario=tutor.copy()  # nuevoDiccionario=dict(tutor)

# .clear() nos permite vaciar una lista o diccionario

listaFrutas.clear()
print(listaFrutas)

tutor.clear()
print(tutor)

