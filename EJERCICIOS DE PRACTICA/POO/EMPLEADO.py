class Empleado:
    def __init__(self,nombre,salario,departamento):
        self.nombre=nombre
        self.salario=salario
        self.departamento=departamento

    def mostrar(self):
        print(f"Nombre: {self.nombre}.")
        print(f"Nomina mensual: {self.salario}.")
        print(f"Departamento: {self.departamento}.")
    
    def salarioAnual(self):
        anual=self.salario*12
        return anual

empleado1=Empleado("Malotitox",1200,"Departamento de Testeo de Pingas")

empleado1.mostrar()
print(f"Su salario Anual es de aproximadamente: {empleado1.salarioAnual()}")

