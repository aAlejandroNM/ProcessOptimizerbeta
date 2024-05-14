from manejoexcepciones import *
def crear_producto(datos):
    datos = dict(datos)
    producto = {}
    producto["id"] = generador_id(datos)
    producto["nombre"] = input("Ingrese el nuevo producto: ")
    producto["caracteristicas"] = input("Ingrese las características del producto: ")
    
    # Manejo de excepciones para asegurar que el precio sea un número válido
    while True:
        try:
            producto["precio"] = float(input("¿Cuánto cuesta el producto? "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido para el precio del producto.")

    datos["productos"].append(producto)
    print("¡Producto agregado con éxito!")
    return datos

def eliminar_producto(datos):
    datos = dict(datos)

    print("Estos son los productos disponibles")

    for i in range(len(datos["productos"])):
        print(datos["productos"][i]["id"], end=": ")
        print(datos["productos"][i]["nombre"])

    ID_ingresado =int(input("Ingrese el id del producto: "))
    for i in range(len(datos["productos"])):
        if datos["productos"][i]["id"] == ID_ingresado:
                datos["productos"].pop(i)
                print("producto eliminado!")
                actualizador_id(datos)
                return datos
        print("No se encontro el producto !!")
    return datos

def modificar_producto(datos):
    datos = dict(datos)

    print("Estos son los actuales productos")

    for i in range(len(datos["productos"])):
        print(datos["productos"][i]["id"], end=": ")
        print(datos["productos"][i]["nombre"])

    id_soli = int(input("Ingrese el id del producto que quiere modificar: "))
    for i in range(len(datos["productos"])):
        if datos["productos"][i]["id"] == id_soli:
            datos["productos"][i]["nombre"] = input("Ingrese el nuevo nombre: ")
            datos["productos"][i]["caracteristicas"] = input("Ingrese las características del producto: ")
            
            # Manejo de excepciones para asegurar que el precio sea un número válido
            while True:
                try:
                    datos["productos"][i]["precio"] = float(input("¿Cuánto cuesta el producto? "))
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para el precio del producto.")
                    
            print("Producto modificado con éxito!")
            return datos
            
    print("No se encontró el producto :(")
    return datos

def generador_id(datos):
    return len(datos["productos"]) + 1

def actualizador_id(datos):
    for i in range(len(datos["productos"])):
        datos["productos"][i]["id"] = i + 1
    return datos