n1=input("Introduce el numero 1: ")

try:
    n1=int(n1)
except:
    print("Introduzca un numero entero")
    exit()

n2=input("Introduce el numero 2: ")

try:
    n2=float(n2)
except:
    print("Introduzca un numero decimal o flotante")
    exit()

"""
int-cambia la variable de texto a numero entero
float-cambia la variable de texto a numero decimal
try-prueba si se cumplen las condiciones de las variables
except-si da error o una excepcion a la prueba hace algo que digas  
"""


