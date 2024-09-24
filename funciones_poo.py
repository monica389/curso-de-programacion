class Rectangulo: 
    def _init_ (self, alto, ancho):
        self.alto = alto
        self.ancho = ancho  
    def mostrar_caracteristicas(self):
        print(f"el rectangulo tiene un ancho {self.ancho}  y un alto {self.alto}")
        return
    def area(self):
        area = self.alto * self.ancho
        print(f" el area es {area}")
        return 
    def perimetro(self):
        perimetro= self.lado*2 + self. lado*2
        print(f" el perimetro es {perimetro}")
        return  (self.alto + self.ancho)
mi_Rectangulo = area (10,25)
mi_Rectangulo.mostrar_caracteristicas()


rectangulo_1 = Rectangulo()
rectangulo_1.mostrar_caracteristicas()
rectangulo_1.area()
rectangulo_1.perimetro()
