from flask import Flask, render_template
import random
import datetime 
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year
    return render_template('index.html', num=random_number, updated_year=year)


@app.route('/guess/<name>')
def guess(name):
    
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    genderize = genderize_response.json()
    gender = genderize["gender"]

    agify_response = requests.get(f"https://api.agify.io?name={name}")
    agify = agify_response.json()
    age = agify["age"]

    return render_template('guess.html', gender=gender, age=age, name=name)

@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template('blog.html', posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)