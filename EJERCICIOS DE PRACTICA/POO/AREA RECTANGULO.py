class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho

    def area(self):
        area=self.largo*self.ancho
        return str(area)
    
    def perimetro(self):
        perimetro=(self.largo*2)+(self.ancho*2)
        return str(perimetro)

rectangulo1=Rectangulo(20,10)
rectangulo2=Rectangulo(15,8)

print(f"El area del 1 es: {rectangulo1.area()}")
print(f"El perimetro del 1 es: {rectangulo1.perimetro()}")
print(f"El area del 2 es: {rectangulo2.area()}")
print(f"El perimetro del 2 es: {rectangulo2.perimetro()}")