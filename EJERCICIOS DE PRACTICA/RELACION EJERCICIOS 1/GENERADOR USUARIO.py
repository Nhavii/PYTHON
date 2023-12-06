import random

def generar_nombre_usuario(nombre, apellido):
    num_aleatorio = str(random.randint(1, 100))
    nombre_usuario = nombre.lower() + apellido.lower() + num_aleatorio
    return nombre_usuario

nombre =input("Introduzca su nombre: ")
apellido =input("Introduzca su apellido: ") 

nombre_usuario_generado = generar_nombre_usuario(nombre, apellido)
print("Nombre de usuario generado:", nombre_usuario_generado)