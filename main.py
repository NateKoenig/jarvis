import speech_recognition as sr
import webbrowser
import time
import playsound
import os 
import random
from gtts import gTTS
from time import ctime
#from weather import *

r = sr.Recognizer()

def fetchAudio(ask = False):
	with sr.Microphone() as source:
		if ask:
			jarvis_speak(ask)
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		voice_data = ''

		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			jarvis_speak('Sorry, I did not get that')
		except sr.RequestError:
			jarvis_speak('Sorry, my speech service is down')

		return voice_data


def jarvis_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 10000000)
	audio_file = 'audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

def respond(voice_data):
	if 'what is your name' in voice_data:
		jarvis_speak('My name is Jarvis')
	if 'what time is it' in voice_data:
		jarvis_speak(ctime())
	if 'search' in voice_data:
		search = fetchAudio('What do you want to search for?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		jarvis_speak('Here is what I found for ' + search)
	if 'find location' in voice_data:
		location = fetchAudio('What is the location')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		jarvis_speak('Here is the location of ' + location)
	if 'what is the weather' in voice_data:
		weather = fetchAudio('Where do you want the weather for?')
		#url
	if 'exit' in voice_data:
		jarvis_speak('Goodbye sir')
		exit()

time.sleep(1)
jarvis_speak('How can I help you?')
while 1:
	voice_data = fetchAudio()
	respond(voice_data)