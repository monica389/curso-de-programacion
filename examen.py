#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
Nombre= input ("Ingrese su nombre"):
print("Hola, {Nombre}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num3 = input("Ingrese el tercer numero: ")

PROMEDIO = num1 + num2 + num3 / 3
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 3

calificacion = input("Ingrese la calificación del estudiante: ")
texto = "El estudiante ha aprobado"
if calificacion >= 6:
    print(texto)
else:
    texto= "El estudiante ha reprobado"
print(texto)

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(lista_compras):
    print("- " + lista_compras[i])

Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5
print("El número aleatorio generado es: " + numero)#

class Circulo:
    def_init_(radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.

Mi_circulo = Circulo(5)
print("El área del círculo es: " mi_circulo.calcular_area())


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
numero = random.randit(1, 10)

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena
    if letra.lower in vocales:
        contador + 1

print("Número de vocales en la cadena: " contador)

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return 

texto = input("Ingrese un texto: ")
repeticiones = input("¿Cuántas veces desea repetir el texto? ")
print(f"El texto repetido es: {repetir_cadena}")

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.