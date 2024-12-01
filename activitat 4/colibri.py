class Colibri:
    def __init__(self,color,tamaño,color_ojos,pico,color_plumas):
        self.color =color
        self.tamaño = tamaño
        self.color_ojos = color_ojos
        self.pico=pico 
        self.color_plumas = color_plumas
    # Getters
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
    
     # Setters
    def setColor(self, color):
        self.color = color

    def setTamaño(self, tamaño):
        self.tamaño = tamaño

    def setColorOjos(self, color_ojos):
        self.color_ojos = color_ojos

    def setPico(self, pico):
        self.pico = pico

    def setColorPlumas(self, color_plumas):
        self.color_plumas = color_plumas