from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField(label="Email")
    password = PasswordField(label="Password")
    submit = SubmitField(label="Log In")



app.secret_key = "any token"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)