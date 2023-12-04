def calculadora(numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="*":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    return resultado
    
numero1=int(input("Pon el numero 1: "))
signo=str(input("Que operacion sera; +, -, *, /: "))
numero2=int(input("Pon el numero 2: "))
print(calculadora(numero1,numero2,signo))