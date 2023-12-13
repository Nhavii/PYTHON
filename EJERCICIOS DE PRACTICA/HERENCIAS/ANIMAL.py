class Animal:
    def hacerSonido(self):
        print("Hacer sonido genérico.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def hacerSonido(self):
        print("Guau")

class Gato(Animal):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def hacerSonido(self):
        print("Miau")

perro1=Perro("Bobi","Labrador")
gato1=Gato("Kiko","Atigrado")

print(f"El nombre del perro es: {perro1.nombre}")
print(f"La raza del perro es: {perro1.raza}")
print(f"El nombre del gato es: {gato1.nombre}")
print(f"La raza del gato es: {gato1.raza}")

perro1.hacerSonido()
gato1.hacerSonido()