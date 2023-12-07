def fibonacciRecursivo(n):
    if n<=0:
        return[]
    if n==1:
        return[0]
    if n==2:
        return[0,1]
    else:
        secuencia=fibonacciRecursivo(n-1)
        secuencia.append(secuencia[-1]+secuencia[-2])
        return secuencia

longitud=int(input("Introduzca de cuanto quiere la tula de fibonacci: "))

resultado=fibonacciRecursivo(longitud)

print(f"La secuencia es de longitud: {longitud}, es: {resultado}")
