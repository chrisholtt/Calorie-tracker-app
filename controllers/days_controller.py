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

