usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}
def login():
    intentos = 3
    while intentos > 0:
        usuario = input("Ingresa tu nombre de usuario: ")
        contraseña = input("Ingresa tu contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("¡Login exitoso!")
            return True
        else:
            intentos -= 1
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intentos.")
    print("Número máximo de intentos alcanzado. Acceso denegado.")
