class Pizza:
    # atributos de clase

    # método de inicialización
    def __init__(self,variedad):
        # atributos de instancia
        self.variedad = variedad
    
    # comandos
    def setVariedad(self,variedad):
        self.variedad = variedad

    # consultas
    def getVariedad(self):
        return self.variedad
    
