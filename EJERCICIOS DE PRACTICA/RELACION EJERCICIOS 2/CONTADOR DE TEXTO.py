def analizaTexto(texto):
    palabras=texto.split(" ")
    nPalabras=len(palabras)
    
    nCaracteres=len(texto)
    
    nOracion=len(texto.split("."))-1+len(texto.split("?"))-1+len(texto.split("!"))-1

    
    print("Estadisticas del texto: ")
    print(f"-Numero de palabras: {nPalabras}")
    print(f"-Numero de caracteres: {nCaracteres}")
    print(f"-Numero de oraciones: {nOracion}")

textoUsuario=str(input("Introduzca el texto a analizar: "))


analizaTexto(textoUsuario)



