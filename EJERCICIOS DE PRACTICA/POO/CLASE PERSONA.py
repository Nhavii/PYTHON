class Persona:
    def __init__(self,nombre,edad,direccion):
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion

persona1=Persona("Juan",25,"Calle Mamawebo 69")
persona2=Persona("Maria",69,"Calle Pinga 13")

print(f"Nombre: {persona1.nombre}, Edad: {persona1.edad}, Dirección: {persona1.direccion}.")
print(f"Nombre: {persona2.nombre}, Edad: {persona2.edad}, Dirección: {persona2.direccion}.")
