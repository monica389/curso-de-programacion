#ingresando 3 numeros indicar cual es el mayor
def ingreso_un_numero():
    while True:
        numero = input ("ingrese un numero:")
        if numero.isdigit():
            numero = int(numero)
            if numero > 0:
                    break
            else:
                print("Ingrese un numero mayor a 0")
        else:
            print ("El numero ingresado no es valido")  
    return numero  
 
mayor = 0 
menor = 0  
suma = 0      
for contador in range(3):
    numero = ingreso_un_numero()
    print(f"El {contador+1}° N° ingresado es: {numero}")
    if numero > mayor:
       mayor = numero 
    if numero <  menor or menor == 0:
        menor = numero
    suma = suma + numero    

print (f"El numero mayor es {mayor}")
print (f"El numero menor es {menor}")
print (f"El promedio es igual: {suma/3}")
        
mayor = numero
numero_2 = ingreso_un_numero()
if numero_2 > mayor:
    mayor = numero_2
numero_3 = ingreso_un_numero()
if numero_3 > mayor:
    mayor = numero_3

print (f" El Primer numero ingresado es {numero}")
print (f" El Segundo numero ingresado es {numero_2}")
print (f" El Tercer numero ingresado es {numero_3}")
print (f"El numero mayor es")