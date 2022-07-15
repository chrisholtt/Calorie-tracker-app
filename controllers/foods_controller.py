from flask import Flask, render_template, redirect, Blueprint, request
from repositories import user_repository, day_repository, food_repository
from models.user import User

foods_blueprint = Blueprint("foods", __name__)

#  NEW CREATION ROUTE
@foods_blueprint.route("/foods/new/<id>/<day>", methods=["POST"])
def new_creation(id, day):
    return redirect(f"/day/{id}/{day}")

