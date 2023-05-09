from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):
    
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    genderize = genderize_response.json()
    gender = genderize["gender"]

    agify_response = requests.get(f"https://api.agify.io?name={name}")
    agify = agify_response.json()
    age = agify["age"]

    return render_template('guess.html', gender=gender, age=age, name=name)

if __name__ == "__main__":
    app.run(debug=True)