class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

class Coche(Vehiculo):
    def __init__(self,marca,modelo,puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def numeroPuertas(self):
        return self.puertas
    
class Moto(Vehiculo):
    def __init__(self,marca,modelo,cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def cilindradas(self):
        return self.cilindrada
    
coche1=Coche("Toyota","Corolla",4)
moto1=Moto("Honda","CBR500R","500cc")

print(f"Coche: {coche1.marca}, {coche1.modelo} - Número de puertas: {coche1.puertas}" )    
print(f"Moto: {moto1.marca}, {moto1.modelo} - Cilindrada: {moto1.cilindrada}" )