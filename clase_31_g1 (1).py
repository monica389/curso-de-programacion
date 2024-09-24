#Objetivo: Implementar una clase CuentaBancaria 
#que permita a los usuarios realizar operaciones bancarias básicas 
#como depositar, retirar y consultar el saldo.

import funciones as fp

class CuentaBancaria:
    def __init__(self, titular:str | None = "", saldo_inicial: float | None = 0):
      self.titular = titular
      self.saldo = saldo_inicial
      pass
      
    def consultar_saldo(self):
        print("\n"*2)
        print(f"{self.titular} su saldo actual: {self.saldo} pesos") 
        print("\n"*2)
        return           
      
    def depositar (self):
        print("\n"*2)
        deposito = fp.ingresar_numero("Ingrese el importe a depositar: ")
        if deposito > 0:
            self.saldo = self.saldo + deposito
            print ("Gracias por utilizar nuestros servicios")
            self.consultar_saldo()
            return self.saldo   
    
    def retirar(self):
        print("\n"*2)
        retiro = fp.ingresar_numero("Ingrese el importe a retirar: ")
        if retiro <= self.saldo:
            self.saldo = self.saldo - retiro
            print ("Gracias por utilizar nuestros servicios")
            self.consultar_saldo()
            return self.saldo 
        else:
          print("Tienes fondos insuficientes para realizar la operación")
          self.consultar_saldo()
          
print("\n"*4)
titular = input ("Ingrese el nombre del titular: ")
print("\n"*2)
caja_ahorro= CuentaBancaria(titular , 0)

while True:
    opcion = input("Elije la opcion que quieres realizar:\n-Depositar (D) \n-Retirar(R)\n-Mostrar Saldo (S)\n-Si quieres finalizar sesion (F) \n-Opcion:").upper()
    if opcion == "D" or opcion == "R" or opcion == "S" or opcion == "F":
        if opcion == "D":
            caja_ahorro.depositar()
        if opcion == "R":
            caja_ahorro.retirar()
        if opcion == "S":
            caja_ahorro.consultar_saldo()
        if opcion == "F":
            caja_ahorro.consultar_saldo()
            exit("Finalizando Sesion con Exito")
    else:
        print("Ingresaste una opcion incorrecta (D,R,S,F)")
        print("\n"*10)