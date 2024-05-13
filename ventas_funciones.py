from menus import *
from datetime import datetime
def crear_venta(datos, datos_usuarios,datos_servicios,datos_productos):
    datos = dict(datos)
    venta={}
   
    print("Estos son los usuarios disponibles")

    for i in range(len(datos_usuarios["usuarios"])):
        print(datos_usuarios["usuarios"][i]["documento"], end=": ")
        print(datos_usuarios["usuarios"][i]["nombre"])

    venta["id"]=generador_id(datos)
    venta["cliente"]=input("Ingrese el nombre del cliente: ")
    documento=input("Ingrese el documento del cliente: ")

    print("Que quiere vender ?")
    print("(1) Servicio")
    print("(2) Producto")
    opc = int(input("numero "))
    servicio=""
    producto=""
    if opc == 1:
        
        print("Estos son los Servicios disponibles")
        for i in range(len(datos_servicios["servicios"])):
            print(datos_servicios["servicios"][i]["id"], end=": ")
            print(datos_servicios["servicios"][i]["nombre"])

        id_solici = int(input("ingrese el id del servicio que desea vender"))
        
        for i in range(len(datos_servicios["servicios"])):
            if datos_servicios["servicios"][i]["id"] == id_solici:
                servicio = datos_servicios["servicios"][i]["nombre"]
        
        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["documento"] == documento:
                datos_usuarios["usuarios"][i]["sus_servicios"].append(servicio)
                datos_usuarios["usuarios"][i]["cantidad_compras"]=+1

    elif opc ==2:
        print("Estos son los productos disponibles")
        for i in range(len(datos_productos["productos"])):
            print(datos_productos["productos"][i]["id"], end=": ")
            print(datos_productos["productos"][i]["nombre"])

        id_solici = int(input("ingrese el id del producto que desea vender"))
        for i in range(len(datos_productos["productos"])):
            if datos_productos["productos"][i]["id"] == id_solici:
                producto = datos_productos["productos"][i]["nombre"]
        
        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["documento"] == documento:
                datos_usuarios["usuarios"][i]["productos"].append(producto)
                datos_usuarios["usuarios"][i]["cantidad_compras"] +=1

    venta["producto"]=producto
    venta["servicio"]=servicio
    venta["documento"]=documento
    venta["fecha"]=datetime.now().strftime("%Y-%m-%d %H:%M")
    datos["ventas"].append(venta)


    print("venta realizada con éxito!")
    
    return datos, datos_usuarios 

# def actualizador_tipo_cliente(datos_usuarios,documento):
#     for i in range(len(datos_usuarios)):
#         print(datos_usuarios["usuarios"][i]["documento"])
#         print(documento)
#         print(i)
#         print(len(datos_usuarios))

#         if datos_usuarios["usuarios"][i]["documento"]== documento:
#             if datos_usuarios["usuarios"][i]["cantidad_compras"] ==1:
#                 datos_usuarios["usuarios"][i]["tipo_cliente"]="regular"
#             elif datos_usuarios["usuarios"][i]["cantidad_compras"] >=3:
#                 datos_usuarios["usuarios"][i]["tipo_cliente"]="leal"
#             return datos_usuarios
#         else:
#             print("no se encontro dicho documento")
#     return datos_usuarios

def actualizador_tipo_cliente(datos_usuarios, documento):
    for usuario in datos_usuarios["usuarios"]:
        if usuario["documento"] == documento:
            if usuario["cantidad_compras"] == 1:
                usuario["tipo_cliente"] = "regular"
            elif usuario["cantidad_compras"] >= 3:
                usuario["tipo_cliente"] = "leal"
            return datos_usuarios
    print("No se encontró el usuario con el documento especificado:", documento)
    return datos_usuarios




def mostrar_ventas(datos):
    for i in range(len(datos["ventas"])):
        print( "ID:",datos["ventas"][i]["id"], end=" ")
        print("Nombre Cliente: ",datos["ventas"][i]["cliente"])
        print("Doc Identidad: ",datos["ventas"][i]["documento"])
        print("Fecha Venta: ",datos["ventas"][i]["fecha"])
        print("***************************************")

def caracteristicas_pro_ser(datos,datos_servicios):
    print("Caracteristicas Productos")
    for i in range(len(datos["productos"])):
        print(datos["ventas"][i]["id"])
        print(datos["ventas"][i]["nombre"])
        print(datos["ventas"][i]["caracteristicas"])
        print(datos["ventas"][i]["precio"])
    print("Caracteristicas Servicios")
    for i in range(len(datos_servicios["servicios"])):
        print(datos_servicios["servicios"][i]["id"])
        print(datos_servicios["servicios"][i]["nombre"])
        print(datos_servicios["servicios"][i]["caracteristicas"])
        print(datos_servicios["servicios"][i]["precio"])

def generador_id(datos):
    return len(datos["ventas"]) + 1

def actualizador_id(datos):
    for i in range(len(datos["ventas"])):
        datos["ventas"][i]["id"] = i + 1
    return datos
