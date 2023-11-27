import random
opciones=["Piedra","Papel","Tijeras"]

jugador= input("Elige entre Piedra, Papel o Tijeras: ")
jugador=jugador.capitalize

pc=random.choice(opciones)

if jugador=="Piedra":
    if pc==jugador:
        print(f"Pringao empatasteis, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Papel":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Tijeras":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Piedra":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Tijeras":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Papel":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Piera":
        print(f"Ganaste, la pc saco {pc}")
if jugador=="Papel":
    if pc==jugador:
        print(f"Pringao empatasteis, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Papel":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Tijeras":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Piedra":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Tijeras":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Papel":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Piera":
        print(f"Ganaste, la pc saco {pc}")
if jugador=="Tijeras":
    if pc==jugador:
        print(f"Pringao empatasteis, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Papel":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Piedra" and jugador=="Tijeras":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Piedra":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Papel" and jugador=="Tijeras":
        print(f"Ganaste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Papel":
        print(f"Perdiste, la pc saco {pc}")
    elif pc=="Tijeras" and jugador=="Piera":
        print(f"Ganaste, la pc saco {pc}")
else:
    print("Ponga una opcion valida.")
    exit()






