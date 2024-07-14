from app.modelos import Grupo_Entrada,TipoEntrada
from app.utils import print_centrado, input_centrado
import os

class VistaGrupo:

    def __init__(self, grupo: Grupo_Entrada, x=1, y=1, color="default"):
        self.grupo = grupo
        self.x = x
        self.y = y
        self.color = color
    
    def paint(self):
        contador_lineas = self.y

        #texto_formateado = f"{tipo.name:.<14s}{tipo.value.precio:5.2f}    {grupo.cantidad_entradas_por_tipo(tipo):2d}     {grupo.subtotal_tipo(tipo):7.2f}"
        print_centrado("Tipo                    PU      Q       TOTAL", self.x, contador_lineas,self.color)
        contador_lineas += 1
        print_centrado("=============================================", self.x, contador_lineas,self.color)
        contador_lineas += 1
        for indice, tipo in enumerate(TipoEntrada):
            texto_formateado = f"{tipo.name:.<22s}{tipo.precio:5.2f}    {self.grupo.cantidad_entradas_por_tipo(tipo):2d}    {self.grupo.subtotal_tipo(tipo):7.2f}"
            print_centrado(texto_formateado, self.x, contador_lineas, self.color)
            contador_lineas += 1 
        
        print_centrado("---------------------------------------------",self.x, contador_lineas, self.color)
        contador_lineas += 1 
        print_centrado(f"                              {self.grupo.num_entradas:3d}   {self.grupo.total:8.2f}",self.x,contador_lineas, self.color)

class VistaEntrada:
    def __init__(self, etiqueta: str, x, y, color= "default"):
        self.etiqueta = etiqueta
        self.y = y
        self.x = x
        self.value = ""
        self.color = color

    def paint(self):
        
        return input_centrado(self.etiqueta, self.x, self.y, self.color)

#if __name__ == "__main__":    
#    os.system('cls')
#    grupo = Grupo_Entrada()
#    grupo.add_entrada(2)
#    grupo.add_entrada(2)
#    grupo.add_entrada(6)
 #   grupo.add_entrada(15)
 #   grupo.add_entrada(70)


 #   vg = VistaGrupo(grupo,10,10,"azul")


 #   vedad = VistaEntrada("EDAD: ", 10, 30,"Azul")

 #   vg.paint()

 #   vedad.paint()
     
 #   Input("Pulsa Enter para acabar", 10,32,"Rojo")