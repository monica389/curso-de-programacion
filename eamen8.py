# Ejercicio 8: Función para repetir cadenas
# Cantidad de errores: 3

def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado  # Se debe retornar el resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))  # Convertir a entero
print(f"El texto repetido es: {repetir_cadena(texto, repeticiones)}")  # Llamar a la función con argumentos

