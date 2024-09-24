cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:  # Falta dos puntos al final de la línea
    if letra.lower() in vocales:  # Se debe usar paréntesis para llamar a lower()
        contador += 1  # Se debe usar += para incrementar el contador
print("Numero de vocales en la cadena:", contador)