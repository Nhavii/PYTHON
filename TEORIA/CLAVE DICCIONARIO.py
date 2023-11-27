tutor={
    "nombre":"Carlos",
    "edad":27,
    "materias":["Python","PHP","JavaScript"]
}

print("nombre" in tutor) # Dara True or False si esta o no en el diccionario

if "nombre" in tutor:
    print("La clave existe.")
else:
    print("La clave no existe.")