import os

archivo=os.stat("C:/Users/Navi/Desktop/PROGRAMACION/EJERCICIOS/renombrado.txt")
print(archivo.st_size)
print(archivo.st_mode)
