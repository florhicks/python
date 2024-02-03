import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    request_cafe = random.choice(cafes).to_dict()
    return jsonify(cafe=request_cafe)


@app.route("/all", methods=["GET"])
def get_all_cafes():
    all_cafes = [cafe.to_dict() for cafe in db.session.query(Cafe).all()]
    return jsonify(all_cafes)


@app.route("/search", methods=["GET"])
def search_cafe_by_location():
    location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Cafe Not Found": "We dont find a cafe at that location"})


@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Succesfully added the new cafe"})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price_coffee(cafe_id):
    price = request.args.get("new_price")
    coffee_to_update = Cafe.query.get(cafe_id)
    if coffee_to_update:
        coffee_to_update.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Coffee price updated"}), 200
    else:
        return jsonify(response={"error": "Not found id of required cafe"}), 404


@app.route("/reports-closed/<cafe_id>", methods=["DELETE"])
def closed_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "APIkey":
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Deleted cafe"}), 200
        else:
            return jsonify(error={"cafe not found": "wrong ID"}), 404
    else:
        return jsonify(error={"failed": "wrong API key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
