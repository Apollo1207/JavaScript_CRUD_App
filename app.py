import json

from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

with open("secret.json") as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)


class SportBuild(db.Model):
    __tablename__ = "sport_build"
    id = db.Column(db.Integer, primary_key=True)
    number_of_seats = db.Column(db.Integer, unique=False)
    year_of_foundation = db.Column(db.Integer, unique=False)
    location = db.Column(db.String(30), unique=False)
    scale_of_field = db.Column(db.Integer, unique=False)
    name_of_sport = db.Column(db.String(30), unique=False)

    def __init__(self,
                 number_of_seats=None, year_of_foundation=None,
                 location=None, scale_of_field=None,
                 name_of_sport=None, roof_type=None,
                 color_of_field=None, count_of_vip_places=None):
        self.number_of_seats = number_of_seats
        self.year_of_foundation = year_of_foundation
        self.location = location
        self.scale_of_field = scale_of_field
        self.name_of_sport = name_of_sport

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class SportBuildSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = SportBuild
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    number_of_seats = fields.Integer(required=True)
    year_of_foundation = fields.Integer(required=True)
    location = fields.String(required=True)
    scale_of_field = fields.Integer(required=True)
    name_of_sport = fields.String(required=True)


sport_build_schema = SportBuildSchema()
sport_builds_schema = SportBuildSchema(many=True)


@app.route("/sportBuilds", methods=["GET"])
def get_all_sport_builds():
    get_sport_builds = SportBuild.query.all()
    if not get_sport_builds:
        abort(404)
    sport_builds = sport_builds_schema.dump(get_sport_builds)
    return make_response(jsonify({"sportBuild": sport_builds}), 200)


@app.route("/sportBuild", methods=["POST"])
def create_sport_build():
    data = request.get_json()
    sport_build = sport_build_schema.load(data)
    sport_builds = sport_build_schema.dump(sport_build.create())
    return make_response(jsonify({"sportBuild": sport_builds}), 200)


@app.route("/sportBuild/<id>", methods=["PUT"])
def update_sport_build_by_id(id):
    data = request.get_json()
    get_sport_build = SportBuild.query.get(id)
    if data.get("number_of_seats"):
        get_sport_build.number_of_seats = data["number_of_seats"]
    if data.get("year_of_foundation"):
        get_sport_build.year_of_foundation = data["year_of_foundation"]
    if data.get("location"):
        get_sport_build.location = data["location"]
    if data.get("scale_of_field"):
        get_sport_build.scale_of_field = data["scale_of_field"]
    if data.get("name_of_sport"):
        get_sport_build.name_of_sport = data["name_of_sport"]

    db.session.add(get_sport_build)
    db.session.commit()
    sport_builds = sport_build_schema.dump(get_sport_build)
    return make_response(jsonify({"sportBuild": sport_builds}), 200)


@app.route("/sportBuild/<id>", methods=["DELETE"])
def delete_sport_build_by_id(id):
    get_sport_build = SportBuild.query.get(id)
    if not get_sport_build:
        abort(404)
    db.session.delete(get_sport_build)
    db.session.commit()
    return make_response("", 200)


if __name__ == "__main__":
    app.run(debug=True, port="3000")
