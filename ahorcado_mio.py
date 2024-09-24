import random
def elegir_palabra():
    palabras = ['python', 'ahorcado', 'programacion', 'desarrollador', 'inteligencia', 'artificial']
    return random.choice(palabras)

def mostrar_estado(actual, intentos):
    print("\nPalabra:", " ".join(actual))
    print(f"Intentos restantes: {intentos}")

def juego_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = ['_'] * len(palabra_secreta)
    intentos = 8
    letras_usadas = set()

    print("¡Bienvenido al juego del ahorcado!")

    while intentos > 0 and '_' in letras_adivinadas:
        mostrar_estado(letras_adivinadas, intentos)
        letra = input("Adivina una letra: ").lower()

        if letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            continue

        letras_usadas.add(letra)

        if letra in palabra_secreta:
            for i, l in enumerate(palabra_secreta):
                if l == letra:
                    letras_adivinadas[i] = letra
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra.")

    if '_' not in letras_adivinadas:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("\nLo siento, te has quedado sin intentos. La palabra era:", palabra_secreta)
