from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_URL = "https://api.themoviedb.org/3/movie/"
URL_MOVIE_IMG_PATH = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
API_KEY = ""

class EditForm(FlaskForm):
    rating = FloatField(label="Rating:", validators=[DataRequired()])
    review = StringField(label="Review:", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class MovieForm(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String, nullable=False)


if not os.path.exists("new-books-collection.db"):
    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    with app.app_context():
        all_movies = Movie.query.order_by(Movie.rating).all()
        for i in range(len(all_movies)):
            all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
        all_movies = Movie.query.order_by(Movie.rating).all()
    return render_template("index.html", all_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    form = EditForm()
    update_movie = Movie.query.filter_by(id=id).first()
    if form.validate_on_submit():
        update_movie.rating = form.rating.data
        update_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=update_movie)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    deleted_movie = Movie.query.get(id)
    db.session.delete(deleted_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url=MOVIE_DB_URL, params={"query": movie_title, "api_key": API_KEY})
        movie_data = response.json()["results"]
        print(movie_data)
        return render_template("select.html", all_movies=movie_data)
    return render_template("add.html", form=form)


@app.route("/find_movie")
def find_movie():
    movie_id = request.args.get("movie_id")
    response = requests.get(url=f"{MOVIE_DETAILS_URL}{movie_id}", params={"api_key": API_KEY})
    movie_data = response.json()
    print(movie_data)
    new_movie = Movie(
        title=movie_data["original_title"],
        year=int(movie_data["release_date"].split("-")[0]),
        description=movie_data["overview"],
        img_url=f"{URL_MOVIE_IMG_PATH}{movie_data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)