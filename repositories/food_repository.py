from db.run_sql import run_sql

from models.user import User
from models.food import Food



def save(food):
    sql = """
    INSERT INTO foods (name, calories, day_id, user_id)
    VALUES (%s, %s, %s, %s)
    RETURNING *
    """

    values = [food.name, food.calories, food.day.id, food.user.id]
    results = run_sql(sql, values)
    food.id = results[0]['id']


def delete_all():
    sql = "DELETE FROM foods"
    run_sql(sql)