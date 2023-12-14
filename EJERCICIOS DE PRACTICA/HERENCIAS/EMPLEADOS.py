class Empleado:
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario

class Gerente(Empleado):
    def calcularBono(self):
        return self.salario*0.20
    
class Desarrollador(Empleado):
    def calcularBonus(self):
        return "Seguro de salud y bono anual"
    
empleado1=Empleado("Pepe",50000)
gerente1=Gerente("Laura",70000)
desarrollador1=Desarrollador("Carlos",60000)

bonoGerente=gerente1.calcularBono()
bonusDesarrollador=desarrollador1.calcularBonus()

print(f"Nombre del empleado: {empleado1.nombre}, Salario: {empleado1.salario}")
print(f"Nombre del gerente: {gerente1.nombre}, Salario: {gerente1.salario}, Bonificación: {bonoGerente}")
print(f"Nombre del empleado: {empleado1.nombre}, Salario: {empleado1.salario}, Bonus: {bonusDesarrollador}")