# Asignacion

lista=[1,2,3,4,5,6,7]
lista1=lista



lista1[2]=100  # Lo del corchete es la posicion el 0.
"""
print(lista1)
print(lista)  # Lo que cambios en lista1 tambien lo hace en lista.
"""

# .copy() copaimos la lista, por lo que no se modifica la otra

listaA=[1,2,3,4,5,6,7]
listaB=listaA.copy()

listaB[0]=90
print(listaB)
print(listaA)