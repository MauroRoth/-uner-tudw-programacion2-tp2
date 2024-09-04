class Pizza:
    # atributos de clase
    # atributos de instancia
    variedad = str

    # constructor
    def __init__(self,variedad):
        self.variedad = variedad
    
    # comandos
    def setVariedad(self,variedad):
        self.variedad = variedad

    # consultas
    def getVariedad(self):
        return self.variedad
    
