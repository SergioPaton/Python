class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas ):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def __str__(self):
          return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

p = Coche("Rojo", 4, 5, 120, 150)
print(p)