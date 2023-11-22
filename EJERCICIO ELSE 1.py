nllantas=input("Escriba cuantas llantas compro: ")

try:
    nllantas=int(nllantas)
except:
    print("Por favor escriba una cantidad valido.")
    exit()

if nllantas>=5:
    total= nllantas*700
else:
    total= nllantas*800
    
print(f"Su total es: {total}")
