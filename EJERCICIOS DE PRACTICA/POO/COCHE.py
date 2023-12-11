class Coche:
    def __init__(self,marca,modelo,año,aceleracion):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.aceleracion=aceleracion
        self.velocidad=10

    def acelerar(self):
        self.velocidad=self.aceleracion+self.velocidad
        
    def frenar(self):
        f=self.velocidad-self.aceleracion
        if f<=0:
            f=0
        self.velocidad=f

    def __str__(self):
        return f"El coche de {self.marca} del modelo {self.modelo} del año {self.año} acelera a {self.aceleracion} y va a {self.velocidad} km/h."

coche1=Coche("Toyota","Panda",2020,4)
coche2=Coche("Honda","Nabo",2023,2)

print(coche1)
print(coche2)
