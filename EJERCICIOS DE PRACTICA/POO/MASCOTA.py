class Mascota:
    def __init__(self,nombre,especie,edad):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}.")
        print(f"Especie: {self.especie}.")
        print(f"Edad: {self.edad}.")

    def perrogato(self):
        if self.especie.lower()=="gato":
            print(f"Su mascota es un gato.")
        else:
            print(f"Su mascota es un perro.")

mascota1=Mascota("Kiko","Gato",6)
mascota2=Mascota("Nabo","Perro",3)

mascota1.mostrar()
mascota1.perrogato()
mascota2.mostrar()
mascota2.perrogato()
