import traceback
import datetime

def manejar_excepciones(excepcion, continuar=True):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    mensaje_error = (f"{fecha_actual}: {excepcion}\n")
    
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(mensaje_error)
    
    # Mostrar el mensaje de error al usuario
    print(f"Se ha producido un error: {excepcion}")
    
    # Decidir si se debe continuar con el flujo del programa o detenerlo
    if continuar:
        return True
    else:
        return False
