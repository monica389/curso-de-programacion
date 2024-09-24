def sumar(numero_1: int, numero_2: int)->int:
    return numero_1 + numero_2
print(sumar)
#import funciones_sumar as fs


#funcion para validar un texto
(#texto_input:str|none)
def validar_texto()-> str:
    while True:
        texto= input("ingrese un texto") #
        if not texto.isdigit():
            break
        else:
            print("Ingrese un texto valido")
    return texto
textoimprimir = validar_texto() (# ingrese nombre y apellido)
print(f"el texto ingresado es:{textoimprimir}")       
