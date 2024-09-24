# Crear una lista vacía
mi_lista = []

# Agregar 5 elementos usando append
mi_lista.append(10)
mi_lista.append(20)
mi_lista.append(30)
mi_lista.append(40)
mi_lista.append(50)

# Imprimir la longitud de la lista
print("Longitud de la lista:", len(mi_lista))

# Eliminar el último elemento usando pop
mi_lista.pop()

# Eliminar un elemento específico usando remove
mi_lista.remove(20)

# Imprimir la lista final usando un for
print("Lista final:")
for elemento in mi_lista:
    print(elemento)