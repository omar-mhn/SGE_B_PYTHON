from cotxe import Cotxe
from colibri import Colibri
# instàncies de Cotxe
cotxe1 = Cotxe("bmw","serie","rojo",98000,"electric")
# Mostrar getters de Cotxe
print(f"marca: {cotxe1.getMarca()}")        
print(f"el modelo: {cotxe1.getModel()}")        
print(f"El color: {cotxe1.getColor()}")        
print(f"El kilometraje: {cotxe1.getKilometraje()} Km")  
print(f"Tipo: {cotxe1.getTipos()}")      

# instàncies de Colibrí.
colibri1 = Colibri("amarillo","pequeño","negros","negro","verde esmeralda")
#Mostrar getters de Colibrí 

print()
print(f"el color de colibri: {colibri1.getColor()}")        
print(f"el tamaño del colibri {colibri1.getTamaño()}")        
print(f"el color de los ejos del colibri {colibri1.getColorOjos()}")        
print(f"el color de pico: {colibri1.getPico()}")  
print(f"el color de plumas: {colibri1.getColorPlumas()}")
#Modificar atributs de Cotxe a través dels setters

cotxe1.setMarca("Mercedes")
cotxe1.setModel("Class A")
cotxe1.setColor("Negro")
#Mostrar els  atributs modificats a través dels getters
print()
print(f"marca: {cotxe1.getMarca()}")        
print(f"el modelo: {cotxe1.getModel()}")        
print(f"El color: {cotxe1.getColor()}")
#Modificar  atributs de Colibrí a través dels setters
colibri1.setColor("Rojo")
colibri1.setTamaño("Mediano")
colibri1.setColorOjos("Azul")
#Mostrar els  atributs modificats a través dels get
print()
print(f"el color de colibri: {colibri1.getColor()}")        
print(f"el tamaño del colibri {colibri1.getTamaño()}")        
print(f"el color de los ejos del colibri {colibri1.getColorOjos()}")