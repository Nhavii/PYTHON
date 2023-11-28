tareas=[]

def agregarTarea():
    tarea=input("Introduzca la tarea para agregar: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def eliminarTarea():
    if len(tareas)==0:
        print("La lista esta vacia.")
    else:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea}")
        indice=int(input("Introduzca el numero de la tarea para eliminar: "))-1
        if indice>=0 and indice<len(tareas):
            eliminada=tareas.pop(indice)
            print(f"la tarea {eliminada} ha sido eliminada.")
        else:
            print("El numero ingresado no es valido.")

def mostrarTareas():
    if len(tareas)==0:
        print("La lista esta vacia.")
    else:
        print("Lista de tareas: ")
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea}")

while True:
    print("Que desea hacer: ")
    print("1. Agregar Tarea.")
    print("2. Eliminar Tarea.")
    print("3. Mostrar Tareas.")
    print("4. Salir.")

    opcion=input("Introduzca que opcion quiere realizar: ")

    if opcion=="1":
        agregarTarea()
    elif opcion=="2":
        eliminarTarea()
    elif opcion=="3":
        mostrarTareas()
    elif opcion=="4":
        break
    else:
        print("Ponga una opcion valida.")

    
    


