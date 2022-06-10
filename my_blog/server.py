from flask import Flask, render_template
import requests


app = Flask(__name__)
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=response, num=num)


if __name__ == "__main__":
    app.run(debug=True)
