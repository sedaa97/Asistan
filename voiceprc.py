import time
from gtts import gTTS
import speech_recognition as sr
import os

class VoicePrc:
    def __init__(self):
        super(self)

    def konusma(metin):
     sec =len(metin.split())
     tts = gTTS(text=metin, lang='tr')
     tts.save("ses.mp3")
     os.system("ses.mp3")
     time.sleep(sec * 0.8)

    def result(data):
     tts = gTTS(text="tabii. şunu söyledin:" + data +". gitmek istediğin link için dur ya da devam de", lang='tr')
     tts.save("sonuclar.mp3")
     os.system("sonuclar.mp3")
     sec = len(data.split())
     sec = sec + 10
     time.sleep(sec * 0.8)

    def sesalma():
     data = ""
     try:
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         data = r.recognize_google(audio, language='tr-tr')
         data = data.lower()
         return data
     except sr.UnknownValueError:
         raise Exception('This is the exception you expect to handle')

    def listen():
     data = ""
     try:
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.listen(source)
         data = r.recognize_google(audio, language='tr-tr')
         data = data.lower()
         return data
     except sr.UnknownValueError:
         print("Bişey Söylenmedi")
