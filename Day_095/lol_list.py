import requests
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

response = requests.get("http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json")
response.raise_for_status()
data = response.json()["data"]


version = "9.18.1"

champions = []
for champion in data.values():
    name = champion["name"]
    title = champion["title"]
    description = champion["blurb"]
    image_filename = champion["image"]["full"]
    image_url = f"http://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{image_filename}"
    tags = champion["tags"]
    champions.append({"name": name, "title": title, "description": description, "image_url": image_url, "tags": tags})

@app.context_processor
def inject_now():
    return {'footer_year': datetime.now().year}

@app.route("/")
def home():
    return render_template("index.html", champions=champions)

if __name__ == '__main__':
    app.run(debug=True)