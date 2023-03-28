import requests
from twilio.rest import Client


api_key = "Private api key"
account_sid = "AC31231ec2bafa0063a47a69117eaaef60"
auth_token = "hidden aith token"
parameters = {
    "lat":-9.975337,
    "lon":-68.429321,
    "exclude":"current, minutely, daily",
    "appid":api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:2]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's raining today, bring an umbrella",
            from_='+14346029262',
            to='+971526738751'
            )
print(message.status)


