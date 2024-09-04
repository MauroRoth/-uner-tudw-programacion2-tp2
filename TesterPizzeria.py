from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
from Pizza import Pizza

class TesterPizzeria:
    def main(self):
        maestroPizzero1 = MaestroPizzero('Anibal')
        print('Maestro Pizzero: ', maestroPizzero1.getNombre())
        mozo1 = Mozo('Alberto')
        mozo2 = Mozo('Luis')
        print('Mozo 1: ', mozo1.getNombre())
        print('Mozo 2: ', mozo2.getNombre())

        pizza1 = Pizza('primavera')
        pizza2 = Pizza('especial')
        pizza3 = Pizza('fugazeta')
        pizza4 = Pizza('calabresa')

        maestroPizzero1.tomarPedido(pizza1.getVariedad())
        maestroPizzero1.tomarPedido(pizza2.getVariedad())
        maestroPizzero1.tomarPedido(pizza3.getVariedad())
        maestroPizzero1.tomarPedido(pizza4.getVariedad())

        print('\nLista de Pizzas por Cocinar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorCocinar()))

        maestroPizzero1.cocinar()

        print('\nLista de Pizzas por Entregar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))

        entregadas = maestroPizzero1.entregar()

        print('\nEntregadas: ')
        list(map(lambda x: print(x.getVariedad()),entregadas))
        
        print('\nLista de Pizzas por Entregar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))

        print('Estado del Mozo: ', mozo1.isEstadoLibre())
        pizzas = [pizza1,pizza2,pizza3]
        mozo1.tomarPizzas(pizzas)
        list(map(lambda x: print(x.getVariedad()),mozo1.getPizzas()))
        print('Estado del Mozo: ', mozo1.isEstadoLibre())
        mozo1.servirPizzas()
        list(map(lambda x: print(x.getVariedad()),mozo1.getPizzas()))
        print('Estado del Mozo: ', mozo1.isEstadoLibre())
        # soluciones de los puntos 5a, 5b, 5c ...
        

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()