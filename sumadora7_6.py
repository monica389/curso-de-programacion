suma_total = 0
print("Introduce un numero para sumar. Ingresa 0 para finalizar.")
while True :
    numero =int(input("Introduce un numero: "))
    if numero == 0:
        break
    suma_total += numero
print(f"La suma total de los numeros ingresados es: {suma_total}")
