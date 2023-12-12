class Libro:
    def __init__(self,título,autor,año,disponible):
        self.título=título
        self.autor=autor
        self.año=año
        self.disponible=disponible

    def mostrar(self):
        print(f"Título: {self.título}.")
        print(f"Autor: {self.autor}.")
        print(f"Año: {self.año}.")

    def disponibilidad(self):
        if self.disponible:
            print(f"El libro {self.título} está disponible.")
        else:
            print(f"El libro {self.título} no está disponible.")

libro1=Libro("Mamatorio","Mi Nabo Gordo",1969,"Disponible")

eleccion=""

while eleccion!=0:
    eleccion=int(input("Que quiere hacer; 0 para salir, 1 para mostrar informacion, 2 ver disponibilidad: "))
    if eleccion==0:
        print("ahi te mates, no vuelvas")
    elif eleccion==1:
        libro1.mostrar()
    elif eleccion==2:
        libro1.disponibilidad()
    else:
        print("comete un nabo")