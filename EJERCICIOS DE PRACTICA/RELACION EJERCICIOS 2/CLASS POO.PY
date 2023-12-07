class Coche:
        
    def __init__(self,color,aceleracion,ruedas):
        self.color= color
        self.aceleracion=aceleracion
        self.ruedas=ruedas
        self.velocidad=10
        

    def acelera(self):
        self.velocidad= self.velocidad + self.aceleracion

    def frena(self):
        v=self.velocidad-self.aceleracion
        if v<0:
            v=0
        self.velocidad=v
    
    def __str__(self):
        return f"Mi coche es de color {self.color} y acelera a {self.aceleracion} y tiene esta velocidad:{self.velocidad} y tiene {self.ruedas} ruedas"

rayo=Coche("verde porro",100,5)
manolo=Coche("amarillo",210,3)
print(manolo)

manolo.color="naranja"
manolo.aceleracion=4
print(manolo)

    
   