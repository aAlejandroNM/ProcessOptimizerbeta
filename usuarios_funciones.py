from manejoexcepciones import *
def crear_usuarios(datos):
    datos = dict(datos)
    usuario = {}

    usuario["nombre"] = input("Ingrese el nombre: ")
    
    documento = ""
    while len(documento) != 10:
        try:
            documento = input("Ingrese el documento (debe tener 10 caracteres): ")
            if len(documento) != 10:
                raise ValueError("El documento debe tener exactamente 10 caracteres.")
        except ValueError as ve:
            print(f"Error: {ve}")
    
    usuario["documento"] = documento
    
    usuario["tipo_cliente"] = "Nuevo"
    usuario["telefono"] = input("Ingrese su número telefónico: ")
    usuario["direccion"] = input("Ingrese su dirección de residencia: ")

    try:
        opcion_estudiante = int(input("Ingrese 1 si el cliente es estudiante o 2 de lo contrario: "))
        if opcion_estudiante not in [1, 2]:
            raise ValueError("Ingrese 1 o 2.")
        usuario["estudiante"] = opcion_estudiante == 1
    except ValueError as ve:
        print(f"Error: {ve}. Se asumirá que el cliente no es estudiante.")
        usuario["estudiante"] = False

    try:
        opcion_videojuegos = int(input("Ingrese 1 si el cliente juega videojuegos de forma competitiva o 2 de lo contrario: "))
        if opcion_videojuegos not in [1, 2]:
            raise ValueError("Ingrese 1 o 2.")
        usuario["videojuegos"] = opcion_videojuegos == 1
    except ValueError as ve:
        print(f"Error: {ve}. Se asumirá que el cliente no juega videojuegos de forma competitiva.")
        usuario["videojuegos"] = False

    try:
        usuario["cantidad_gente"] = int(input("¿Con cuánta gente vive el cliente? "))
    except ValueError as ve:
        print(f"Error: {ve}. Se asumirá que el cliente vive solo.")
        usuario["cantidad_gente"] = 1

    usuario["consultas"] = input()
    usuario["reclamaciones"] = ""
    usuario["sugerencias"] = ""
    usuario["cantidad_compras"] = 0
    usuario["sus_servicios"] = []
    usuario["productos"] = []

    datos["usuarios"].append(usuario)

    print("Cliente registrado con éxito!")

    return datos

def eliminar_usuarios(datos):
    datos = dict(datos)

    doc_ingresado =input("Ingrese el documento del cliente: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == doc_ingresado:
                datos["usuarios"].pop(i)
                print("Cliente eliminado!")
                return datos
        print("Participante no existe")
    return datos

def modificar_clientes(datos):
    datos = dict(datos)

    print("Estos son los actuales clientes")
    # Mostrar clientes actuales
    for i in range(len(datos["usuarios"])):
        print(datos["usuarios"][i]["documento"], end=": ")
        print(datos["usuarios"][i]["nombre"])

    documento = input("Ingrese el documento del cliente que quiere modificar: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"][i]["nombre"] = input("Ingrese el nuevo nombre: ")
            datos["usuarios"][i]["telefono"] = input("Ingrese el nuevo teléfono del cliente: ")
            datos["usuarios"][i]["direccion"] = input("Ingrese la nueva dirección del cliente: ")
            try:
                opc_estudiante = int(input("Ingrese 1 si el cliente es estudiante o 2 de lo contrario: "))
                if opc_estudiante not in [1, 2]:
                    raise ValueError("Ingrese 1 o 2.")
                datos["usuarios"][i]["estudiante"] = opc_estudiante == 1
            except ValueError as ve:
                print(f"Error: {ve}. Se asumirá que el cliente no es estudiante.")
                datos["usuarios"][i]["estudiante"] = False
            
            try:
                opc_videojuegos = int(input("Ingrese 1 si el cliente juega videojuegos de forma competitiva o 2 de lo contrario: "))
                if opc_videojuegos not in [1, 2]:
                    raise ValueError("Ingrese 1 o 2.")
                datos["usuarios"][i]["videojuegos"] = opc_videojuegos == 1
            except ValueError as ve:
                print(f"Error: {ve}. Se asumirá que el cliente no juega videojuegos de forma competitiva.")
                datos["usuarios"][i]["videojuegos"] = False
            
            try:
                cantidad_personas = int(input("Ingrese con cuántas personas vive el cliente: "))
                datos["usuarios"][i]["cantidad_gente"] = cantidad_personas
            except ValueError as ve:
                print(f"Error: {ve}. Se asumirá que el cliente vive solo.")
                datos["usuarios"][i]["cantidad_gente"] = 1

            print("Cliente modificado con éxito!")
            return datos

    print("No se encontró el cliente :(")
    return datos

def crear_consulta(datos):
    
    doc_ingresado=input("Ingrese el Documento de identidad de quien hizo la consulta: ")
    
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == doc_ingresado:
            datos["usuarios"][i]["consultas"]=input("ingrese la consulta del usuario: ")
            print('Consulta guardada con exito !!!')
            return datos
    print("No se encontro ese usuario")
    return datos

def crear_reclamacion(datos):
    
    doc_ingresado=input("Ingrese el Documento de identidad de quien hizo el reclamo: ")
    
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == doc_ingresado:
            datos["usuarios"][i]["reclamaciones"]=input("ingrese la reclamacion del usuario: ")
            print('Reclamo guardado con exito !!!')
            return datos
    print("No se encontro ese usuario")
    return datos



def crear_sugerencia(datos):
    doc_ingresado=input("Ingrese el Documento de identidad de quien hizo el reclamo: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == doc_ingresado:
            datos["usuarios"][i]["sugerencias"]=input("ingrese la sugerencia del usuario: ")
            print('Sugerencia guardada con exito !!!')
            return datos
    print("No se encontro ese usuario")
    return datos
        
            

     