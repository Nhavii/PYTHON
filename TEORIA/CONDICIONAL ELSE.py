n1=input("Escriba el numero 1: ")
n2=input("Escriba el numero 2: ")

try:
    n1=float(n1)
    n2=float(n2)
except:
    print("Pon numeros validos.")
    exit()

if n1>n2:
    print("El primer numero es mayor que el segundo.")
else:
    print("El primer numero es menor que el segundo.")


