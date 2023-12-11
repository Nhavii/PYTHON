class Alumno:
    def __init__(self,nombre,edad,notas):
        self.nombre=nombre
        self.edad=edad
        self.notas=notas

    def promedio(self):
        promedio=0
        for nota in self.notas:
            promedio=nota+promedio
        promedio=promedio/len(self.notas)
        if promedio>=5:
            print(f"Aprobado con un a nota de: {promedio}")
        else:
            print(f"Suspenso con nota de: {promedio}")
        
alumno1=Alumno("Manolo",25,[1,5,8,3,6,8,3])
alumno2=Alumno("Pepe",32,[4,7,3,6,7,10,1,8,7])

alumno1.promedio()
alumno2.promedio()
