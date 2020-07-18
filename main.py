import os

try:
	import pyttsx3
except ImportError:
	os.system("pip install pyttsx3")
	import pyttsx3

try:
	import speech_recognition
except ImportError:
	os.system("pip install speechRecognition")
	import speech_recognition

try:
	import wikipedia
except ImportError:
	os.system("pip install wikipedia")
	import wikipedia

try:
	import webbrowser
except ImportError:
	os.system("pip install webbrowser")
	import webbrowser

try:
	import pythoncom
except ImportError:
	os.system("pip install pywin32")
	os.system("pip install pypiwin32")
	import pythoncom

try:
	import itertools
except ImportError:
	os.system("pip install more-itertools")
	os.system("pip install itertools-s")
	import itertools

try:
	import pipwin
except ImportError:
	os.system("pip install pipwin")
	import pipwin

#os.system("pipwin install pyaudio")

import smtplib
from datetime import datetime
from Initialisation import *

if __name__ == "__main__":
	_init_ = Initialisation()