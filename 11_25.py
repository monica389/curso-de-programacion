numero_aleatorio = 3
eligio = 3
salio = 3
numero_aleatorio = random.randit (1,3)

if numero_aleatorio ==1: 
    salio = "PIEDRA"
if numero_aleatorio ==2:
    salio = "PAPEL"
if numero_aleatorio ==3
   salio = "TIJERA"
   print("")
print("#"*40)
print("######                                                                    ######")
print("######                 Bienvenido al juego de                             ###### ")
print("######                TIEDRA - PAPEL O TIJERA  😛🚀                       ###### ")
print("######                                                                    ######")
print("######            INGRESE 1 SI QUIERE ELEGIR PIEDRA                       ######")
print("######            INGRESE 2 SI QUIERE ELEGIR PAPEL                        ######")
print("######            INGRESE 3 SI QUIERE ELEGIR TIJERA                       ######")
print("######                                                                    ######")
print("#"*40)
print("")

numero_ingresado = input ("Ingrese un numero entre el 1 y el 3: ")
if numero_ingresado.isdigit():
   numero_ingresado = int(numero_ingresado)
else:   
    print("#"*50)
    print("######                                                ######")
    print("######       NO INGRESO UN DATO CORRECTO  😛🚀        ###### ")
    print("######            FIN DEL JUEGO                       ######")
    print("######                                                ######")
    print("#"*50)
    print("")
    print("")
    exit()

if numero_ingresado == 1:
    eligio = "PIEDRA"
if numero_ingresado == 2:
    eligio = "PAPEL "
if numero_ingresado == 3:
    eligio = "TIJERA"

print (eligio)

if numero_ingresado == numero_aleatorio: 
    print("#"*30)
    print("######                                                                    ######")
    print(f"######       EMPATARON AMBOS ELIGIERO {salio}  😛🚀                        ###### ")
    print("######                                                                    ######")
    print("#"*30)
    print("")    

if numero_ingresado == 0 or numero_ingresado >= 11:
    print("#"*60)
    print("######                                                ######")
    print("######       NO INGRESO UN DATO CORRECTO  😛🚀        ###### ")
    print("######            FIN DEL JUEGO                       ######")
    print("######                                                ######")
    print("#"*60)
    print("")
    print("")
    exit()

if numero_aleatorio == 1  and  numero_ingresado == 2: 
    print("#"*40)
    print("######                                                ######")
    print("######           ¡¡A GANDADO!! 🤗👌👏                 ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*40)
    print("")   

if numero_aleatorio == 1 and  numero_ingresado== 3: 
    print("#"*50)
    print("######                                                ######")
    print("######           ¡¡A PERDIDO!! 😤                     ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*50)
    print("")   

if numero_aleatorio == 2 and  numero_ingresado == 3: 
    print("#"*60)
    print("######                                                ######")
    print("######           ¡¡A GANDADO!! 🤗👌👏                 ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*60)
    print("")     

if numero_aleatorio == 2 and  numero_ingresado == 1: 
    print("#"*60)
    print("######                                                ######")
    print("######           ¡¡A PERDIDO!! 😤                     ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*60)
    print("") 

if numero_aleatorio == 3 and  numero_ingresado == 1: 
    print("#"*60)
    print("######                                                ######")
    print("######           ¡¡A GANDADO!! 🤗👌👏                 ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*60)
    print("")   
if numero_aleatorio == 3 and  numero_ingresado == 2: 
    print("#"*60)
    print("######                                                ######")
    print("######           ¡¡A PERDIDO!! 😤                     ###### ")
    print(f"######        USTED ELIGIO {eligio}                     ###### ")
    print(f"######        Y LA MAQUINA ELIGIO {salio}              ###### ")
    print("######                                                ######")
    print("#"*60)
    print("") 
