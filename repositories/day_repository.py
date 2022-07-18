from unittest import result
from db.run_sql import run_sql
from repositories import user_repository

from models.user import User
from models.food import Food
from models.day import Day



def save(day):
    sql = """
    INSERT INTO days (day, user_id)
    VALUES (%s, %s)
    RETURNING *
    """

    values = [day.day, day.user.id]
    results = run_sql(sql, values)
    day.id = results[0]['id']


def delete_all():
    sql = "DELETE FROM days"
    run_sql(sql)


def save_days(days):
    for day in days:
        sql = """
        INSERT INTO days (day, user_id)
        VALUES (%s, %s)
        RETURNING *
        """

        values = [day.day, day.user.id]
        results = run_sql(sql, values)
        day.id = results[0]['id']
            

def select_with_user_id(id):
    days = []
    sql = "SELECT * FROM days WHERE user_id = %s ORDER BY id"
    values = [id]
    results = run_sql(sql, values)

    if results:
        user = user_repository.select(id)
        for row in results:
            days.append(Day(row['day'], user, row['id']))
    return days


def set_target_calories(calories, id, day):
    sql = """
    UPDATE days SET target_calories = %s
    WHERE user_id = %s AND day = %s
    """
    values = [calories, id, day]
    run_sql(sql, values)


def get_calories(user_id, id):
    calories = None
    sql = "SELECT target_calories FROM days WHERE user_id = %s AND id = %s"
    values = [user_id, id]
    results = run_sql(sql, values)

    if results:
        calories = results[0]["target_calories"]
        return calories


def select_day(day_id):
    day = None
    sql = "SELECT day FROM days WHERE id = %s"
    values = [day_id]
    results = run_sql(sql, values)

    if results:
        day = results[0]['day']
        return day


def get_day_id(id, day):
    day_id = None
    sql = "SELECT id FROM days WHERE user_id = %s AND day = %s"
    values = [id, day]
    results = run_sql(sql, values)

    if results:
        day_id = results[0]['id']
        return day_id


def get_first_day_id(user_id):
    day_id = None
    sql = """
    SELECT id FROM days
    WHERE user_id = %s
    """
    values = [user_id]

    results = run_sql(sql, values)

    if results:
        for row in results:
            day_id = row['id']
            return day_id

