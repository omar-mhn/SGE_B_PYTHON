class Colibri:
    def __init__(self,color,tamaño,color_ojos,pico,color_plumas):
        self.color =color
        self.tamaño = tamaño
        self.color_ojos = color_ojos
        self.pico=pico 
        self.color_plumas = color_plumas

    def getColor(self):
        return self.color
    def getTamaño(self):
        return self.tamaño
    def getColorOjos(self):
        return self.color_ojos
    def getPico(self):
        return self.pico
    def getColorPlumas(self):
        return self.color_plumas
