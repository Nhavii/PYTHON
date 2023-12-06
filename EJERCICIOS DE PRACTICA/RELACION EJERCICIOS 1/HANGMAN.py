import random
palabras=["Fresa","Naranja","Mango","Pera"]

def elegirPalabra():
    return random.choice(palabras)

final=elegirPalabra()

def mostrarBarras(palabra):
    barra=""
    for i in palabra:
        barra=barra+"_"
    return barra

def mostrarLetra(letra,palabra,palabraBarras):
    barra=""
    for i in palabra:
        if letra==i:
            barra=barra+letra
        else:
            barra=barra+"_"
    return barra
        
def victoria(palabra):
    if palabra==final:
        print("Ganaste chupapollas.") 
    else:
        print("Perdiste chupapollas.") 

print(mostrarBarras(final))

while True:
    letra=input("Prueba con una letra: ")
    adivinar=mostrarLetra(letra,final)
    print(adivinar)