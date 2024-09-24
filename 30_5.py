contador = 0
seguir = True
while seguir == True: 
    valor_usuario = input("Ingrese un valor o ingrese A para finalizar:")
    contador += 1
    if valor_usuario == "A":
        seguir = False
print(f" Se ejecuta correctamente {contador} veces!")        
    