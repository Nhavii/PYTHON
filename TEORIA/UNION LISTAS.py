lista1=[1,2,3]
lista2=[4,5,6,7]
listaFrutas=["Fresa","Mango","Pera"]

# Con Simbolo +

listaUnidas=lista1+listaFrutas+lista2

# Con mSimbolo *

lista3=lista1*7 #lista1*=3
print(lista3)

lista4=lista1+listaFrutas*3
print(lista4)

# Metodo .extend()

lista2.extend(listaFrutas)
lista2.extend(lista1)
print(lista2)