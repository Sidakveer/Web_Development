from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ============= Api section ===============
API_KEY = "ad78a5e9681681f51de820ce463a70b6"
API_LINK = "https://api.themoviedb.org/3/search/movie"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10.")
    review = StringField("Your review.")
    submit = SubmitField("Add Movie")


class AddForm(FlaskForm):
    movie = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")

# db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        response = requests.get(API_LINK, params={"api_key": API_KEY, "query": form.movie.data})
        result = response.json()["results"]
        return render_template("select.html", data=result)
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie_id = request.args.get("id")
    if movie_id:
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = request.get()


if __name__ == '__main__':
    app.run(debug=True)
