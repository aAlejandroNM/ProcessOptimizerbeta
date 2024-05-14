from manejoexcepciones import *
def crear_servicio(datos):
    datos = dict(datos)
    servicio = {}
    servicio["id"] = generador_id(datos)
    servicio["nombre"] = input("Ingrese el nuevo servicio: ")
    servicio["caracteristicas"] = input("Ingrese las características del servicio: ")
    
    while True:
        try:
            servicio["precio"] = float(input("¿Cuánto cuesta el servicio? "))
            break
        except ValueError as e:
            manejar_excepciones(e)
            print("Error: Por favor, ingrese un número válido para el precio del servicio.")

    datos["servicios"].append(servicio)

    print("Servicio agregado con éxito!")
    return datos

def eliminar_servicios(datos):
    datos = dict(datos)

    print("Estos son los Servicios disponibles")

    for i in range(len(datos["servicios"])):
        print(datos["servicios"][i]["id"], end=": ")
        print(datos["servicios"][i]["nombre"])

    doc_ingresado =int(input("Ingrese el id del servicio: "))
    for i in range(len(datos["servicios"])):
        if datos["servicios"][i]["id"] == doc_ingresado:
                datos["servicios"].pop(i)
                print("Servicio eliminado!")
                actualizador_id(datos)
                return datos
    print("No se encontro el servicio !!")
    return datos

def modificar_servicios(datos):
    datos = dict(datos)

    print("Estos son los actuales servicios")
    #mostrar servicios
    for i in range(len(datos["servicios"])):
        print(datos["servicios"][i]["id"], end=": ")
        print(datos["servicios"][i]["nombre"])

    id_soli =int(input("Ingrese el id del servicio que quiere editar: "))
    for i in range(len(datos["servicios"])):
        if datos["servicios"][i]["id"] == id_soli:
                datos["servicios"][i]["nombre"]=input("Ingrese el nuevo nombre: ")
                datos["servicios"][i]["caracteristicas"]=input("Ingrese las caracteristicas del servicio")
                while True:
                    try:
                        datos["servicios"][i]["precio"] = int(input("¿Cuánto cuesta el servicio? "))
                        break
                    except ValueError as e:
                        manejar_excepciones(e)
                        print("Error: Por favor, ingrese un numero válido para el precio del servicio.")

                print("Servicio modificado con éxito!")
                return datos         
    print("No se encontró el servicio :(")
    return datos


def generador_id(datos):
    return len(datos["servicios"]) + 1

def actualizador_id(datos):
    for i in range(len(datos["servicios"])):
        datos["servicios"][i]["id"] = i + 1
    return datos


        