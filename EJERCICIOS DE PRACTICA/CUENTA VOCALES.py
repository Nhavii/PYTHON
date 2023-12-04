vocales=["a","e","i","o","u"]

def contarVocales(texto):
    cuenta=0
    for i in texto:
        if i in vocales:
            cuenta+=1
    return cuenta   

texto=str(input("Pon la frase coño: "))
print(contarVocales(texto))

    



