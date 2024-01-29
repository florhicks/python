from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

if not os.path.exists("new-books-collection.db"):
    with app.app_context():
        db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods = ["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        rating = request.form["rating"]
        with app.app_context():
      

            new_book = Book(title=name, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:id>",methods = ["GET","POST"])
def edit(id):
    if request.method == "POST":
        with app.app_context():
            book_to_update = Book.query.get(id)
            book_to_update.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for('home'))
    with app.app_context():
            book = Book.query.filter_by(id=id).first()
    return render_template("edit_rating.html", book = book )

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

