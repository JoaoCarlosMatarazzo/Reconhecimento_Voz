import speech_recognition as sr
#Usando a Biblioteca SpeechRecognition

# Inicializa o reconhecedor de fala
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Ajustando ruído ambiente... Por favor, aguarde.")
    recognizer.adjust_for_ambient_noise(source)
    print("Diga algo!")
    audio = recognizer.listen(source)

try:
    print("Você disse: " + recognizer.recognize_google(audio, language='pt-BR'))
except sr.UnknownValueError:
    print("Não foi possível entender o áudio")
except sr.RequestError as e:
    print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")





