from os import remove

from playsound import playsound
from gtts import gTTS

def textToSpeech(text, lang):
	voice = gTTS(text, lang=lang)
	filename = "temp.mp3"
	voice.save(filename)
	playsound(filename)
	remove(filename)

user_name = input("Enter your name: ")
textToSpeech(f"Hey {user_name}! How are you doing?", "en")
