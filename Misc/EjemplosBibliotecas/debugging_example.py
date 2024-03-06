import random

class Roscon:
    def __init__(self, radio):
        self.radio = radio
    
    def getDiametro(self):
        diametro = self.radio * 2
        return diametro
    
    def setRadio(self,radio):
        self.radio = radio
    
def instanciaRoscon():
    radio_aleatorio = random.randint(1,100)    # Genera un radio aleatorio para el roscón
    nuevo_roscon = Roscon(radio_aleatorio)     # Instancia el nuevo roscón
    return nuevo_roscon

def creaVariosRoscones(num_roscones): 
    roscones = []                                     # Crea una lista vacía
    for i in range(num_roscones):  
        nuevo_roscon = instanciaRoscon()              # Crea un nuevo roscon
        roscones.append(nuevo_roscon)                 # Lo agrega a la lista.
    return roscones


print("Ingrese el número de roscones a crear:")
num_roscones = int(input())
roscones = creaVariosRoscones(num_roscones)

diametros = []
for r in roscones:
    diametros.append(r.getDiametro())

print("Los diametros de los roscones generados es: ")
print(diametros)