from app.modelos import Entradas,TipoEntrada

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
