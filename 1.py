import random
def devolver_palabra_actual():
    palabra_actual = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_actual += letra
        else:
            palabra_actual += "_"
    return palabra_actual
def juego():
    palabras = ["manzana", "banana", "pera", "uva", "naranja"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")

    while intentos > 0:
        palabra_actual = devolver_palabra_actual()
        print(palabra_actual)
        if "_" not in palabra_actual:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")


    if intentos == 0:
        print("¡Has perdido! La palabra era:", palabra_secreta)

while True
    juego()
    