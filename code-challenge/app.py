from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from database import db
from models import Hero, Power
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheros.db"
migrate = Migrate(app, db)
api = Api(app)

db.init_app(app)

@app.route("/powers", methods=['GET', 'POST'])
def get_powers():
    if request.method == 'GET':
        powers = [power.to_dict() for power in Power.query.all()]
        return jsonify(powers), 200

    if request.method == 'POST':
        data = request.get_json()
        new_power = Power(
            name=data["name"],
            description=data["description"],
            hero_id=data["hero_id"]
        )

        db.session.add(new_power)
        db.session.commit()
        return jsonify(new_power.to_dict()), 201

@app.route("/powers/<int:id>", methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    return jsonify(power.to_dict()), 200


@app.route("/powers/<int:id>", methods=['GET', 'PATCH'])
def get_or_update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    if request.method == 'GET':
        return jsonify(power.to_dict()), 200

    if request.method == 'PATCH':
        data = request.get_json()
        if "name" in data:
            power.name = data["name"]
        if "description" in data:
            power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict()), 200


@app.route("/heroes/<int:id>", methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify(hero.to_dict()), 200
    

@app.route("/heroes", methods=['GET', 'POST'])
def get_heroes():
    if request.method == 'GET':
        heroes = [hero.to_dict() for hero in Hero.query.all()]
        return jsonify(heroes), 200

    if request.method == 'POST':
        data = request.get_json()
        new_hero = Hero(
            name=data["name"],
            super_name=data["super_name"]
        )
        db.session.add(new_hero)
        db.session.commit()
        return jsonify(new_hero.to_dict()), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)
