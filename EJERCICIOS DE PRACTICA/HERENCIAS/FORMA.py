class Forma:
    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Forma):
    def __init__(self,longitud,ancho):
        self.longitud=longitud
        self.ancho=ancho
    
    def area(self):
        return self.lado*self.ancho
    
    def perimetro(self):
        return 2*self.lado+2*self.ancho
    
class Triangulo(Forma):
    def __init__(self,l1,l2,l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def area(self):
      semi=(self.lado1+self.lado2+self.lado3)/2
      return [semi*(semi-self.lado1)*(semi-self.lado2)*(semi-self.lado3)]

    def perimetro(self):
        return self.lado1+self.lado2+self.lado3
    



    

