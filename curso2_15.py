usuario= input("inresa tu nombre y apellido")
print (f"Hola, {usuario}, bienvenido al Curso de Programacion, a continuacion los capitulos: ")
capitulo = 1
while True:
        print(f"Estás en el capítulo {capitulo}")
        print("¿Qué deseas hacer?")
        print("1. Ir al siguiente capítulo")
        print("2. Abandonar el curso")

        opcion = input("Elige una opción (1 o 2): ")

        if opcion == "1":
            capitulo += 1
            print(f"Avanzando al capítulo {capitulo}...\n")
        elif opcion == "2":
            print("Has decidido abandonar el curso. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, elige 1 o 2.\n")