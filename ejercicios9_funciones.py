#generar una funcion  que permita el ingreso de la cantidadde numeros aleatorios a generar y los muestre.
import random 
def generar_numeros_aleatorios(cantidad):
    numeros_aleatorios = [random.randint(0, 100) for _ in range(cantidad)]
    print(f"Se han generado {cantidad} números aleatorios:")
    for numero in numeros_aleatorios:
        print(numero)
# Ejemplo de uso
cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
generar_numeros_aleatorios(cantidad)