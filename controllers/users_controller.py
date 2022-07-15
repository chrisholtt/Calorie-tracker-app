from flask import Flask, render_template, redirect, Blueprint, request
# from repositories import book_repository, author_repository
from models.user import User


users_blueprint = Blueprint("users", __name__)

#  INDEX 
@users_blueprint.route("/users")
def user():
    return render_template("users/index.html")