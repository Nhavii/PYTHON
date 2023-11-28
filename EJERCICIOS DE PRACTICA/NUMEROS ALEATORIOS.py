import random

cantidad=input("Introduzca cuantos numeros aleatorios del 1 al 100 quiere ver: ")
cantidad=int(cantidad)

try:
    cantidad=int(cantidad)
except:
    print("Ponga un valor valido")
    exit()

for _ in range(cantidad):
    numerosAleatorios=random.randint(1,100)
    print(numerosAleatorios)



