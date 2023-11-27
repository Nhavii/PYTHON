"""
break:detiene o rompe la ejecucion del ciclo
continue:salta a la siguiente iteracion del ciclo
"""

numero=1

"""
while numero<=10:
    print(numero)
    if numero==7:
        break
    numero+=1
"""

"""
while numero<=10:
    if numero==5:
        numero+=1
        continue     
    print(numero)
    numero+=1
"""


lista_frutas=["Fresa","Naranja","Mango","Pera"]

"""
for fruta in lista_frutas:
    if fruta=="Mango":
        break
    print(fruta)
"""

for fruta in lista_frutas:
    if fruta=="Mango":
        continue
    print(fruta)





