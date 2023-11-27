dia=input("Introduzca un numero entre el 1 y el 7: ")

try:
    dia=int(dia)
except:
    print("Ponga un valor valido.")
    exit()

if dia==1:
    print("Es Lunes, mierda.")
elif dia==2:
    print("Es martes")
elif dia==3:
    print("Es miercoles")
elif dia==4:
    print("Es jueves")
elif dia==5:
    print("Es viernes")
elif dia==6:
    print("Es sabado")
elif dia==7:
    print("Es domingo")
else:
    print("lee mejor, pone entre 1 y 7 solo.")
    exit()
    

