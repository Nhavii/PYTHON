frutas=["Naranja","Fresa","Mango","Pera"]
frutas1=["Naranja","Fresa","Mango","Pera"]
numeros=(7,9,1,3,0,2,8,6,4,5)

# .sort() ordena listas alfabeticamente o ascendente, solo funciona sis solo hay texto o solo numeros.

"""
frutas.sort()
print(frutas)
"""
# Con reverse=True lo haces de la Z-A o descendiente.
"""
frutas1.sort(reverse=True)
print(frutas1)
"""
# .reverse() da la vuelta a la lista
"""
frutas.reverse()
print(frutas)
"""

# .sorted() Si devuelve la lista. Solo texto o solo numero.

listaNumeros=sorted(numeros,reverse=True)
print(listaNumeros)
print(numeros)