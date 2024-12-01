class Cotxe:
    def __init__(self,marca,model,color,kilometraje,tipos):
        self.marca =marca
        self.model=model
        self.color=color
        self.kilometraje = kilometraje
        self.tipos = tipos
    # Getters
    def getMarca(self):
        return  self.marca
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def getKilometraje(self):
        return  self.kilometraje
    def getTipos(self):
        return self.tipos
    
   # Setters
    def setMarca(self, marca):
        self.marca = marca

    def setModel(self, model):
        self.model = model

    def setColor(self, color):
        self.color = color

    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def setTipos(self, tipos):
        self.tipos = tipos


