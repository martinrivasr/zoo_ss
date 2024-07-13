from app.modelos import Entradas,TipoEntrada, Grupo_Entrada
import pytest

def test_crear_entradas():

    entradas = Entradas(12)
    assert entradas.tipo == TipoEntrada.NIÑO
    assert entradas.precio == 14

    entradas = Entradas(35)
    assert entradas.tipo == TipoEntrada.ADULTO
    assert entradas.precio == 23

    entradas = Entradas(70)
    assert entradas.tipo == TipoEntrada.JUBILADO
    assert entradas.precio == 18

    entradas = Entradas(1)
    assert entradas.tipo == TipoEntrada.BEBE
    assert entradas.precio == 0

def xtest_crear_entrada_edad_negativa_error():
    with pytest.raises(ValueError):
        Entradas(-2)
    #try:
    #    entrada = Entradas (-2)
    #    assert False, "No ha saltado ValueError"

    #except ValueError:

    #    assert True 

def xtest_crear_entrada_edad_centenario_error():
    pass


def test_crear_grupo_entradas ():
    grupo = Grupo_Entrada()
    assert grupo.total == 0
    assert grupo.num_entradas == 0

def test_anyadir_entradas_a_grupo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(35)
    assert grupo.num_entradas == 1
    assert grupo.total == 23

    grupo = Grupo_Entrada()
    grupo.add_entrada(35)
    assert grupo.num_entradas == 1
    assert grupo.total == 23

    grupo.add_entrada(12)
    assert grupo.num_entradas == 2
    assert grupo.total == 37

    grupo.add_entrada(70)
    assert grupo.num_entradas == 3
    assert grupo.total == 55

    grupo.add_entrada(2)
    assert grupo.num_entradas == 4
    assert grupo.total == 55


def test_cantidad_entradas_por_tipo ():
    grupo = Grupo_Entrada()
    grupo.add_entrada (10)

    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.NIÑO) == 1

    grupo.add_entrada(36)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.ADULTO) == 1

    grupo.add_entrada(14)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.NIÑO) == 1

def test_subtotal_por_tipo ():
    grupo = Grupo_Entrada()
    grupo.add_entrada (10)

    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 14

