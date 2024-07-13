import shutil
import os
import msvcrt


def print_centrado(texto, x=0, y=0, color="default"):
    # Obtener las dimensiones de la terminal actual
    ancho_terminal = shutil.get_terminal_size().columns
    alto_terminal = shutil.get_terminal_size().lines

    # Diccionario de colores ANSI
    colores = {
        "default": "\033[0m",
        "negro": "\033[30m",
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "magenta": "\033[35m",
        "cian": "\033[36m",
        "blanco": "\033[37m",
    }

    # Obtener el código de color, por defecto es el color por defecto de la terminal
    color_code = colores.get(color.lower(), "\033[0m")

    # Si x y y son mayores que 0, se usan como coordenadas de inicio para el texto
    if x > 0 or y > 0:
        columna_inicio = x
        fila_inicio = y
    else:
        # Si no, se centran el texto en la terminal
        columna_inicio = (ancho_terminal - len(texto)) // 2
        fila_inicio = alto_terminal // 2

    # Mover el cursor a la posición especificada y luego imprimir el texto con el color
    print(f"\033[{fila_inicio};{columna_inicio}H{color_code}{texto}\033[0m")



def Input(mensaje="", x=0, y=0, color="default"):
    if mensaje:
        print_centrado(mensaje, x, y, color)
    msvcrt.getch()