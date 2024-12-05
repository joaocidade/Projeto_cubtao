import speech_recognition as sr

def reconhecer_fala():
    reconhecedor = sr.Recognizer()  # Instância do reconhecedor
    with sr.Microphone() as source:  # Uso correto de Microphone
        reconhecedor.adjust_for_ambient_noise(source)
        print("Diga algo...")
        try:
            audio = reconhecedor.listen(source)  # Captura o áudio
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
