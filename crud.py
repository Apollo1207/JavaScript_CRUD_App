import json
from flask import Flask, redirect, render_template, \
    request, jsonify, make_response, abort, url_for

from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from flask_sqlalchemy import SQLAlchemy

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
    id = db.Column(db.Integer, unique=True, primary_key=True)
    number_of_seats = db.Column(db.Integer, unique=False)
    year_of_foundation = db.Column(db.Integer, unique=False)
    location = db.Column(db.String(30), unique=False)
    scale_of_field = db.Column(db.Integer, unique=False)
    name_of_sport = db.Column(db.String(30), unique=False)

    def __str__(self):
        return f"NumberOfSeats:{self.number_of_seats} YearOfFoundation:{self.year_of_foundation}" \
               f" Location:{self.location} ScaleOfField:{self.scale_of_field} NameOfSport:" \
               f"{self.name_of_sport} "


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


@app.route("/home", methods=["GET"])
def get_all_sport_builds():
    all_sport_builds = SportBuild.query.all()
    sport_builds = sport_builds_schema.dump(all_sport_builds)
    return render_template("index.html", sport_builds=sport_builds)


@app.route("/", methods=["GET", "POST"])
def create_sport_build():
    if request.method == "POST":
        try:
            sport_build = SportBuild(
                number_of_seats=request.form.get("seats"),
                year_of_foundation=request.form.get("year"),
                location=request.form.get("location"),
                scale_of_field=request.form.get("scale"),
                name_of_sport=request.form.get("name"))

            db.session.add(sport_build)
            db.session.commit()
            return redirect(url_for('get_all_sport_builds'))
        except Exception as e:
            print("Failed to add sportBuild")
            print(e)

    return render_template("create.html")


@app.route("/update/<id>", methods=["POST", "GET", "PUT"])
def update_sport_build(id):
    sport_builds = SportBuild.query.get(id)
    if request.method == "POST":
        if sport_builds.number_of_seats != request.form["seats"]:
            sport_builds.number_of_seats = request.form["seats"]
        if sport_builds.year_of_foundation != request.form["year"]:
            sport_builds.year_of_foundation = request.form["year"]
        if sport_builds.location != request.form["location"]:
            sport_builds.location = request.form["location"]
        if sport_builds.scale_of_field != request.form["scale"]:
            sport_builds.scale_of_field = request.form["scale"]
        if sport_builds.name_of_sport != request.form["name"]:
            sport_builds.name_of_sport = request.form["name"]
        db.session.add(sport_builds)
        db.session.commit()
        return redirect(url_for('get_all_sport_builds'))

    return render_template("edit.html", sport_builds=sport_builds)


@app.route("/delete/<id>")
def delete_sport_build(id):
    sport_builds = SportBuild.query.get(id)
    db.session.delete(sport_builds)
    db.session.commit()
    return redirect(url_for('get_all_sport_builds'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="3000")
