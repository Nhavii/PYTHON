edad=input("Introduzca su edad: ")

try:
    edad=int(edad)
except:
    print("Ponga una edad valida.")
    exit()


if edad>=18:
    print("Pringao eres mayor de edad.")
if edad<=18:
    print("Pringao eres menor de edad.")