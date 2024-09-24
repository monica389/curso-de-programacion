# funcion verificar si un numero es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = 7
resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}.")