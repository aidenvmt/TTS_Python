import pyttsx3

def decirTexto():    
    texto = str(input("Escribe una frase: "))
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',130)
    
    engine.say(texto)
    engine.runAndWait()   

decirTexto()