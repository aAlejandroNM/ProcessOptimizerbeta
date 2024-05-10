from menus import *
from datos import *


USUARIOS_DB = "usuarios.json"
datos_usuarios = traer_datos(USUARIOS_DB)


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
        menu_Reportes()
    elif opc == 5:
        print("Salió!!")
        break