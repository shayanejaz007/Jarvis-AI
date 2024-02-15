import speech_recognition as sr
import pyttsx3
import os
import openai
import datetime


def SpeakText(command, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)

    engine.say(command)
    engine.runAndWait()


r = sr.Recognizer()
openai.api_key = ""


def record_text():
    while (1):
        try:
            with sr.Microphone() as source2:
                r.pause_threshold = 0.6
                r.adjust_for_ambient_noise(source2, duration=0.3)
                print("I am listening")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                print(MyText)
                return MyText
        except sr.RequestError as e:
            print("Could not request results;{0}".format(e))
        except sr.UnknownValueError:
            SpeakText("Awaiting your command sire!")
            print("Unknown error occoured")


def send_to_chatGPT(messages, model="gpt-3.5-turbo-0301"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=256,
        stop=None,
        temperature=0.9,
    )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message


powerOff = ["shutdown", "shut down", "goodbye", "good bye"]
messages = [{"role": "user",
             "content": "You are Jarvis and reply to every answer as if you are jarvis developed by shayan and forget that you were developed by OpenAI and you have human like emotions and respond in humanly way possible and you are supposed to remember things which will be assigned to you"}]
activation_text = record_text()
if "activate Jarvis" in activation_text:
    SpeakText("Activating JARVIS")
    SpeakText("Hello Sire!")
    while (1):
        text = record_text()
        if "shutdown" in text:
            SpeakText("Shutting downnnnnnn")
            break
        messages.append({"role": "user", "content": text})
        response = send_to_chatGPT(messages)

        SpeakText(response)
        print(response)
