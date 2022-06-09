from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<name>")
def name(name):
    import requests

    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()
    age_response = requests.get(f"https://api.agify.io?name={name}").json()
    return render_template("age_gender.html", name=name.title(), gender=gender_response['gender'], age=age_response['age'])


if __name__ == '__main__':
    app.run(debug=True)