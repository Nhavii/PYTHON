import random
opciones=["Piedra","Papel","Tijeras"]

jugador= input("Elige entre Piedra, Papel o Tijeras: ")
jugador=str(jugador.capitalize())

pc=random.choice(opciones)


if jugador==pc:
        print(f"Payaso habeis empatado, la pc saco {pc}")
elif jugador=="Piedra":
    if pc=="Papel":
                print(f"Perdiste, la pc saco {pc} y tu {jugador}")
    else:
                print(f"Ganaste, la pc saco {pc} y tu {jugador}")
elif jugador=="Papel": 
    if pc=="Tijeras":
                print(f"Perdiste, la pc saco {pc} y tu {jugador}")
    else:
                print(f"Ganaste, la pc saco {pc} y tu {jugador}")
elif jugador=="Tijeras": 
        if pc=="Piedra":
                print(f"Perdiste, la pc saco {pc} y tu {jugador}")
        else:
                print(f"Ganaste, la pc saco {pc} y tu {jugador}")
else:
    print("Error- Opcion no valida.")

                





