from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")


secret_token = "any token"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = FlaskForm()
    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)