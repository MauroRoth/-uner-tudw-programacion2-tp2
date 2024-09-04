import Pizza

class MaestroPizzero:
    # atributos de clase
    # atributos de instancia
    nombre = str
    pizzasPorCocinar = Pizza()
    pizzasPorEntregar = Pizza()

    # constructor
    def __init__(self,nombre) -> None:
        self.nombre = nombre

    # comandos
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def tomarPedido(self,pizza):
        self.pizzasPorEntregar.append(pizza)
    
    def cocinar(self):
        pass
    
    def entregar(self):
        pass

    # consultas
    def getNombre(self):
        return self.nombre
    
    def getPizzasPorCocinar(self):
        return self.pizzasPorCocinar
    
    def getPizzasPorEntregar(self):
        return self.pizzasPorEntregar
    
    

