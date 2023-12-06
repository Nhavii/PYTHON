import os       

directorioActual=os.getcwd()
archivos=os.listdir(directorioActual)

print(f"Estos son los archivos del directorio actual de este archivo: {archivos}")