from usuarios_funciones import *
from servicios_funciones import * 
from datos import *
from productos_funciones import *
from ventas_funciones import *
from reportes import *

USUARIOS_DB = "usuarios.json"
datos_usuarios = traer_datos(USUARIOS_DB)

SERVICIOS_DB = "servicios.json"
datos_servicios = traer_datos(SERVICIOS_DB)

PRODUCTOS_DB = "productos.json"
datos_productos = traer_datos(PRODUCTOS_DB)

VENTAS_DB = "ventas.json"
datos_ventas = traer_datos(VENTAS_DB)

def menu_principal():
    print("***************************************")
    print("Menu Principal")
    print("(1) Usuarios")
    print("(2) Gestion Servicios")
    print("(3) Ventas")
    print("(4) Productos")
    print("(5) Reportes ")
    print("(6) Servicio al Cliente")
    print('(7) Salir')
    print("***************************************")   

def menu_usuarios():
    while True:
        print("***************************************")
        print("Menu Usuarios")
        print("(1) Crear Usuarios")
        print("(2) Modificar Usuarios")
        print("(3) Eliminar Usuarios")
        print("(4) Atras")
        print("***************************************")
        opc = pedir_opcion()
        if opc == 1:
            crear_usuarios(datos_usuarios)
        elif opc == 2:
            modificar_clientes(datos_usuarios)
        elif opc == 3:
            eliminar_usuarios(datos_usuarios)
        elif opc == 4:
            break
        guardar_datos(datos_usuarios,USUARIOS_DB)

def menu_gestion_servicios():
    while True:
        print("***************************************")
        print("Menu Gestion Servicios")
        print("(1) Crear Servicios")
        print("(2) Modificar Servicios")
        print("(3) Eliminar Servicios")
        print("(4) Atras")
        print("***************************************")
        opc = pedir_opcion()
        if opc == 1:
            crear_servicio(datos_servicios)
        elif opc == 2:
            modificar_servicios(datos_servicios)
        elif opc == 3:
            eliminar_servicios(datos_servicios)
        elif opc == 4:
            break
        guardar_datos(datos_servicios,SERVICIOS_DB)

def menu_productos():
    while True:
        print("***************************************")
        print("Menu Gestion Productos")
        print("(1) Crear Producto")
        print("(2) Modificar Producto")
        print("(3) Eliminar Producto")
        print("(4) Atras")
        print("***************************************")
        opc = pedir_opcion()
        if opc == 1:
            crear_producto(datos_productos)
        elif opc == 2:
            modificar_producto(datos_productos)
        elif opc == 3:
            eliminar_producto(datos_productos)
        elif opc == 4:
            break
        guardar_datos(datos_productos,PRODUCTOS_DB)

def menu_Ventas():
    
    while True:
        print("***************************************")
        print("Menu Ventas")
        print("(1) Crear Venta")
        print("(2) Mostrar Ventas")
        print("(3) Caracteristicas Servicios/Productos")
        print("(4) Atras")
        print("***************************************")
        opc = pedir_opcion()
        if opc == 1:
            crear_venta(datos_ventas, datos_usuarios,datos_servicios, datos_productos)
            documento =input("ingrese el documento de nuevo para confirmar la venta: ")
            actualizador_tipo_cliente(datos_usuarios,documento)
        elif opc == 2:
            mostrar_ventas(datos_ventas)
        elif opc == 3:
            caracteristicas_pro_ser(datos_productos, datos_servicios)      
        elif opc == 4:
            break
        guardar_datos(datos_usuarios,USUARIOS_DB)
        guardar_datos(datos_ventas,VENTAS_DB)

def menu_Reportes():
   
    while True:
        print("***************************************")
        print("Menu Reportes")
        print("(1) Generar Reporte Cantidad Productos")
        print("(2) Generar Reporte Servicios Màs Populares")
        print("(3) mostrar lo que cada usuario ha comprado y su cantidad")
        print("(4) Atras")
        print("***************************************")      
        opc = pedir_opcion()
        if opc == 1:
            cantidad_pr_servicios(datos_productos,datos_servicios)
        elif opc == 2:
            mas_populares(datos_ventas) 
        elif opc == 3:
            syp_usuarios(datos_usuarios) 
        elif opc == 4:
            break

def menu_servicio_cliente():
    while True:
        print("***************************************")
        print("Menu Servicio al Cliente")
        print("(1) Crear Consulta de un cliente")
        print("(2) Crear Reclamacion")
        print("(3) Crear Sugerencia")
        print("(4) Atras")
        print("***************************************")
        opc = pedir_opcion()
        if opc == 1:
            crear_consulta(datos_usuarios)
        elif opc == 2:
            crear_reclamacion(datos_usuarios) 
        elif opc == 3:
            crear_sugerencia(datos_usuarios)
        elif opc == 4:
            break
        guardar_datos(datos_usuarios,USUARIOS_DB)

def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1