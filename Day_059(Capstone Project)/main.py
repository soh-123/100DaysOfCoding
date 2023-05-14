from flask import Flask, render_template
import requests

all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

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

@app.route("/post/<int:id>.html")
def show_post(id):
    index = id - 1
    display_post = all_posts[index]
    return render_template("post.html", post=display_post)

if __name__ == "__main__":
    app.run(debug=True)