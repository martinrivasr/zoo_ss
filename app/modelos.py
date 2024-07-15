from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = ("BEBE",0)
    NIÑO = ("NIÑO",14)
    ADULTO = ("ADULTO",23)
    JUBILADO = ("JUBILADO",18)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Entradas:
    def __init__(self, edad:int):
        if edad < 0:
            raise ValueError ("La edad no puede ser negativa")
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            #self.precio = TipoEntrada.BEBE
        elif edad <= 13:
            self.tipo = TipoEntrada.NIÑO
            #self.precio =  TipoEntrada.NIÑO
        elif edad <= 65:
            self.tipo = TipoEntrada.ADULTO
            #self.precio = TipoEntrada.ADULTO
        else:
            self.tipo = TipoEntrada.JUBILADO
            #self.precio = TipoEntrada.JUBILADO
        self.precio = self.tipo.precio


    def __validate_edad(self, edad):
        if edad < 0 == 0 or edad > 99:
            raise ValueError("la edad no debe ser negativa, o mayor a 99")
class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: {'P':TipoEntrada.BEBE.precio, 'Q':0},
            TipoEntrada.NIÑO: {'P':TipoEntrada.NIÑO.precio, 'Q':0},
            TipoEntrada.ADULTO: {'P':TipoEntrada.ADULTO.precio, 'Q':0},
            TipoEntrada.JUBILADO: {'P':TipoEntrada.JUBILADO.precio, 'Q':0}
        }

 # se genera una nueva instancia con la edad ques e recibe, 
                                        # cada que se agrega un nuevo atribito en init, se debe agregar aqui 
                                        # el atributo para irlo adicionando o incrementando 
# aqui se encapsula , comprotamiento y estado. se encapsula
                                                     # entrada y se ahí se pasa el valor.
    def add_entrada(self, edad):
        nueva_entrada = Entradas(edad) 
                                         
        self.total +=  nueva_entrada.precio
        self.num_entradas +=  1

        self.tipos_entrada[nueva_entrada.tipo]["Q"] += 1 
        

    def cantidad_entradas_por_tipo(self, tipo : TipoEntrada) -> int: 
        #return self.tipos_entrada[tipo]         # Se crea este metodo ara poder acceder a los datos del diccionario
        return self.tipos_entrada[tipo]['Q'] #py que se genero en el init
        
    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]['Q'] *  self.tipos_entrada[tipo]['P']
        