import random
import string

def generarContrasena(longitud):
    caracteres=string.ascii_letters + string.digits
    contrasena="".join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud=input("Introduzca cuantos caracteres quiere en la contrasena: ")
try:
    longitud=int(longitud)
except:
    print("Ponga un valor valido")
    exit()
nuevaContrasena=generarContrasena(longitud)
print(f"La nueva contrasena es: {nuevaContrasena}")