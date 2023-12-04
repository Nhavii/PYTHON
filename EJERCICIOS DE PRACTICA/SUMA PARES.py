def sumaPares (cum):
    par=0
    for i in range(1,cum+1):
       if i%2==0:
           par=i+par
    return par
        
manolo=int(input("Pon un numero parguela: "))
print(sumaPares(manolo))

           
           
