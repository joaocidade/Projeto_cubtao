import speech_recognition as sr

# utilizar a biblioteca pyaudio para capturar o áudio e a SpeechRecognition para reconhecer o áudio
def reconhecer_fala():
    reconhecedor = sr.Recognizer()  
    with sr.Microphone() as source:  
        reconhecedor.adjust_for_ambient_noise(source)
        print("Diga algo...")
        try:
            audio = reconhecedor.listen(source) 
            frase = reconhecedor.recognize_google(audio, language='pt-BR')  # Reconhece o áudio
            print("Você disse: " + frase)
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            frase = ""
        except sr.RequestError as e:
            print(f"Erro na API do Google: {e}")
            frase = ""
        return frase

# Chama a função
reconhecer_fala()
