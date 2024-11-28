class Cotxe:
    def __init__(self,marca,model,color,kilometraje,tipos):
        self.marca =marca
        self.model=model
        self.color=color
        self.kilometraje = kilometraje
        self.tipos = tipos

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

