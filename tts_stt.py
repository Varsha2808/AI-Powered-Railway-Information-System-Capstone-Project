import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    # Get available voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # break
    engine.say(command, )
    engine.runAndWait()


try:
	with sr.Microphone() as source2:
		r.adjust_for_ambient_noise(source2, duration=0.2)
		audio2 = r.listen(source2)
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()
		print("Did you say ",MyText)
		SpeakText(f"Did you Say, {MyText}")
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
	print("unknown error occurred")