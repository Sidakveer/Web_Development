import flask
import requests
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    blogs = requests.get("https://api.npoint.io/9cf96892ea904c91dac0").json()
    return render_template("index.html", all_post=blogs)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:id>")
def post(id):
    blogs = requests.get("https://api.npoint.io/9cf96892ea904c91dac0").json()
    for post in blogs:
        if post["id"] == id:
            blog = post
    return render_template("post.html", post=blog)


if __name__ == '__main__':
    app.run(debug=True)