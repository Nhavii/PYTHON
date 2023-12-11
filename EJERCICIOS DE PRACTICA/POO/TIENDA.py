class Tienda:
    def __init__(self,nombre,productos):
        self.nombre=nombre
        self.productos=productos
    

    def añadir(self):
        producto=str(input("¿Qué producto desea añadir?: "))
        self.productos.append(producto)
        return f"El producto {producto} ha sido añadido a la tienda {self.nombre}"        

    def mostrar(self):
        print(f"Esta es nuestra lista de productos: {self.productos}")

    def buscar(self):
        busqueda = input("¿Qué producto desea buscar?: ").lower()
        coincidencias = []
        for producto in self.productos:
            if busqueda in producto.lower():
                coincidencias.append(producto)    
        if coincidencias:
            print(f"Productos encontrados con el nombre '{busqueda}':")
            for producto in coincidencias:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{busqueda}'.")

tienda1=Tienda("NabOS",["XXXL","XXL","XL","L"])

eleccion=""

while eleccion!=0:
    eleccion=int(input("Que quiere hacer; 0 para salir, 1 para añadir, 2 mostrar, 3 buscar: "))
    if eleccion==0:
        print("ahi te mates, no vuelvas")
    elif eleccion==1:
        tienda1.añadir()
    elif eleccion==2:
        tienda1.mostrar()
    elif eleccion==3:
        tienda1.buscar()
    else:
        print("comete un nabo")