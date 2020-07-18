import pyttsx3
import speech_recognition as spRecog
import wikipedia
import webbrowser
import os
import smtplib
import random
from itertools import islice
from datetime import datetime

# Importing created files
from mWish import *
from lmWish import *
from anWish import *
from eWish import *
from leWish import *
from nWish import *
from lnWish import *
from emWish import *
from listenError import *

maleVoice = 0
femaleVoice = 1
randomMin = 0
randomMax = 3

class Initialisation:
	# Constructor
	def __init__(self):
		# Intialising the voice engine and retrieving default values
		# rate = 200
		# volume = 1.0
		self.voiceEngine = pyttsx3.init()
		voices = self.voiceEngine.getProperty('voices')
		rate = self.voiceEngine.getProperty('rate')
		volume = self.voiceEngine.getProperty('volume')

		# Initialising other pages
		self.mWish = Morning()
		self.lmWish = LateMorning()
		self.anWish = Afternoon()
		self.eWish = Evening()
		self.leWish = LateEvening()
		self.nWish = Night()
		self.lnWish = LateNight()
		self.emWish = EarlyMorning()
		self.listenError = ListenError()

		# To check all existing voices on the device
		'''
		for voice in voices:
			print(voice, voice.id)
			print(rate)
			print(volume)
			voiceEngine.setProperty('voice', voice.id)
			print("Initialising IRIS")
			voiceEngine.say("Initialising IRIS")
			voiceEngine.runAndWait()
			voiceEngine.stop()
		'''

		# Setting new values to the voice engine
		new_rate = 150
		self.voiceEngine.setProperty('rate', new_rate)
		self.voiceEngine.setProperty('voice', voices[femaleVoice].id)
		print("Initialising IRIS")
		self.speak("Initialising IRIS")
		self.wish()
		self.listen()

	# Function that handles speaking
	def speak(self, _text_):
		self.voiceEngine.say(_text_)
		self.voiceEngine.runAndWait()

	# Function that handles listening
	def listen(self):
		voice_recogniser = spRecog.Recognizer()
		with spRecog.Microphone() as audio_source:
			print("Listening")
			audio = voice_recogniser.listen(audio_source)

		try:
			print("Analysing")
			audio_query = spRecog.recognize_google(audio)
			print(audio_query)

		except Exception as e:
			self.speak(list(islice(self.listenError.request, 1)))
			#self.listen()

	# Function that handles wishing
	def wish(self):
		_hour_ = int(datetime.now().hour)
		print(_hour_)
		count = random.randint(randomMin, randomMax)

		# Conditions for wishing
		if(_hour_ >= 6 and _hour_ < 9):
			print("Morning wishes")
			self.speak(list(islice(self.mWish.wishes, 1)))
		elif(_hour_ >= 9 and _hour_ < 12):
			print("Late morning wishes")
			self.speak(list(islice(self.lmWish.wishes, 1)))
		elif(_hour_ >= 12 and _hour_ < 15):
			print("Afternoon wishes")
			self.speak(list(islice(self.anWish.wishes, 1)))
		elif(_hour_ >= 15 and _hour_ < 18):
			print("Evening wishes")
			self.speak(list(islice(self.eWish.wishes, 1)))
		elif(_hour_ >= 18 and _hour_ < 21):
			print("Late evening wishes")
			self.speak(list(islice(self.leWish.wishes, 1)))
		elif(_hour_ >= 21 and _hour_ < 24):
			print("Night wishes")
			self.speak(list(islice(self.nWish.wishes, 1)))
		elif(_hour_ >= 0 and _hour_ < 4):
			print("Wishes with bed references")
			self.speak(list(islice(self.lnWish.wishes, 1)))
		elif(_hour_ >= 4 and _hour_ < 6):
			print("Early morning wishes")
			self.speak(list(islice(self.emWish.wishes, 1)))