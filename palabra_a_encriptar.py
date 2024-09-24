palabra_a_encriptar= input("Escriba para encriptar en formato Cesar:")
lista_abecedario = [ "a","b","c","d","e","f","g","h","i", "j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
lista_palabra = list (palabra_a_encriptar)
lista_indice = []
indice =0
palabra_encriptada = []
print (lista_palabra)
for palabra in lista_palabra:
    indice= lista_abecedario.index(palabra)
    lista_indice.append(indice+desplazamiento)
    for numero in lista_indice:
        palabra_encriptada.append(lista_abecedario[numero])
salida =  ",".join(palabra_encriptada)
print(salida)