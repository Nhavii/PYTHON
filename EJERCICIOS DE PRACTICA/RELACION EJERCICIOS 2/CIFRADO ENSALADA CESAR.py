def cifrarTexto(texto,clave):
    mensajeCifrado=""
    for letra in texto:
        if letra.isalpha():
            mayuscula=letra.isupper()
            letra=letra.upper()
            codigo=ord(letra)-65
            letraCifrada=chr((codigo+clave)%26+65)
            if not mayuscula:
                letraCifrada=letraCifrada.lower()
            mensajeCifrado+=letraCifrada
        else:
            mensajeCifrado+=letra
    return mensajeCifrado

def descifrarTexto(mensajeCifrado,clave):
    return cifrarTexto(mensajeCifrado,-clave)

texto=str(input("Introduzca  el texto a cifrar: "))
clave=int(input("Ponga el mierda de numero: "))

mensajeCifrado=cifrarTexto(texto,clave)
print(f"Mensaje cifrado: {mensajeCifrado}")

mensajeDescifrado=descifrarTexto(mensajeCifrado,clave)
print(f"Mensaje descifrado: {mensajeDescifrado}")
