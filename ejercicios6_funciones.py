# escriba una funcion que calcule el factorial de un numero dado
def calcular_factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Ejemplo de uso:
numero = 4
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}.")