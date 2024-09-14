import requests
from twilio.rest import Client
account_sid = ''
auth_token = ''
parameters = {
    "lat" : 23.344101,
    "lon" : 85.309563,
    "appid" : "",
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data = response.json()
print(data["list"][0]["weather"][0]["id"])
weather_id = [data["list"][i]["weather"][0]["id"] for i in range(0,4)]
print(weather_id)
will_rain = False
for id in weather_id:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body= "Its going to rain today, bring umbrella.",from = "",to = '')
    print(message.status)