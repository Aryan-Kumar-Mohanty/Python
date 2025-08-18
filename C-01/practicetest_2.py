import pyttsx3
engine = pyttsx3.init()
x =input("what do u want the bot to say:")
engine.say(x )
engine.runAndWait()