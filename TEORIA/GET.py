tutor={
    "nombre":"Carlos",
    "edad":27,
    "materias":["Python","PHP","JavaScript"]
}

# Normal
print(tutor["nombre"])

# .get() si ponemos una clave que no exista devuelve none.
# si no existe la llave, poniendo una coma podemos decir qu nos devuelva lo que queramos
print(tutor.get("edad"))
print(tutor.get("edades","La clave o llave no existe."))
