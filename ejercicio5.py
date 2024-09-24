import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2  # Usamos math.pi para obtener el valor de Pi

# Crear una instancia de la clase Círculo
mi_circulo = Circulo(5)

# Imprimir el área del círculo
print("El área del círculo es:", mi_circulo.calcular_area())
