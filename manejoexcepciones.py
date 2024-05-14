import traceback
import datetime

def manejar_excepciones(excepcion, continuar=True):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    mensaje_error = (f"{fecha_actual}: {excepcion}\n")
    
    with open("errores.txt", "a") as archivo_errores:
        archivo_errores.write(mensaje_error)
    

    print(f"Se ha producido un error: {excepcion}")

    if continuar:
        return True
    else:
        return False
