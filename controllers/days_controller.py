import re
from flask import Flask, render_template, redirect, Blueprint, request
from repositories import user_repository, day_repository, food_repository, reminder_repository
from models.user import User


days_blueprint = Blueprint("days", __name__)

#  INDEX 
@days_blueprint.route("/days/<id>")
def days(id):
    first_day_id = day_repository.get_first_day_id(id)
    print(first_day_id)
    return redirect(f"/day/{id}/{first_day_id}")
    # return render_template("days/index.html", user=user, days=days)

# Individual day:
@days_blueprint.route("/day/<id>/<day_id>/")
def day(id, day_id):
    user = user_repository.select(id)
    day = day_repository.select_day(day_id)
    days = day_repository.select_with_user_id(id)
    days_id = day_id
    calories = day_repository.get_calories(id, day_id)
    eaten_calories = food_repository.get_eaten_cals(id, day_id)
    eat_calories = food_repository.get_eat_cals(calories, eaten_calories)
    foods = food_repository.user_foods(id, day_id)
    unassigned_foods = food_repository.unassigned_foods()
    reminders = reminder_repository.get_reminders(id, day_id)
    progress = day_repository.get_progress(calories, eaten_calories)
    return render_template("days/day.html", day=day, user=user, days=days, calories=calories, unassigned_foods=unassigned_foods, foods=foods, eaten_calories=eaten_calories, eat_calories=eat_calories, days_id=days_id, reminders=reminders, progress=progress)


# Set cals
@days_blueprint.route("/calories/<id>/<day>", methods=["POST"])
def target_calories(id, day):
    calories = request.form["target_calories"]
    day_id = day_repository.get_day_id(id, day)
    day_repository.set_target_calories(calories, id, day)
    return redirect(f"/day/{id}/{day_id}")




# REMINDERS:::

# SET reminder:
@days_blueprint.route("/reminder/<id>/<day_id>", methods=["POST"])
def set_reminder(id, day_id):
    reminder = request.form['reminder']
    reminder_repository.set_reminder(reminder, False, id, day_id)
    return redirect(f"/day/{id}/{day_id}/")

# MARK COMPLETED:
@days_blueprint.route("/reminder/mark-completed/<user_id>/<day_id>/<id>", methods=["POST"])
def complete_reminder(user_id, day_id, id):
    reminder_repository.complete(True, id)
    return redirect(f"/day/{user_id}/{day_id}")

# MARK UNCOMPLETED:
@days_blueprint.route("/reminder/mark-uncompleted/<user_id>/<day_id>/<id>", methods=["POST"])
def uncomplete_reminder(user_id, day_id, id):
    reminder_repository.complete(False, id)
    return redirect(f"/day/{user_id}/{day_id}")



# DELETE REMINDER:
@days_blueprint.route("/reminder/delete/<user_id>/<day_id>/<id>", methods=["POST"])
def delete(user_id, day_id, id):
    reminder_repository.delete(id)
    return redirect(f"/day/{user_id}/{day_id}")


