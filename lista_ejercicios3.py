palabras = ["adivinanza","palas","camarero","reloj","tias","celular","reloj"]
print(palabras.count('reloj'))

palabras.reverse()
print(palabras)

palabras = ["adivinanza","palas","camarero","reloj","tias","celular","reloj"]
terminos = ["teclado","curso","operadores","listas"]
lista_concatenada = palabras + terminos
print(lista_concatenada)

palabras = ["adivinanza","palas","camarero","reloj","tias","celular","reloj"]
mitad =len(palabras) // 2
sublista1 = palabras[:mitad]
sublista2 = palabras[mitad]
print(f'sublista 1:{sublista1}')
print(f'Sublista 2:{sublista2}')



