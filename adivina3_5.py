import random
numero_secreto = random.randint(1,10)
intentos = 0
while intentos < 3:
    intentos =int(input("Adivina el numero entre 1 y 10:"))
    intentos +=1
    if intentos == numero_secreto:
        print(f"¡Correcto! Adivinaste el numero en {intentos} intentos.") 
    elif intentos< numero_secreto:      
        print(" El numero secreto es mayor. Intenta de nuevo.")
    else:
        print("El numero secreto es menor. Intenta de nuevo.")
if intentos == 3 and intentos != numero_secreto:
    print ("f Lo siento,no adivinaste el numero. El numero secreto era {numero_secreto}.")
