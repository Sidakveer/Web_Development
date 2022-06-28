import wtforms.validators
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[Email()])
    password = PasswordField(label="Password", validators=[InputRequired(message="Must be atleast 8 characters long")])
    submit = SubmitField(label="Log In")



app.secret_key = "any token"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)