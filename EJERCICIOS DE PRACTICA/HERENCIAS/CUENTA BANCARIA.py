class CuentaBancaria:
    def __init__(self, saldoInicial=0):
        self.saldo = saldoInicial

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo -= monto

    def obtener_saldo(self):
        return self.saldo

class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldoInicial=0, comision=0.05):
        super().__init__(saldoInicial)
        self.comision=comision
    
    def aplicarComision(self):
        comisionAplicada=self.saldo*self.comision
        self.saldo-=comisionAplicada

class CuenataAhorro(CuentaBancaria):
    def __init__(self,saldoInicial=0,tasaInteres=0.03):
        super().__init__(saldoInicial)
        self.tasaInteres=tasaInteres

    def aplicarInteres(self):
        interesGenerado=self.saldo*self.tasaInteres
        self.saldo+=interesGenerado
