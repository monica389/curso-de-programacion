import pyttsx3
engine= pyttsx3.init()
hablar = input("escribe lo que quieras que diga")
engine.say(hablar) 
voice= engine.getProperty('voices')
for i,voice in enumerate(voice):
    print(f"{i}. {voice.name} ({voice.languages})") 
engine.setProperty('rate', 300)
engine.setProperty("voice,voices[1].id")



