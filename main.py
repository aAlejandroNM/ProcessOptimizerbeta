from menus import *
from datos import *


USUARIOS_DB = "usuarios.json"
datos_usuarios = traer_datos(USUARIOS_DB)

SERVICIOS_DB = "servicios.json"
datos_servicios = traer_datos(SERVICIOS_DB)

PRODUCTOS_DB = "productos.json"
datos_productos = traer_datos(PRODUCTOS_DB)

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        menu_usuarios()
    elif opc == 2:
        menu_gestion_servicios()
    elif opc == 3:
        menu_Ventas()
    elif opc == 4:
        menu_productos()
    elif opc == 5:
        menu_Reportes()
    elif opc == 6:
        menu_servicio_cliente()
    elif opc == 7:
        print("Salió!!")
        break