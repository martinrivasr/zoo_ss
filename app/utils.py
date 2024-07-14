import shutil
import os
import msvcrt
import sys



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


def input_centrado(prompt, x=0, y=0, color="default"):
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
    # Si x y y son mayores que 0, se usan como coordenadas de inicio para el prompt
    if x > 0 or y > 0:
        columna_inicio = x
        fila_inicio = y
    else:
        # Si no, se centran el prompt en la terminal
        columna_inicio = (ancho_terminal - len(prompt)) // 2
        fila_inicio = alto_terminal // 2

    # Mover el cursor a la posición especificada y luego imprimir el prompt con el color
    print(f"\033[{fila_inicio};{columna_inicio}H{color_code}{prompt}\033[0m", end="", flush=True)

    # Posicionar el cursor para la entrada del usuario
    input_usuario = ""
    while True:
        char = msvcrt.getch()
        if char == b'\r':  # Enter
            break
        elif char == b'\x08':  # Backspace
            if len(input_usuario) > 0:
                input_usuario = input_usuario[:-1]
                print("\b \b", end="", flush=True)
        else:
            input_usuario += char.decode()
            print(char.decode(), end="", flush=True)
    print()  # Mover a la siguiente línea después de la entrada
    return input_usuario

def Cls():
    return os.system('cls')

def dimensiones_terminal(x=1,y=1):
    ancho_terminal = shutil.get_terminal_size().columns
    alto_terminal = shutil.get_terminal_size().lines

    inicio_columna = (ancho_terminal - x) // 2
    Inicio_fila =  (alto_terminal - y) // 2  

    return inicio_columna, Inicio_fila            