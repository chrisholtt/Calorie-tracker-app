from flask import Flask, render_template, redirect, Blueprint, request
from repositories import user_repository, day_repository, food_repository
from models.user import User
from models.food import Food

foods_blueprint = Blueprint("foods", __name__)

#  NEW CREATION ROUTE
@foods_blueprint.route("/foods/new/<id>/<day>", methods=["POST"])
def new_food(id, day):
    name = request.form['name']
    calories = request.form['calories']
    food_type = request.form['food_type']
    food = Food (name, calories, food_type, False)
    food_repository.save(food)
    day_id = day_repository.get_day_id(id, day)
    return redirect(f"/day/{id}/{day_id}")


# Add food to day
@foods_blueprint.route("/foods/add/<user_id>/<day>/<food_id>", methods=["POST"])
def add_food_to_day(user_id, food_id, day):
    food = food_repository.select(food_id)
    day_id = request.form['day_id']
    user = user_id
    # finish here
    food_repository.save_food_to_day(food, day_id, user)
    return redirect(f"/day/{user_id}/{day_id}")

# remove food
@foods_blueprint.route("/foods/remove/<user_id>/<day>/<food_id>", methods=["POST"])
def remove_food(user_id, day, food_id):
    day_id = day_repository.get_day_id(user_id, day)
    food_repository.delete(food_id)
    return redirect(f"/day/{user_id}/{day_id}")


# EAT FOOD
@foods_blueprint.route("/foods/eat/<user_id>/<day>/<food_id>", methods=["POST"])
def eat_food(user_id, day, food_id):
    day_id = day_repository.get_day_id(user_id, day)
    food_repository.eat(True, food_id)
    return redirect(f"/day/{user_id}/{day_id}")

# UNEAT FOOD
@foods_blueprint.route("/foods/uneat/<user_id>/<day>/<food_id>", methods=["POST"])
def uneat_food(user_id, day, food_id):
    day_id = day_repository.get_day_id(user_id, day)
    food_repository.eat(False, food_id)
    return redirect(f"/day/{user_id}/{day_id}")


# EDIT FOOD 
@foods_blueprint.route("/foods/edit/<user_id>/<food_id>", methods=["POST"])
def edit_food(user_id, food_id):
    day_id = request.form["day_id"]
    food = food_repository.select(food_id)
    return render_template("foods/edit.html", food=food, day_id=day_id, user_id=user_id, food_id=food_id)
    

# UPDATE FOOD
@foods_blueprint.route("/foods/edit/add/<user_id>/<food_id>/<day_id>", methods=["POST"])
def update_food(user_id, food_id, day_id):
    name = request.form['name']
    calories = request.form['calories']
    type = request.form['food_type']
    food_repository.edit(name, calories, type, food_id)
    return redirect(f"/day/{user_id}/{day_id}")
    

# SEARCH FOOD:
@foods_blueprint.route("/foods/search/<id>/<days_id>", methods=["POST"])
def search(id, days_id):
    search_value = request.form['search']
    results = food_repository.search(search_value)
    print(results)
    # Now returning back to a duplicate of the main day route:
    user = user_repository.select(id)
    day = day_repository.select_day(days_id)
    days = day_repository.select_with_user_id(id)
    calories = day_repository.get_calories(id, days_id)
    eaten_calories = food_repository.get_eaten_cals(id, days_id)
    eat_calories = food_repository.get_eat_cals(calories, eaten_calories)
    foods = food_repository.user_foods(id, days_id)
    unassigned_foods = results
    return render_template("days/day.html", day=day, user=user, days=days, calories=calories, unassigned_foods=unassigned_foods, foods=foods, eaten_calories=eaten_calories, eat_calories=eat_calories, days_id=days_id)
    
