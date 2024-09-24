# crea una funcion que genere una lista con los primeros 'n' numeros de la secuencia de Fibonacci, donde cada numero es la suma de  los dos anteriores comenzando con el 0 y 1
def fibonacci_iterativo(n):
#Devuelve la secuencia de Fibonacci hasta el enésimo término.
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Ejemplo de uso:
n = 10
resultado = fibonacci_iterativo(n)
print(f"Los primeros {n} términos de la secuencia de Fibonacci son: {resultado}.")

