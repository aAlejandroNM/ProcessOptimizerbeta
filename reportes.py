def cantidad_pr_servicios(datos_productos,datos_servicios):
    contador =0
    for producto in datos_productos["productos"]:
        print('ID', producto["id"], end=": ")
        print(producto["nombre"])
        contador +=1
    print("***************************************")
    print(F'TOTAL DE PRODUCTOS = {contador}')
    print("***************************************")
    contador=0
    for i in range(len(datos_servicios["servicios"])):
        print('ID',datos_servicios["servicios"][i]["id"],end=": ")
        print(datos_servicios["servicios"][i]["nombre"])
        contador +=1
    print("***************************************")
    print(F'TOTAL DE SERVICIOS = {contador}')

def mas_populares(datos_ventas):
    servicios =[]
    productos =[]

    for venta in datos_ventas["ventas"]:
        if "producto" in venta and venta["producto"] != "":
            productos.append(venta["producto"])
        if "servicio" in venta and venta["servicio"] != "":
            servicios.append(venta["servicio"])
    
    producto_mas_popular = "" 
    maximo_productos = 0  

    for producto in productos:
        cantidad = productos.count(producto)  # cuanntas veces aparece el producto en la lista
        if cantidad > maximo_productos:
            producto_mas_popular = producto
            maximo_productos = cantidad

    servicio_mas_popular = "" 
    maximo_servicios = 0  

    for servicio in servicios:
        cantidad = servicio.count(servicio)
        if cantidad > maximo_servicios:
            servicio_mas_popular = servicio
            maximo_servicios = cantidad
    print("***************************************")
    print(f"El producto más popular es: {producto_mas_popular}")
    print("***************************************")
    print(f"El servicio más popular es: {servicio_mas_popular}")

def syp_usuarios(datos_usuarios):
    for usuario in datos_usuarios["usuarios"]:
        nombre = usuario["nombre"]
        documento = usuario["documento"]
        
        print(f"Reporte para el usuario {nombre} (Documento: {documento}):")
        print("Servicios:")
        if usuario["sus_servicios"]:
            for servicio in usuario["sus_servicios"]:
                print(f"- {servicio}")
        else:
            print("El usuario no tiene servicios contratados.")
        
        print("\nProductos:")
        if usuario["productos"]:
            for producto in usuario["productos"]:
                print(f"- {producto}")
        else:
            print("El usuario no ha comprado productos.")