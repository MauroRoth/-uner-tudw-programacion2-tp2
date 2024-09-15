from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
from Pizza import Pizza

class TesterPizzeria:
    def main(self):
        # 5a. Crear objetos de tipo MaestroPizzero, Mozo y Pizza.
        # Único objeto MaestroPizzero 
        maestroPizzero1 = MaestroPizzero('Anibal')
        print('Maestro Pizzero: ', maestroPizzero1.getNombre())
        # Dos objetos de la clase mozo.
        mozo1 = Mozo('Alberto')
        mozo2 = Mozo('Luis')
        print('Mozo 1: ', mozo1.getNombre())
        print('Mozo 2: ', mozo2.getNombre())
        # Varios objetos de la clase Pizza
        pizza1 = Pizza('primavera')
        pizza2 = Pizza('especial')
        pizza3 = Pizza('fugazeta')
        pizza4 = Pizza('calabresa')

        # 5b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
        
        # Mensaje tomarPedido()
        maestroPizzero1.tomarPedido(pizza1.getVariedad())
        maestroPizzero1.tomarPedido(pizza2.getVariedad())
        maestroPizzero1.tomarPedido(pizza3.getVariedad())
        maestroPizzero1.tomarPedido(pizza4.getVariedad())

        print('\nLista de Pizzas por Cocinar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorCocinar()))

        # Mensaje cocinar()
        maestroPizzero1.cocinar()

        print('\nLista de Pizzas por Entregar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))
        
        # Mensaje entregar()
        entregadas = maestroPizzero1.entregar()

        print('\nEntregadas: ')
        list(map(lambda x: print(x.getVariedad()),entregadas))
        
        print('\nLista de Pizzas por Entregar')
        list(map(lambda x: print(x.getVariedad()),maestroPizzero1.getPizzasPorEntregar()))

        # 5c. Enviar los mensajes tomarPizzas y servirPIzzas a los objetos de la clase Mozo creados en el punto a.
        print(f'\nEstado del Mozo {mozo1.getNombre()}: {mozo1.isEstadoLibre()}')
        print(f'\nEstado del Mozo {mozo2.getNombre()}: {mozo2.isEstadoLibre()}')
        
        pizzas1 = [pizza1,pizza2,pizza3]
        pizzas2 = [pizza4]

        # Mensaje tomarPizzas()
        mozo1.tomarPizzas(pizzas1)
        print(f'\nPizzas tomadas por el Mozo {mozo1.getNombre()}')
        list(map(lambda x: print(x.getVariedad()),mozo1.getPizzas()))
        print(f'\nEstado del Mozo {mozo1.getNombre()}: {mozo1.isEstadoLibre()}')
        
        mozo2.tomarPizzas(pizzas2)
        print(f'\nPizzas tomadas por el Mozo {mozo2.getNombre()}')
        list(map(lambda x: print(x.getVariedad()),mozo2.getPizzas()))
        print(f'\nEstado del Mozo {mozo2.getNombre()}: {mozo2.isEstadoLibre()}')

        # Mensaje servirPizzas()
        mozo1.servirPizzas()
        print(f'\nPizzas Servidas por el Mozzo {mozo1.getNombre()}!!!')
        list(map(lambda x: print(x.getVariedad()),mozo1.getPizzas())) # comprueba que el mozo no tiene pizzas
        print(f'\nEstado del Mozo {mozo1.getNombre()}: {mozo1.isEstadoLibre()}')

        mozo2.servirPizzas()
        print(f'\nPizzas Servidas por el Mozzo {mozo2.getNombre()}!!!')
        list(map(lambda x: print(x.getVariedad()),mozo2.getPizzas())) # comprueba que el mozo no tiene pizzas
        print(f'\nEstado del Mozo {mozo1.getNombre()}: {mozo1.isEstadoLibre()}')
        
if __name__ == '__main__':
    print('PIZZERÍA <<<DON PIPO>>>')
    print(50*'-')
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()