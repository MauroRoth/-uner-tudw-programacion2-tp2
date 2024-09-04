from Pizza import Pizza

class MaestroPizzero:
    # atributos de clase

    # método de inicialización
    def __init__(self,nombre) -> None:
        # atributos de instancia
        self.nombre = nombre
        self.pizzasPorCocinar = list()
        self.pizzasPorEntregar = list()

    # comandos
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def tomarPedido(self,nombre_pizza):
        # requiere nombre_pizza no vacío
        pizza = Pizza(nombre_pizza)
        self.pizzasPorCocinar.append(pizza)
    
    def cocinar(self):
        if len(self.pizzasPorCocinar)>0:
            self.pizzasPorEntregar = self.pizzasPorCocinar
    
    def entregar(self):
        entregadas = list()
        if len(self.pizzasPorEntregar)>1:
            for i in range(2):
                pizza = self.pizzasPorEntregar.pop(0)
                entregadas.append(pizza) 
        elif len(self.pizzasPorEntregar)==1:
            pizza = self.pizzasPorEntregar.pop()
            entregadas.append(pizza)
        return entregadas

    # consultas
    def getNombre(self):
        return self.nombre
    
    def getPizzasPorCocinar(self):
        return self.pizzasPorCocinar
    
    def getPizzasPorEntregar(self):
        return self.pizzasPorEntregar
    
    

