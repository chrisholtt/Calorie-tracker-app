from flask import Flask, render_template, redirect, Blueprint, request
from repositories import user_repository, day_repository, food_repository
from models.user import User


days_blueprint = Blueprint("days", __name__)

#  INDEX 
@days_blueprint.route("/days/<id>")
def days(id):
    user = user_repository.select(id)
    days = day_repository.select_with_user_id(id)
    return render_template("days/index.html", user=user, days=days)

# Individual day:
@days_blueprint.route("/day/<id>/<day>")
def day(id, day):
    user = user_repository.select(id)
    days = day_repository.select_with_user_id(id)
    calories = day_repository.get_calories(id, day)
    return render_template("days/day.html", day=day, user=user, days=days, calories=calories)

# Calorie POST
@days_blueprint.route("/calories/<id>/<day>", methods=["POST"])
def target_calories(id, day):
    calories = request.form["target_calories"]
    print(calories)
    day_repository.set_target_calories(calories, id, day)
    return redirect(f"/day/{id}/{day}")
