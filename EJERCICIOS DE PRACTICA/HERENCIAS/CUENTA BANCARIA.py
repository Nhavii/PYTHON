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

class CuentaAhorro(CuentaBancaria):
    def __init__(self,cuenta,saldo,mantenimiento):
        super().__init__(cuenta,saldo)
        self.mantenimiento=mantenimiento

class CuentaCorriente(CuentaBancaria):
    def __init__(self,cuenta,saldo,comision):
        super().__init__(cuenta,saldo)
        self.comision=comision
