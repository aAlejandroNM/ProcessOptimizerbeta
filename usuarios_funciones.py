def crear_usuarios(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")

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

def modificar_clientes():
     