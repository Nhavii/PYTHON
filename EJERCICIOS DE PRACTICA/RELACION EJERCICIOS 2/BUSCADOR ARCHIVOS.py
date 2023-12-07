import os      

def busquedaPorNombre(ruta, nombre):
    resultados=[]
    for rutaActual, carpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if nombre in archivo:
                resultados.append(os.path.join(rutaActual,archivo))
    return resultados

def busquedaPorExtension(ruta, extension):
    resultados = []
    for rutaActual, carpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(extension):
                resultados.append(os.path.join(rutaActual, archivo))
    return resultados

carpeta = "C:/Users/Navi/Desktop/PROGRAMACION/CARPETA EJEMPLO"
nombreABuscar = "calvo"
extensionABuscar = ".txt"

porNombre=busquedaPorNombre(carpeta,nombreABuscar)
porExtension=busquedaPorExtension(carpeta,extensionABuscar)

print("Archivos por nombre encontrados: ")
for archivo in porNombre:
    print(archivo)

print("Archivos por extensiones encontrados: ")
for archivo in porExtension:
    print(archivo)