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
        f1 = lambda x:x[0]<2
        f2 = lambda x:x[1]
        f3 = lambda x,y: y.remove(x)
        entregadas = list(map(f2,filter(f1,enumerate(self.pizzasPorEntregar))))
        list(map(lambda x: f3(x,self.pizzasPorEntregar),entregadas))
        return entregadas

    # consultas
    def getNombre(self):
        return self.nombre
    
    def getPizzasPorCocinar(self):
        return self.pizzasPorCocinar
    
    def getPizzasPorEntregar(self):
        return self.pizzasPorEntregar
    
    

