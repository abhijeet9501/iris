import google.generativeai as gem
import re

gem.configure(api_key="AIzaSyDeksTEF53JrMLymSJ7NwWTFN5j2fo2c9s")

generation_config = {
    "temperature": 1.5,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 50,
    "response_mime_type": "text/plain"
}

model = gem.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config)

convo = model.start_chat()

with open(r"D:\Python\Projects\Iris\intent.txt", "r", encoding="utf-8") as file:
    prompt = file.read()
    file.close()

convo.send_message(prompt)


def get_intent(msg):
    convo.send_message(msg)
    text = convo.last.text

    if not text.endswith('"'):
        text += '"'

    intent = re.search(r"\{([^\}]+)\}", text)
    query = re.search(r"\[([^\]]+)\]", text)
    message = re.search(r"\"([^\"]+)\"", text)

    intent = intent.group(1) if intent else None
    query = query.group(1) if query else None
    message = message.group(1) if message else None

    return intent, message, query
