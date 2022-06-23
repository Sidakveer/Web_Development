import smtplib
import flask
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

YOUR_EMAIL = ""
YOUR_PASSWORD = ""


@app.route("/")
def home():
    blogs = requests.get("https://api.npoint.io/9cf96892ea904c91dac0").json()
    return render_template("index.html", all_post=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}, {email}, {phone}, {message}")
        sendmail(name, email, phone, message)
        return render_template("contact.html", strs="Successfully Sent Message")

    return render_template("contact.html", strs="Contact me")


@app.route("/post/<int:id>")
def post(id):
    blogs = requests.get("https://api.npoint.io/9cf96892ea904c91dac0").json()
    for post in blogs:
        if post["id"] == id:
            blog = post
    return render_template("post.html", post=blog)


def sendmail(name, email, phone, msg):
    message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n Message: {msg}"
    with smtplib.SMTP("smtp.gmail.com", port=578) as connection:
        connection.starttls()
        connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(from_addr=YOUR_EMAIL, to_addrs=YOUR_EMAIL, msg=message)


if __name__ == '__main__':
    app.run(debug=True)