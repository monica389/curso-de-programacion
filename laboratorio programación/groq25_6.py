import pyttsx3
import speech_recognition as sr
from groq import Groq
# primero usamos pyttsx3 para saludarnos

client = Groq(
    api_key = "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",
)
pregunta= input("Que te gustaria preguntar")
interaccion_chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pregunta,
        }
    ],
    model="llama3-8b-8192",
)


print(interaccion_chat.choices[0].message.content)
engine = pyttsx3.init()
engine.say("Hola En que puedo ayudarte hoy?")
engine.runAndWait() 
habla =input("Desea escuchar la respuesta? S/N").upper 
escrito =input("Desea escribir la pregunta? S/N").upper

#segundo usamos el peechRecognition para dar nuestro prompt
#inicializar el recognizer

r = sr.Recognizer()
# configura el microfono
whit sr.Microphone() as source:
print("Hable 10 segundos):")


#cuarto obtenemos un resultado por medio de pyttsx3
#print(interaccion_chat.choice[0].message).content
if habla =="s"
   engine.say(interaccion_chat.choice[0].message).content
   engine.runAndwait()