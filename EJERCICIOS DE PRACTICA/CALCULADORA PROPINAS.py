precio=input("Introduzca el costo total: ")

try:
    precio=float(precio)
except:
    print("Ponga unos valores validos.")
    exit()

tip=precio*0.2

total=precio+tip

print(f"Su total incluyendo un 20% de propina seria {total} Euros, su propina seria de {tip}.")