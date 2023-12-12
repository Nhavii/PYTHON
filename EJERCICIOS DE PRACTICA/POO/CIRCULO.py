class Circulo:
    def __init__(self,radio,color):
        self.radio=float(radio)
        self.color=color
    
    def Area(self):
        area=3.14159*(self.radio**2)
        return area

    def Perimetro(self):
        perimetro=2*3.14159*self.radio
        return perimetro
    
circulo1=Circulo(4,"rojo")

print(f"El area es: {circulo1.Area()}")
print(f"El Perimetro es: {circulo1.Perimetro()}")