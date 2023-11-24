numero=input("Introduzca un numero: ")

try:
    numero=int(numero)
except:
    print("Ponga un valor valido.")
    exit()

contador=1

while contador<=12:
    #print(f"{numero} x {contador} = "+str(numero*contador))
    print(f"{numero} x {contador} = {numero*contador}")
    contador+=1
print(f"Tabla del {numero} hasta el 12")
    