"""
codigo si se cumple if condicion else codigo si no se cumple
"""
n1=input("Escriba el numero 1: ")
n2=input("Escriba el numero 2: ")

try:
    n1=float(n1)
    n2=float(n2)
except:
    print("Pon numeros validos.")
    exit()

print("Resultado true") if n1>n2 else print("Resultado false")