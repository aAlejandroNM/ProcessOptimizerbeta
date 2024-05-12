def crear_usuarios(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["telefono"]=input("Ingrese su numero telefonico: ")
    usuario["direccion"]=input("Ingrese su direccion de residencia: ")
    print("Ingrese 1 si el cliente es estudiante o 2 de lo contrario")
    opc = -1
    try:
        opc = int(input("Ingrese la opcion: "))
    except Exception:
        opc = 2
    if opc == 1:
        usuario["estudiante"] = True
    else:
        usuario["estudiante"] = False
    print("Ingrese 1 si el cliente juega videojuegos de forma competitiva o 2 de lo contrario")
    opc = -1
    try:
        opc = int(input("Ingrese la opcion: "))
    except Exception:
        opc = 2
    if opc == 1:
        usuario["videojuegos"] = True
    else:
        usuario["videojuegos"] = False
    usuario["cantidad_gente"]=int(input("Con cuanta gente vive el cliente?"))
    usuario["consultas"]=input()
    usuario["reclamaciones"]=""
    usuario["sugerencias"]=""
    usuario["cantidad_compras"]=1
    usuario["sus_servicios"]=[]
    usuario["productos"]=[]

    datos["usuarios"].append(usuario)

    print("cliente registrado con éxito!")
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

    print("Estos son los clientes disponibles")

    for i in range(len(datos["usuarios"])):
        print(datos["usuarios"][i]["nombre"], end=": ")
        print(datos["usuarios"][i]["documento"])


    doc_soli =input("Ingrese el documento del cliente que quiere editar: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == doc_soli:
                datos["usuarios"][i]["nombre"]=input("Ingrese el nuevo nombre: ")
                datos["usuarios"][i]["documento"]=input("Ingrese el nuevo documento: ")
                print("Usuario modificado con exito!")
                return datos
        print("El usuario no existe :(")
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
        
            

     