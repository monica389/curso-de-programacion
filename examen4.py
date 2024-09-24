lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item.lower() == 'salir':  # Convierte a minúsculas para evitar problemas con mayúsculas
        break
    lista_compras.append(item)

print("Lista de compras:")
for item in lista_compras:  # Iterar directamente sobre la lista
    print(f"- {item}")