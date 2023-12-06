import random

def adivina_el_numero(intentos):
    numero_aleatorio = random.randint(1, 100)
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    for intento_actual in range(intentos):
        print("Tienes", intentos - intento_actual, "intentos restantes.")
        intento = int(input("Introduce tu suposición: "))

        if intento < numero_aleatorio:
            print("Más alto...")
        elif intento > numero_aleatorio:
            print("Más bajo...")
        else:
            print("¡Felicidades! ¡Adivinaste el número!")
            return

    print("¡Se acabaron los intentos! El número era", numero_aleatorio)

adivina_el_numero(5)




    
    

