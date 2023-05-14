from flask import Flask, render_template, request
import requests
import smtplib
import os

all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
EMAIL = os.environ("MY_EMAIL")
PASSWORD = os.environ("MY_PASSWORD")
app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template('index.html', posts=all_posts)

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

@app.route("/post/<int:id>.html")
def show_post(id):
    index = id - 1
    display_post = all_posts[index]
    return render_template("post.html", post=display_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)