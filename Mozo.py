from Pizza import Pizza

class Mozo:
    # atributos de clase

    # método de inicialización
    def __init__(self,nombre):
        # atributos de instancia
         self.nombre = nombre
         self.pizzas = list()
       
    # comandos
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def tomarPizzas(self,pizzas):
        # requiere pizzas ligado
        i=0
        while self.isEstadoLibre() and len(pizzas)>len(self.pizzas):
            self.pizzas.append(pizzas[i])
            i+=1

    def servirPizzas(self):
        self.pizzas.clear()
    
    # consultas
    def getNombre(self) -> str:
        return self.nombre
    
    def getPizzas(self) -> Pizza:
        return self.pizzas
    
    def isEstadoLibre(self)->bool:
        if len(self.pizzas)<2:
            return True
        return False
    