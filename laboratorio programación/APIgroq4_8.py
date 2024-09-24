import speech_recognition as sr
import requests
import pyttsx3

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Dijiste: {texto}")
            return texto
        except sr.UnknownValueError:
            print("No pude entender lo que dijiste.")
        except sr.RequestError:
            print("No se pudo solicitar resultados del servicio de reconocimiento de voz.")
    return None
def consultar_api(texto):
    url = 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
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "query": texto
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("respuesta", "No se obtuvo una respuesta adecuada.")
    else:
        return "Error al consultar la API de Groq."
def texto_a_audio(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
def main():
    texto = reconocer_voz()
    if texto:
        respuesta = consultar_api(texto)
        print(f"Respuesta de la API: {respuesta}")
        texto_a_audio(respuesta)
