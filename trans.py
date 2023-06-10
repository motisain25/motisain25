import googletrans as googletrans
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("wait for calibration")
    recognizer.adjust_for_ambient_noise(source, 1)
    print("strat speaking")
    audio = recognizer.listen(source)
    print("recorded succefully")
    speech = recognizer.recognize_google(audio)
    speech = speech.lower()
    print(speech)


def trans():
    print("Translating")
    print(googletrans.LANGCODES)
    language = input("type the translation language code").lower()
    translator = googletrans.Translator()
    translation = translator.translate(text=speech, dest=language)
    print("Translation", translation.text)
    engine.setProperty("rate", 120)
    engine.say(translation.pronunciation)
    engine.runAndWait()


trans()
