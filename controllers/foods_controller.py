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
    food = Food (name, calories, food_type)
    food_repository.save(food)
    return redirect(f"/day/{id}/{day}")


# Add food to day
@foods_blueprint.route("/foods/add/<user_id>/<day>/<food_id>", methods=["POST"])
def add_food_to_day(user_id, food_id, day):
    food = food_repository.select(food_id)
    food.day = request.form['day_id']
    food.eaten = 0
    food.user = user_id
    food_repository.save_food_to_day(food)
    return redirect(f"/day/{user_id}/{day}")
