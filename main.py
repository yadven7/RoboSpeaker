# import pyttsx3
#
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1. created by Yadvendra")
#     x = input("Enter What you want me to speak: ")
#
#     engine = pyttsx3.init()
#     engine.say(x)
#     engine.runAndWait()
#
import pyttsx3

print("Welcome to RoboSpeaker 1.1. created by Yadvendra")

engine = pyttsx3.init("sapi5")
text = input("Enter What you want me to speak: ")

engine.say(text)
engine.runAndWait()