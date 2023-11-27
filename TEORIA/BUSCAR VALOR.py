frutas={
    "Peras":23,
    "Manzanas":50,
    "Sandias":7,
    "Melocotones":21,
    "Fresas":100,
    "Uvas":150
}
 # .capitalize() pone la primera letra en mayuscula
busqueda=input("Introduce una fruta: ")
busqueda=str(busqueda)
busqueda=busqueda.capitalize()

numero=frutas.get(busqueda,0)

print(f"Hay {numero} {busqueda} en el inventario.")