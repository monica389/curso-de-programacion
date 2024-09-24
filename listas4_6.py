productos = ["manzanas","pan","leche","huevos","zapallo","lechuga"]
nuevo_producto = "queso"
productos.append(nuevo_producto)
producto_a_eliminar = "pan"
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
print("lista de productos actualizada",productos)
