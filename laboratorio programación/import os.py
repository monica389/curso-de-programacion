
from groq import Groq

while True:
    contenido =input("A continuacion escribe lo que quieras, sino quieres volver a preguntar pon Q o salir:") capitalize()
    if contenido == "Q" or contenido == "Salir":
        exit("gracias por hablar con nosotros, Hasta la proxima")

cliente = Groq(...
api_key = "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",
)
interaccion_chat= cliente.chat.completions.create(
    messages=[
        {
            "role": "usar",
            "content": contenido,
        }
    ],
    model="llama3-8b-8192",
)

 print(interaccion_chat.choices[0].message.content)