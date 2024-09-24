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