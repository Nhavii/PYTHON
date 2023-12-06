import os   

archivo="C:/Users/Navi/Desktop/PROGRAMACION/EJERCICIOS/renombrado.txt"

if os.path.exists(archivo):
    print("El archivo existe.")
else:
    print("El archivo no existe.")