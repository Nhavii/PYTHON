import random

def obtener_palabra():
    palabras = ["python", "programacion", "computadora", "desarrollo", "codigo"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_correctas):
    tablero = ""
    for letra in palabra:
        if letra in letras_correctas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_correctas = []
    intentos = 7

    print("¡Bienvenido al juego del ahorcado!")

    while intentos > 0:
        tablero = mostrar_tablero(palabra, letras_correctas)
        print(tablero)
        print("Tienes {} intentos restantes.".format(intentos))

        letra = input("Ingresa una letra: ").lower()

        if letra in palabra:
            letras_correctas.append(letra)
            if set(letras_correctas) == set(palabra):
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break
        else:
            print("La letra {} no está en la palabra. Pierdes un intento.".format(letra))
            intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra era {}.".format(palabra))

jugar_ahorcado()