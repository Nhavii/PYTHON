nombre1=input("Introduzca su nombre: ")
edad1=input("Introduzca su edad: ")
nombre2=input("Introduzca su nombre: ")
edad2=input("Introduzca su edad: ")

try:
    edad1=int(edad1)
    edad2=int(edad2)
    nombre1=str(nombre1)
    nombre2=str(nombre2)
except:
    print("Ponga valores validos.")
    exit()

mayor = print(f"El mayor es: {nombre1}") if edad1>edad2 else print(f"El mayor es: {nombre2}")

