cantidad=input("Introduzca cauntos ordenadores compro: ")

try:
    cantidad=int(cantidad)
except:
    print("Ponga un valor valido.")
    exit()

if cantidad<5:
    total= cantidad*(700-(700*0.10))
elif 10>cantidad>=5:
    total= cantidad*(700-(700*0.20))
elif cantidad>=10:
    total= cantidad*(700-(700*0.40))

print(f"EL total es: {total}")

