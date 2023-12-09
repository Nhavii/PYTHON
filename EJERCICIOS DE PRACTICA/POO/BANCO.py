class CuentaBancaria:
    def __init__(self,cuenta,saldo):
        self.cuenta=cuenta
        self.saldo=saldo
    
    def depositar(self):
        pobre=float(input("Introduzca la cantidad a ingresar: "))
        self.saldo=self.saldo+pobre
        print(f"Se ha depositado con exito los {pobre}€.")

    def retirar(self):
        rico=float(input("Introduzca la cantidad a retirar: "))
        if rico<self.saldo:
            self.saldo=self.saldo-rico
            print(f"Se ha retirado con exito los {rico}€.")
        else:
            print("Pobre de mierda no puedes sacar mas.")            

    def mostrar(self):
        print(f"Su saldo es de {self.saldo}€.")

persona1=CuentaBancaria("7849874874874387",10)

eleccion=""

while eleccion!=0:
    eleccion=int(input("Que quiere hacer; 0 para salir, 1 para mostrar saldo, 2 meter dinero, 3 sacar dinero: "))
    if eleccion==0:
        print("ahi te mates, no vuelvas")
    elif eleccion==1:
        persona1.mostrar()
    elif eleccion==2:
        persona1.depositar()
    elif eleccion==3:
        persona1.retirar()
    else:
        print("comete un nabo")