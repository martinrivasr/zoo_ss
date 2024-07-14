from app.controladores import Zoo
from app.utils import dimensiones_terminal

# esta funcion calcula las coordinadas de la terminal para que el programa siempre aparezca centrdo
# el calculo se toma del calculo de las dimensiones de los  texto del detalle de entradas y del total de filas que se tienen estimadas
# en el programa, por ejemplo el detalle de la tabla tiene 47 caracteres y son 12 filas las que se tienen en el detalle
# de las entradas, esos números son los que toma para realizar el cálculo para centrar el programa

x, y = dimensiones_terminal(47,12)


zoo = Zoo(x,y,"magenta")
zoo.run()




