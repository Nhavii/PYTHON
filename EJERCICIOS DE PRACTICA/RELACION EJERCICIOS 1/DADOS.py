import random

cantidad=input("Cuantos dados de 6 caras quieres lanzar?: ")
cantidad=int(cantidad)

try:
    cantidad=int(cantidad)
except:
    print("Ponga un valor valido")
    exit()

for _ in range(cantidad):
    dados=random.randint(1,6)
    print(dados)

