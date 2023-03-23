import requests

# answer = requests.get("https://api.kanye.rest")
# data = answer.json()["quote"]

# print(data)
p = {
    "lat":24.453884,
    "lng":54.377342
}
response = requests.get("https://api.sunrise-sunset.org/json", params=p)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise+"\n"+sunset)
