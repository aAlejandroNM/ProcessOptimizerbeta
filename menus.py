from usuarios_funciones import*
from datos import *

USUARIOS_DB = "usuarios.json"
datos_usuarios = traer_datos(USUARIOS_DB)

def menu_principal():
    print("***************************************")
    print("Menu Principal")
    print("(1) Usuarios")
    print("(2) Gestion Servicios")
    print("(3) Ventas")
    print("(4) Reportes")
    print("(5) Salir")
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
            print("pendiente")
        elif opc == 3:
             eliminar_usuarios(datos_usuarios)
        elif opc == 4:
            break
        guardar_datos(datos_usuarios,USUARIOS_DB)

def menu_gestion_servicios():
    print("***************************************")
    print("Menu Gestion Servicios")
    print("(1) Crear Servicios")
    print("(2) Modificar Servicios")
    print("(3) Eliminar Servicios")
    print("(4) Caracteristicas Servicios")
    print("(5) Atras")
    print("***************************************")
    while True:
            opc = pedir_opcion()
            if opc == 1:
                 print("pendiente")
            elif opc == 2:
                 print("pendiente")
            elif opc == 3:
                 print("pendiente")
            elif opc == 4:
                 print("pendiente")
            elif opc == 5:
                break    
    
def menu_Ventas():
    print("***************************************")
    print("Menu Ventas")
    print("(1) Crear Venta")
    print("(2) Mostrar Venta")
    print("(3) productos segun sus caracteristicaspendiente")
    print("(4) Atras")
    print("***************************************")
    while True:
        opc = pedir_opcion()
        if opc == 1:
            print("pendiente")
        elif opc == 2:
            print("pendiente")
        elif opc == 3:
            print("pendiente")             
        elif opc == 4:
            break

def menu_Reportes():
    print("***************************************")
    print("Menu Reportes")
    print("(1) Generar Reporte Cantidad Productos")
    print("(2) Generar Reporte Servicios Màs Populares")
    print("(3) mostrar lo que cada usuario ha comprado y su cantidad")
    print("(4) Atras")
    print("***************************************")
    while True:        
        opc = pedir_opcion()
        if opc == 1:
            print("pendiente")
        elif opc == 2:
            print("pendiente") 
        elif opc == 3:
            print("pendiente")  
        elif opc == 4:
            break

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