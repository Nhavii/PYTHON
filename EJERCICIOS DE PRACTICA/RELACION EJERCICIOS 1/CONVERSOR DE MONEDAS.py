euros=input("Introduzca cuantos euros para pasar a Dolares: ")

try:
    euros=float(euros)
except:
    print("Ponga unos valores validos.")
    exit()

dolares=euros*1.10

print(f"Serian {dolares} Dolares")