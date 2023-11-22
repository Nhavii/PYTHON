genero=input("Ponga M para masculino y F para femenino: ")
edad=input("Ponga su edad: ")

try:
    genero=str(genero)
    edad=int(edad)
except:
    print("Ponga un valor valido.")
    exit()

if genero=="M":
    if edad>=60:
        print("Viejo, se puede jubilar")
    else:
        print("Joven, no se puede jubilar")
elif genero=="F":
     if edad>=60:
        print("Vieja, se puede jubilar")
     else:
        print("Joven, no se puede jubilar")
else:
    print("Ponga una opcion valida en el genero.")