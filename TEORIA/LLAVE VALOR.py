tutor1={
    "nombre":"Carlos",
    "edad":27,
    "materias":["Python","PHP","JavaScript"]
}

lista=list(tutor1.keys())
tupla=tuple(tutor1.values())

for llaves in tutor1.keys():
    print(llaves)
for valor in tutor1.values():
    print(valor)