from cotxe import Cotxe
from colibri import Colibri
cotxe1 = Cotxe("bmw","serie","rojo",98000,"electric")

print(f"marca: {cotxe1.getMarca()}")        
print(f"el modelo: {cotxe1.getModel()}")        
print(f"El color: {cotxe1.getColor()}")        
print(f"El kilometraje: {cotxe1.getKilometraje()} Km")  
print(f"Tipo: {cotxe1.getTipos()}")      


colibri1 = Colibri("amarillo","pequeño","negros","negro","verde esmeralda")
print()
print(f"el color de colibri: {colibri1.getColor()}")        
print(f"el tamaño del colibri {colibri1.getTamaño()}")        
print(f"el color de los ejos del colibri {colibri1.getColorOjos()}")        
print(f"el color de pico: {colibri1.getPico()}")  
print(f"el color de plumas: {colibri1.getColorPlumas()}")
