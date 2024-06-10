import wolframalpha
import requests


app_id = 'PUYG5V-8QX5GE6VAT'
app = wolframalpha.Client(app_id)
api_key = '5a3bf3f6e067ac01a49e704f0d41470e'

news_api_key = '59dbae77bd204023adc74d22e555ceae'


def weather(query):
    city_name = 'Bikaner' if query is None else query

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key

    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final = (f"{condition} {str(temp)} degree celsius, humidity is {str(humidity)} percent, "
             f"wind speed is {str(wind)} kilometer per hour")

    print(final)
    return final


def get_news():
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": news_api_key,
        "country": "in",
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if "status" in data and data["status"] == "ok":
        articles = data["articles"][:5]
        titles = '\n'.join([article["title"] for article in articles])
        print(titles)
        return titles
    else:
        return None
