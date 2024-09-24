class circulo:
    def __init__(self,radio):
        self.radio = radio 
    def calcular_area(self):
        return 31416 * self.radio ** 2

mi_circulo = circulo(5)
print(f"El area del circulo es: {mi_circulo.calcular_area()}")
# este ejercicio esta perfecto
