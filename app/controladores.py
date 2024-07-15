from app.vistas import VistaEntrada, VistaGrupo
from app.modelos import Grupo_Entrada
from app.utils import print_centrado, input_centrado, Cls
import shutil
import os
import time

class Zoo:

    def __init__ (self, x=1, y=1, color= "default"):
        self.color = color
        self.grupo_entradas = Grupo_Entrada()
        #self.x = (shutil.get_terminal_size().columns - 37) // 2
        self.x = x
        self.y = y
        self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, self.y, self.color)
        self.entrada_edad = VistaEntrada("EDAD: ", self.x, self.y + 10 , self.color)
        self.entrada_seguir = VistaEntrada("Otra vez (S/n): ", self.x,self.y + 12, self.color)

# Bucle de pantalla 
    def run(self):
        while True:
            #os.system('cls')
            Cls ()
            self.vista_grupo.paint()
            edad = self.entrada_edad.paint()
            if edad == "":
                respuesta = self.entrada_seguir.paint()
                if respuesta == "S":
                    self.grupo_entradas = Grupo_Entrada()
                    self.vista_grupo.grupo = self.grupo_entradas
                    continue
                else:
                    break
            



            if int(edad) > 99 :
                print_centrado("La edad no debe ser mayor a 99, ingrese nuevamente", self.x, self.y + 12 , self.color)
                time.sleep(1)
            else:
                edad = int(edad)
                self.grupo_entradas.add_entrada(edad)

            # Final "controlado" del programa
        print_centrado("Pulse enter para salir", 1, shutil.get_terminal_size().lines - 2, self.color)
        input()
