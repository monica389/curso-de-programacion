"""
Nombre y Apellido: 
Edad:
DNI:
Email:
"""

#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre: ") #1-Falta cerrar comillas 3- el nombre de la variable no esta en snake_case
print(f"Hola, {nombre_usuario}! Bienvenido!") #2- Falta darle el formato al print con f 


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
#1- los input devuelven str asi que hay que agregar la funcion int()
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: ")) #2-Faltaba un numero completo

promedio = (num1 + num2 + num3 + num4) / 4 #3-Falta un numero completo 4-El nombre no esta en snake_case, no es una constante #5- Falta encerrar todas las sumas en ()
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 2

calificacion = int(input("Ingrese la calificación del estudiante: ")) #1-Falta agregar un int() ya que el input devuelve str
if calificacion >= 6: #2-Hay que corregir el simbolo de "<=" a ">="
    texto = "El estudiante ha aprobado" #3- Hay que cambiar el print por la declaracion del texto
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
for i in range(len(lista_compras)): #1-Falta agregar el len() para saber cuantos elementos tiene la lista
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 5

class Circulo:
    def __init__(self, radio): #1-Falta agregar el self #5- Corregir el init a __init__
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2 #La formula matematica es Pi por Radio al cuadrado el "** 2" es cuadrado.
            #2- no va radio, va self.radio
mi_circulo = Circulo(5) #3-Esta mal declarado el nombre de la clase
print("El área del círculo es: " ,mi_circulo.calcular_area()) #4-Falta formatear el print


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3

import random #1- Falta el import random
numero = random.randint(1, 10) #2- Esta mal el nombre del metodo es randint
print("El número aleatorio generado es: " , numero) #3- Esta mal declarado el print

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena: #1-Faltan los 2 puntos
    if letra.lower() in vocales: #2-Faltan los () en el .lower
        contador += 1 #3-Falta el +=

print("Número de vocales en la cadena: " ,contador) #4-Falta la , en el print

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado #1-No devuelve nada

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? ")) #2- Hay que convertirlo a entero
print(f"El texto repetido es: {repetir_cadena(texto, repeticiones)}") #3-Faltan los (texto, repeticiones)

#Ejercicio 9: Crear una clase llamada Persona.
#Crea tres instancias de la clase persona:
# Gaspar, 23, Profesor.
# Diego, 45, Desarrollador de Software.
# Tu nombre, tu edad, tu profesion.
# Crea metodos para imprimir el nombre, la edad y la profesion de cada persona.
# Crea un metodo para saber si la persona es mayor o menor de edad.

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Profesion: {self.profesion}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"

persona_1 = Persona("Gaspar", 23, "Profesor")
persona_2 = Persona("Diego", 45, "Desarrollador de Software")
persona_3 = Persona("Fermin", 16, "Estudiante")

persona_1.imprimir()
persona_2.imprimir()
persona_3.imprimir()

print(persona_1.es_mayor_de_edad())
print(persona_2.es_mayor_de_edad())
print(persona_3.es_mayor_de_edad())