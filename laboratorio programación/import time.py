import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices = engine.getProperty('voices')
hora_alarma = input("Ingrese la hora de la alarma (HH:MM): ")
while True:
    hora_actual = datetime.now() 
    hora_alarma_str = hora_alarma.strftime('%H:%M:%S')
    hora_actual_str = hora_actual.strftime('H:%M:%S')
    if hora_actual_str ==hora_alarma_str:
        print("¡Hora de levantarse!")
        engine.say("A levantarse dijo la rana mientras espiaba por la ventana")
        engine.runAndWait()
        break
    time.sleep(1) #Espera 1 segundo antes de volver a verificar