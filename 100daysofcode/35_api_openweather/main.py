import settings
import requests
url = "https://api.openweathermap.org/data/2.5/forecast?"



parameters = {
    "lat":58.706070,
    "lon":15.767550,
    "appid":settings.API_KEY,
    "units":"metric",
    "cnt":4}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
condition_codes = [hour_data["weather"][0]["id"] for hour_data in data["list"]]
if any(i <= 700 for i in condition_codes):
    will_train = True

if will_rain:
    print("Bring an umbrella") 


exit()
print(data["list"][0]["weather"][0]["id"])