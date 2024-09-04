from MaestroPizzero import MaestroPizzero
from Mozo import Mozo


class TesterPizzeria:
    def main(self):
        maestroPizzero1 = MaestroPizzero('Anibal')
        print('Maestro Pizzero: ', maestroPizzero1.getNombre())
        mozo1 = Mozo('Alberto')
        mozo2 = Mozo('Luis')
        print('Mozo 1: ', mozo1.getNombre())
        print('Mozo 2: ', mozo2.getNombre())

        maestroPizzero1.tomarPedido('primavera')
        maestroPizzero1.tomarPedido('especial')
        maestroPizzero1.tomarPedido('fugazeta')
        #maestroPizzero1.tomarPedido('calabresa')
        print('\nLista de Pizzas por Cocinar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorCocinar()))

        maestroPizzero1.cocinar()

        print('\nLista de Pizzas por Entregar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))
        entregadas = maestroPizzero1.entregar()
        print('\nEntregadas: ')
        list(map(lambda x: print(x.getVariedad()),entregadas))
        
        print('\nLista de Pizzas por Entregar luego de la Entrega')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))

        # soluciones de los puntos 5a, 5b, 5c ...
        

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()