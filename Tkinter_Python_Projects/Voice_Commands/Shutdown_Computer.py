"""
For mac install portaudio
 brew install portaudio

pyaudio:
https://people.csail.mit.edu/hubert/pyaudio/docs/


pyttsx3:
https://pypi.org/project/pyttsx3/
pyttsx3 is a text-to-speech conversion library in Python.


speech recognition:
https://pypi.org/project/SpeechRecognition/
Library for performing speech recognition, with support for several engines and APIs, online and offline.



open mircrophone:
https://pypi.org/project/SpeechRecognition/1.2.3/

pause threshold:
https://stackoverflow.com/questions/56200907/can-i-control-the-start-finish-time-when-i-use-speech-recognition-in-python



steps:

1] import all the libraries
2] input some audio, recognize it and return else return error
    a] assign variable to recognizer class
    b] open microphone
3] create speak function which says what action its going to perform

"""

import pyttsx3
import speech_recognition as sr
import time
import os


# todo: convert voice to text
def take_input():
    # define a variable and assign an instance of recognizer class by calling it.
    recognizer = sr.Recognizer()
    # open microphone of computer
    with sr.Microphone() as source:
        print("Listening")
        recognizer.pause_threshold = 0.8
        # listen for the first phrase and extract it into audio data
        audio = recognizer.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            # print("You said " + recognizer.recognize(audio))
            print("Recognizing")
            query = recognizer.recognize(audio)
            print("You said " + query)
        except LookupError:
            # speech is unintelligible
            print("Could not understand audio")
            return "None"
    # return audio to text
    time.sleep(2)
    return query


# todo: this code will give out voice output
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def main():
    speak("Do you wanT TO SHUTDOWN your computer Shubham? ")
    while True:
        command = take_input()
        if "yes" in command:
            command.speak("Shutting down your computer")
            os.system("shutdown /s /t 30")
            break
        if "no" in command:
            speak(" alright relax, not shutting down you mac. Oh god.")
            break
        speak("say again!!")


if __name__ == '__main__':
    main()
