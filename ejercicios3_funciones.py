# Crea una función para ordenar una lista de palabras
def ordenar_palabras(lista_palabras):
    return sorted(lista_palabras)
palabras = ["manzana", "naranja", "banana", "kiwi", "fresa"]
palabras_ordenadas = ordenar_palabras(palabras)
print("Palabras ordenadas:", palabras_ordenadas)