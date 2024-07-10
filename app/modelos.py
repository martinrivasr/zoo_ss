from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()

class Entradas:
    def __init__(self, edad:int):
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad <= 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio =  14
        elif edad <= 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else:
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

class Grupo_Entrada:
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {
            TipoEntrada.BEBE: 0,
            TipoEntrada.NIÑO: 0,
            TipoEntrada.ADULTO: 0,
            TipoEntrada.JUBILADO: 0,
        }

    def add_entrada(self, edad):
        nueva_entrada = Entradas(edad)
        self.num_entradas +=  1
        self.total +=  nueva_entrada.precio
        self.tipos_entrada[nueva_entrada.tipo] += 1

    def cantidad_entradas_por_tipo(self, tipo : TipoEntrada) -> int:
        return self.tipos_entrada[tipo]



    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        precio = 0
        if tipo == TipoEntrada.BEBE:
            precio = 0
        elif tipo == TipoEntrada.NIÑO:
            precio = 14
        elif tipo == TipoEntrada.ADULTO:
            precio = 23
        elif tipo == TipoEntrada.JUBILADO:
            precio = 18
        return self.tipos_entrada[tipo] * precio