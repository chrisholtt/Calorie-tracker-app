from flask import Flask, render_template, redirect, Blueprint, request
from repositories import user_repository, day_repository, food_repository
from models.user import User
from models.day import Day, setup_days
from models.food import Food


users_blueprint = Blueprint("users", __name__)

#  INDEX 
@users_blueprint.route("/users")
def user():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)


# NEW USER PAGE 
@users_blueprint.route("/users/signup")
def signup():
    return render_template("/users/signup.html")



# NEW USER FORM ROUTE
@users_blueprint.route("/users/new", methods=["POST"])
def new_user():
    name = request.form['name']
    user = User(name)
    user_repository.save(user)
    user_days = setup_days(user)
    day_repository.save_days(user_days)
    return redirect("/users")

# DELETE USER 
@users_blueprint.route("/user/delete/<id>", methods=["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")
