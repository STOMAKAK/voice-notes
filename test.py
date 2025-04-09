import speech_recognition as sr
mic = sr.Microphone()
recog = sr.Recognizer()

with mic as audio_file:
    print("Скажи что-нибудь")
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    text = recog.recognize_google(audio, language="ru-RU")
    print("Результат:", text)