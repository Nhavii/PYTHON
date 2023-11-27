n1=input("Introduzca un numero: ")

try:
    n1=float(n1)
except:
    print("Ponga un valor valido.")

elevado = n1**3 if (n1%2)==0 else n1**2

print(f"el resultado es: {elevado}")