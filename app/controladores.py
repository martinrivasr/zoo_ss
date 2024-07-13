from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import Grupo_Entrada
from app.utils import print_centrado, Input
import shutil
import os

class Zoo:

    def __init__ (self):
        self.grupo_entradas = Grupo_Entrada()
        self.x = (shutil.get_terminal_size().columns - 37) // 2
        self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, 1)
        self.entrada_edad = VistaEntrada("EDAD: ", self.x, 10)
        self.entrada_seguir = VistaEntrada("Otra vez (S/n): ", self.x, 12)

# Bucle de pantalla 
    def run(self):
        while True:
            os.system('cls')
            self.vista_grupo.paint()
            edad = self.entrada_edad.paint()
            if edad == "":
                respuesta = self.entrada_seguir.paint()
                if respuesta == "S":
                    self.grupo_entradas = Grupo_Entrada()
                    self.vista_grupo.grupo = grupo_entradas
                    continue
                else:
                    break
            
            edad = int(edad)
            self.grupo_entradas.add_entrada(edad)

            # Final "controlado" del programa
        print_centrado("Pulse enter para salir", 1, shutil.get_terminal_size().lines - 2)
        Input()
