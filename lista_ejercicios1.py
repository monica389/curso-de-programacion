lista_nombres =["javier","maricel","monica","paula","gaspar","leticia","florencia"]
print("Longitud de la lista:", len(lista_nombres))

lista_nombres.append("carlos")
print("Lista después de agregar un nuevo nombre:", lista_nombres)

lista_nombres.pop(0)
print("Lista después de eliminar el primer nombre:", lista_nombres)

nombre_a_buscar = "paula"
if nombre_a_buscar in lista_nombres:
    print(f" el nombre {nombre_a_buscar} está presente en la lista.")
else:
    print(f" el nombre {nombre_a_buscar} no está presente en la lista.")
    
lista_nombres.sort()
print("lista ordenada alfabeticamente:" ,lista_nombres)