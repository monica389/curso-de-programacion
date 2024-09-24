class Contador:
def__init__(self):
   self.cuenta = 0    
def incrementar(self).
   self.cuenta += 1       
def decrementar(self):
    if self.cuenta > 0:
    self.cuenta -= 1
else:
        print(f" El contador no puede dar negativo")
def mostrar_contador(self):
    return self.cuenta 
def reiniciar(self):
    self.cuenta = 0 
        
mi_contador = Contador()
mi_contador.incrementar()
print(mi_contador.mostrar_contador())  # Salida: 1 
mi_contador.decrementar()
print(mi_contador.mostrar_contador())  # Salida: 0 mi_contador.decrementar()  # El contador no puede ser negativo.
mi_contador.reiniciar()
        print(mi_contador.mostrar_contador())  # Salida: 0            