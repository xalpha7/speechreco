import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os


a = sr.Recognizer()
b = sr.Recognizer()
print("speak now")
f = open("reply.txt")
x = f.read()
reply = gTTS(text=x,lang='hi',slow=False)
reply.save("reply.wav")
os.system("reply.wav")
with sr.Microphone() as source:
    audio = a.listen(source)
    query = a.recognize_google(audio, language='en')
    print(query)

if 'hello' in b.recognize_google(audio,language='en'):
    print("welcome anurag")
    playsound('reply.wav')