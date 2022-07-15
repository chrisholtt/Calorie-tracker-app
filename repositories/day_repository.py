from db.run_sql import run_sql

from models.user import User
from models.food import Food



def save(day):
    sql = """
    INSERT INTO days (day, target_calories)
    VALUES (%s, %s)
    RETURNING *
    """

    values = [day.name, day.target_calories]
    results = run_sql(sql, values)
    day.id = results[0]['id']


def delete_all():
    sql = "DELETE FROM days"
    run_sql(sql)

