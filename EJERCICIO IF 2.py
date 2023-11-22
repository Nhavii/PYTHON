total=input("Escriba el total de la compra: ")

try:
    total=float(total)
except:
    print("Por favor introduzca un total valido.")
    exit()

if total>=100:
    total=total-(total*0.20)
    print(f"Su total seria: {total}$")