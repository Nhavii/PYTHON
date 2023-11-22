n1=input("Esciba la primera nota: ")
n2=input("Esciba la segunda nota: ")
n3=input("Esciba la tercera nota: ")

try:
    n1=float(n1)
    n2=float(n2)
    n3=float(n3)
except:
    print("Por favor ponga valores validos.")
    exit()

media=(n1+n2+n3)/3

if media>=7.0:
    print(f"Felicidades, tu nota es: {media}")
else:
    print(f"Buen intento, tu nota es: {media}")
