import settings
import requests
url = "https://api.openweathermap.org/data/2.5/forecast?"



parameters = {
    "lat":122.70,
    "lon":33.76,
    "appid":settings.API_KEY}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)