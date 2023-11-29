peso=input("Introduzca su peso: ")
altura=input("Introduzca su altura: ")

try:
    peso=float(peso)
    altura=float(altura)
except:
    print("Ponga un valor valido")
    exit()

imc=peso/(altura**2)
print(f"Tu IMC es {imc}")

if imc<18.5:
    print("Tu peso es muy bajo, deberias subir de peso un poco.")
elif 24.9>imc>18.5:
    print("Tu peso es normal.")
elif 25>imc>29.9:
    print("Tu peso es un poco por encima de lo normal.")
else:
    print("Tienes sobrepeso, adelgaza.")
