from intent import get_intent
from automation import *
from weather import *

import google.generativeai as genai
import os
import pygame
import edge_tts
import asyncio


genai.configure(api_key="AIzaSyCpBB_5BjbbekcAaCiU2q1wIi4mBmL-h-g")


generation_config = {
    "temperature": 1.5,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain"
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat()

with open(r"D:\Python\Projects\Iris\prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.read()
    file.close()

convo.send_message(prompt)


def model_gem(text):
    convo.send_message(text)
    output = convo.last.text
    return output


async def generate_speech(message):
    communicate = edge_tts.Communicate(message, "en-US-JennyNeural", rate="-10%")
    await communicate.save("data.mp3")


def speak(message):
    try:
        asyncio.run(generate_speech(message))
        pygame.init()
        pygame.mixer.init()

        if os.path.exists("data.mp3") and os.path.getsize("data.mp3") > 0:
            pygame.mixer.music.load("data.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            print("Error: The generated audio file is empty or does not exist.")

    except pygame.error as e:
        print(f"pygame.error: {e}")
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        if os.path.exists("data.mp3"):
            os.remove("data.mp3")


while True:

    try:
        user_message = input("User: ")
        intent, message, query = get_intent(user_message)

        if message is not None:
            print(message)
            speak(message)

        match intent:
            case "automate_music":
                spotify(query)
            case "get_weather":
                report = weather(query)
                speak(report)
            case "automate_youtube":
                youtube(query)
            case "get_news":
                news = get_news()
                speak(news)
            case "gemini":
                reply = model_gem(user_message)
                print(f"Iris: {reply}")
                speak(reply)

    except Exception:
        pass
