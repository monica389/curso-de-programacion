class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
    def calcular_valor_total(self):
        return self.precio * self.cantidad 

producto = Producto("Manzanas", 0.5, 100)
print(f"Valor total inicial: {producto.calcular_valor_total()}")
producto.actualizar_precio(0.6)
producto.actualizar_cantidad(150)
print(f"Valor total actualizado: {producto.calcular_valor_total()}")