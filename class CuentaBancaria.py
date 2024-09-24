class Cuenta_bancaria:
   def __init__(self, titular, saldo inicial = 0):
      self.titular = titular
      self.saldo = saldo_inicial pass
   def deposito(self, monto):
      if monto > 0:
         self.saldo += monto
      print(f" Has depositado{monto} pesos. Saldo actual: {self.saldo} pesos") 
   def retirar(self, monto):
      if monto > 0:
         if monto <= self.saldo:
            self.saldo -= monto
            print(f" Has retirado{monto} unidades. Saldo actual{self.saldo}") 
         else:
          print("Tienes fondos insuficientes para realizar la operación")
   def consultar_saldo(self):
      print(f"Saldo actual: {self.saldo} unidades")            
      
      
      
titular = input("Ingrese el nombre del titular:")
cuenta_Bancaria = CuentaBancaria(titular)
while True:
    opcion = input("Elije la opcion que quieres realizar:\n-Depositar (D) \n-Retirar(R)\n-Mostrar Saldo (S)\n-Si quieres finalizar sesion (F) \n-Opcion:").upper()
    if opcion == "D" or opcion == "R" or opcion == "S" or opcion == "F":
        if opcion == "D":
            cuenta_bancaria.depositar()
        if opcion == "R":
            cuenta_bancaria.retirar()
        if opcion == "S":
            cuenta_bancaria.mostrar_saldo()
        if opcion == "F":
            cuenta_bancaria.mostrar_saldo()
            exit("Finalizando Sesion con Exito")
    else:
        print("Ingresaste una opcion incorrecta (D,R,S,F)")
        print("\n"*10)
   

