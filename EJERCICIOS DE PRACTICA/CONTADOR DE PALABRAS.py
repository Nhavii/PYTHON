frase=input("Introduzca la frase para contar las palabras: ")

try:
    frase=str(frase)
except:
    print("Ponga unos valores validos.")
    exit()

cantidadPalabras=frase.split()

palabras=len(cantidadPalabras)

print(f"Hay {palabras} palabras en esa frase.")

