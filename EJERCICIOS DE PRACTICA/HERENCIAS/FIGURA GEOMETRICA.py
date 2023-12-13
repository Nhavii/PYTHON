class FiguraGeometrica:
    def area(self):
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return self.lado*self.lado
    
class Circulo(FiguraGeometrica):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return 3.14*self.radio**2
    
cuadrado1=Cuadrado(5)
circulo1=Circulo(3)

print(f"Area del cuadrado: {cuadrado1.area()}")
print(f"Area del circulo: {circulo1.area()}")
