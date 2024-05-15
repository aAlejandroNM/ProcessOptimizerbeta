from menus import *
from datetime import datetime
from manejoexcepciones import *
def crear_venta(datos, datos_usuarios,datos_servicios,datos_productos):
    datos = dict(datos)
    venta={}
   
    print("Estos son los usuarios disponibles")

    for i in range(len(datos_usuarios["usuarios"])):
        print(datos_usuarios["usuarios"][i]["documento"], end=": ")
        print(datos_usuarios["usuarios"][i]["nombre"])

    venta["id"]=generador_id(datos)
    cliente=input("Ingrese el nombre del cliente: ")
    documento=input("Ingrese el documento del cliente: ")

    print("Que quiere vender ?")
    print("(1) Servicio")
    print("(2) Producto")
    opc = int(input("numero "))
    servicio=""
    producto=""
    valor_total = 0
    if opc == 1:
        
        print("Estos son los Servicios disponibles")
        for i in range(len(datos_servicios["servicios"])):
            print(datos_servicios["servicios"][i]["id"], end=": ")
            print(datos_servicios["servicios"][i]["nombre"])
            
        print(f'Para el cliente {cliente} le recomendamos los siguientes servicios: ')

        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["nombre"]==cliente:
                if datos_usuarios["usuarios"][i]["videojuegos"]== True:
                    print('ID',datos_servicios["servicios"][0]["id"], end=": ")
                    print(datos_servicios["servicios"][0]["nombre"])
                elif datos_usuarios["usuarios"][i]["cantidad_gente"]>4:
                    print('ID',datos_servicios["servicios"][1]["id"], end=": ")
                    print(datos_servicios["servicios"][1]["nombre"])

        id_solici = int(input("ingrese el id del servicio que desea vender"))
        
        #busca el id del servicio y se asigna a valor_total para luego agregar al diccionario
        for i in range(len(datos_servicios["servicios"])):
            if datos_servicios["servicios"][i]["id"] == id_solici:
                servicio = datos_servicios["servicios"][i]["nombre"]
                valor_total =datos_servicios["servicios"][i]["precio"]
        
        #cambia el valor de cantidad de comprar de los usuarios y agrega el servicio escogido a la lista sus_servicios de usuarios
        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["documento"] == documento:
                datos_usuarios["usuarios"][i]["sus_servicios"].append(servicio)
                datos_usuarios["usuarios"][i]["cantidad_compras"]=+1

    elif opc ==2:
        print("Estos son los productos disponibles")
        for i in range(len(datos_productos["productos"])):
            print(datos_productos["productos"][i]["id"], end=": ")
            print(datos_productos["productos"][i]["nombre"])
        
        
        #Mostrar la oferta de estudiantes 
        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["nombre"]==cliente:
                if datos_usuarios["usuarios"][i]["estudiante"]== True:
                    print(f'Para el cliente {cliente} le recomendamos los siguientes Productos ya que es estudiante: ')
                    print('ID',datos_productos["productos"][0]["id"], end=": ")
                    print(datos_productos["productos"][0]["nombre"])
                    print('Precio actual: ',datos_productos["productos"][0]["precio"])
                    precio = datos_productos["productos"][0]["precio"]
                    print("Los estudiantes tienen descuento de 15% en el siguiente producto")
                    print("Precio con descuento del 15%:", precio - (precio * 0.15))
                     
                    

        id_solici = int(input("ingrese el id del producto que desea vender"))
        for i in range(len(datos_productos["productos"])):
            if datos_productos["productos"][i]["id"] == id_solici:
                producto = datos_productos["productos"][i]["nombre"]
                valor_total=datos_productos["productos"][i]["precio"]

        
        for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["documento"] == documento:
                datos_usuarios["usuarios"][i]["productos"].append(producto)
                datos_usuarios["usuarios"][i]["cantidad_compras"] +=1

    venta["cliente"]=cliente
    venta["producto"]=producto
    venta["servicio"]=servicio
    #ciclo para restarle el 20% de descuento si son clientes leales
    for i in range(len(datos_usuarios["usuarios"])):
            if datos_usuarios["usuarios"][i]["nombre"] == cliente:
                if datos_usuarios['usuarios'][i]["tipo_cliente"]=="leal":
                    print("como es cliente leal se le hara un descuento del 20%")
                    valor_total = valor_total - (valor_total * 0.2)
    #calcular descuento de estudiante
    for i in range(len(datos_usuarios["usuarios"])):
        if datos_usuarios["usuarios"][i]["documento"]== documento:
            if datos_usuarios["usuarios"][i]["estudiante"]==True and id_solici == 1:
                valor_total = valor_total -(valor_total*0.15)
    
    venta["valor_total"]=valor_total
    venta["documento"]=documento
    venta["fecha"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    datos["ventas"].append(venta)


    print("venta realizada con éxito!")
    
    return datos, datos_usuarios

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

def caracteristicas_pro_ser(datos_productos, datos_servicios):
    print("Caracteristicas Productos")
    for i in range(len(datos_productos["productos"])):
        print('Id',datos_productos["productos"][i]["id"], end=": ")
        print(datos_productos["productos"][i]["nombre"])
        print('Caracteristicas: ',datos_productos["productos"][i]["caracteristicas"])
        print('Precio: ',datos_productos["productos"][i]["precio"])
    print("***************************************")
    print("Caracteristicas Servicios")
    for i in range(len(datos_servicios["servicios"])):
        print('Id',datos_servicios["servicios"][i]["id"], end=": ")
        print(datos_servicios["servicios"][i]["nombre"])
        print('Caracteristicas: ',datos_servicios["servicios"][i]["caracteristicas"])
        print('Precio: ',datos_servicios["servicios"][i]["precio"])

def generador_id(datos):
    return len(datos["ventas"]) + 1

def actualizador_id(datos):
    for i in range(len(datos["ventas"])):
        datos["ventas"][i]["id"] = i + 1
    return datos
