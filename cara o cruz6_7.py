import random

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def jugar_contra_computadora():
    eleccion_usuario = input("Elige 'Cara' o 'Cruz': ").capitalize()
    resultado = lanzar_moneda()
    print(f"La moneda cayó en {resultado}.")
    if eleccion_usuario == resultado:
        print("¡Felicidades, ganaste!")
    else:
        print("Lo siento, perdiste.")

def jugar_contra_amigo():
    # Pide el nombre de los jugadores
    nombre_jugador1 = input("Introduce el nombre del primer jugador: ")
    nombre_jugador2 = input("Introduce el nombre del segundo jugador: ")
    
    eleccion_jugador1 = input(f"{nombre_jugador1}, elige 'Cara' o 'Cruz': ").capitalize()
    eleccion_jugador2 = "Cruz" if eleccion_jugador1 == "Cara" else "Cara"
    
    print(f"{nombre_jugador2}, te queda '{eleccion_jugador2}'.")
    
    resultado = lanzar_moneda()
    print(f"La moneda cayó en {resultado}.")
    
    if eleccion_jugador1 == resultado:
        print(f"¡Felicidades {nombre_jugador1}, ganaste!")
    else:
        print(f"¡Felicidades {nombre_jugador2}, ganaste!")

def main():
    print("Bienvenido al juego de Cara o Cruz.")
    print("Elige una opción:")
    print("1. Jugar contra la computadora")
    print("2. Jugar contra un amigo")
    
    opcion = input("Introduce el número de tu elección: ")
    
    if opcion == "1":
        jugar_contra_computadora()
    elif opcion == "2":
        jugar_contra_amigo()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()