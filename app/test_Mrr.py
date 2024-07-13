from utils import print_centrado

# Datos de ejemplo
tipo = type('Tipo', (object,), {"name": "Ejemplo", "value": type('Value', (object,), {"precio": 10.50})()})()
grupo = type('Grupo', (object,), {"cantidad_entradas_por_tipo": lambda self, x: 5, "subtotal_tipo": lambda self, x: 52.50})()

# Formatear el texto
indice = 1
texto_formateado = f"{tipo.name:.<14s}{tipo.value.precio:5.2f}    {grupo.cantidad_entradas_por_tipo(tipo):2d}     {grupo.subtotal_tipo(tipo):7.2f}"

# Usar print_centrado para imprimir el texto formateado
print_centrado(texto_formateado, 20, 4 + 3 + indice, "azul")



from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import Grupo_Entrada
from app.utils import print_centrado, Input
import shutil
import os

grupo_entradas = Grupo_Entrada()

x = (shutil.get_terminal_size().columns - 37) // 2

vista_grupo = VistaGrupo(grupo_entradas, x, 1)
entrada_edad = VistaEntrada("EDAD: ", x, 10)
entrada_seguir = VistaEntrada("Otra vez (S/n): ", x, 12)

# Bucle de pantalla 
while True:
    os.system('cls')
    vista_grupo.paint()
    edad = entrada_edad.paint()
    if edad == "":
        respuesta = entrada_seguir.paint()
        if respuesta == "S":
            grupo_entradas = Grupo_Entrada()
            vista_grupo.grupo = grupo_entradas
            continue
        else:
            break
    else:
        edad = int(edad)
        grupo_entradas.add_entrada(edad)

# Final "controlado" del programa
print_centrado("Pulse enter para salir", 1, shutil.get_terminal_size().lines - 2)
Input()
