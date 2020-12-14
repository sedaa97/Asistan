import time
import speech_recognition as sr
import os
from bs4 import BeautifulSoup
import requests
import webbrowser
from voiceprc import VoicePrc
from googlesearch import search


class Main:
    def __init__(self):
        self.program()

    def sesMetin(self):
        while 1==1:
            try:
                word = VoicePrc.sesalma()
                return word
            except Exception as err:
                VoicePrc.konusma("Anlayamadım, lütfen tekrar söyle")

    def textOku(self,parag):
        for j in parag:
            if j.text.strip():
                sentences = j.text.split('.')
                for sen in sentences:
                    print(sen)
                    VoicePrc.konusma(sen)
                    time.sleep(1)
                    kom = VoicePrc.listen()
                    print(kom)
                    if kom == "okumayı bitir":
                        return
            VoicePrc.konusma("Paragraf bitti. Sonraki paragraf okunsun mu")
            while 1 == 1:
                komut = self.sesMetin()
                komut = komut.lower()
                if komut == "okunsun":
                    break
                elif komut == "hayır bitir":
                    return
                else:
                    VoicePrc.konusma("Yanlış komut, lütfen tekrar söyle")
                    continue

    def paragOku(self,sonuc):
        url = sonuc
        rm = requests.get(url)
        soup = BeautifulSoup(rm.content, 'html.parser')
        baslik = soup.find_all("h1")
        paragraf = soup.find_all("p")
        for i in baslik:
            print(i.text)
            VoicePrc.konusma(i.text)
            VoicePrc.konusma("Paragraf Okunsun mu")

            while 1 == 1:
                komut = self.sesMetin()
                komut = komut.lower()
                print(komut)
                if komut == "okunsun":
                    if len(paragraf) != 0:
                        self.textOku(paragraf)
                        time.sleep(1)
                        VoicePrc.konusma("Anlatacaklarım bu kadar. Başka birşey aramak ister misin")
                        komut = self.sesMetin()
                        komut = komut.lower()
                        if komut == "evet istiyorum":
                            self.program()
                        elif komut == "hayır istemiyorum":
                            VoicePrc.konusma("Program sonlanıyor kendine iyi bak")
                            quit(0)
                        else:
                            VoicePrc.konusma("Yanlış komut, lütfen tekrar söyle")
                            continue
                    else:
                        VoicePrc.konusma("Bu sayfanın yapısını anlayamadım")
                elif komut == "hayır":
                    VoicePrc.konusma("Anlatacaklarım bu kadar. Başka birşey aramak ister misin")
                    komut = self.sesMetin()
                    komut = komut.lower()
                    if komut == "evet istiyorum":
                        self.program()
                    elif komut == "hayır istemiyorum":
                        VoicePrc.konusma("Program sonlanıyor")
                        quit(0)
                    else:
                        VoicePrc.konusma("Yanlış komut, lütfen tekrar söyle")
                        continue
                else:
                    VoicePrc.konusma("Yanlış komut, lütfen tekrar söyle")
                    continue

    def program(self):
        VoicePrc.konusma("ben DeepTone. Ne öğrenmek istiyorsun")
        time.sleep(2)
        word = ""
        word = self.sesMetin()
        word = word.lower()
        VoicePrc.konusma("tabii.şunu söyledin:" + word + "." + "onaylıyor musun?")
        time.sleep(2)
        data = self.sesMetin()
        data = data.lower()
        while 1 == 1:
            if (data == "onaylıyorum"):
                break
            else:
                VoicePrc.konusma("Üzgünüm lütfen ne öğrenmek istediğini tekrar eder misin")
                word = self.sesMetin()
                word = word.lower()
                VoicePrc.konusma("tabii.şunu söyledin:" + word + "." + "onaylıyor musun?")
                time.sleep(1)
                data = self.sesMetin()
                data = data.lower()

        for sonuclar in search(word, stop=30):

            if (sonuclar.startswith("http://")):
                rep_sonuclar = sonuclar.replace("http://", "")
            elif (sonuclar.startswith("https://")):
                rep_sonuclar = sonuclar.replace("https://", "")

            print(sonuclar)
            size = rep_sonuclar.find("/")
            VoicePrc.konusma(rep_sonuclar[0:size])
            time.sleep(6)

            while 1==1:
                yazdır = self.sesMetin()
                print(yazdır)
                if "linke tıkla" in yazdır:
                    VoicePrc.konusma("Başlık Okunuyor")
                    webbrowser.open(sonuclar)
                    self.paragOku(sonuclar)


                    break

                elif yazdır == "devam et":
                    break
                else:
                    VoicePrc.konusma("Yanlış tercih, lütfen tekrar söyle")
                    continue



main = Main()
