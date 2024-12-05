from gtts import gTTS
import sounddevice as sd
import soundfile as sf

# Solicita o texto do usuário
print("Digite o texto que deseja falar:")
texto = input()

# Converte o texto em fala
text = gTTS(texto, lang='pt')  # Corrigida a capitalização e o argumento `lang`
text.save("myvoz.mp3")

# Lê o arquivo de áudio gerado
filename = 'myvoz.mp3'
data, fs = sf.read(filename, dtype='int16')

# Reproduz o áudio
sd.play(data, fs)
status = sd.wait()  # Aguarda o áudio terminar

print("Áudio reproduzido com sucesso!")
