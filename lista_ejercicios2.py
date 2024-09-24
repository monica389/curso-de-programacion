numeros =[1,2,3,4,5,6,7]
suma =sum(numeros)
print("la suma de todos los numeros de la lista es:",suma)

maximo =max(numeros)
minimo =min(numeros)
print("El numero maximo de la lista es:",maximo)
print("El numero minimo de la lista es:",minimo)

numeros_multiplicados =[num *2 for num in numeros]
print("Lista de numeros multiplicados por dos:", numeros_multiplicados)

for numero in numeros:
    if numero %2 == 0:
        print( numero)