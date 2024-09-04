from Pizza import Pizza

class Mozo:
    # atributos de clase

    # método de inicialización
    def __init__(self,nombre):
        # atributos de instancia
         self.nombre = nombre
         self.pizzas = Pizza('primavera')
       
    
    # comandos
    def getNombre(self,nombre):
        self.nombre = nombre
    
    def tomarPizzas(self,pizzas):
        self.pizzas = pizzas

    def servirPizzas(self):
        pass
    
    # consultas
    def getNombre(self) -> str:
        return self.nombre
    
    def getPizzas(self) -> Pizza:
        return self.pizzas
    
    def isEstadoLibre(self)->bool:
        return True
    