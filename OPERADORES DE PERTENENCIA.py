"""
in   Sirve para ver si un valor esta en la lista o tupla (true que si,false que no)
"""
frutas=["Fresa","Naranja","Mango","Pera"]

frutas1=("Fresa","Naranja","Mango","Pera")

texto="Hola Mundo"

print("Fresa" in frutas)
print("Naranja" in frutas1)
print("Uva" in frutas)
print("Hola" in texto)
print("Adios" in texto)

"""
not in   Sirve para ver si un valor no esta en la lista o tupla (true que no,false que si)
"""
print("Fresa" not in frutas)
print("Naranja" not in frutas1)
print("Uva" not in frutas)
print("Hola" not in texto)
print("Adios" not in texto)