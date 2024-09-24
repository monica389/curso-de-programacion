def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return self.alto * self.ancho

    def perimetro(self):
        return 2 * (self.alto + self.ancho)

# Ejemplo de uso
rectangulo = Rectangulo(5, 10)
print("Área:", rectangulo.area())           
print("Perímetro:", rectangulo.perimetro())