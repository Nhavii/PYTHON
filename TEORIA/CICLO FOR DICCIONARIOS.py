frutas = {
"Fresa":"roja",
"Pera":"verde",
"Papaya":"naranja",
"Uva":"morada",
"Guayaba":"rosa"
}

#for valor in frutas:
#   print(f"{valor} es de color {frutas[valor]}")

for llaves,valor in frutas.items():
    print(f"{llaves} es de color {valor}")