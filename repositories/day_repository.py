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
    sql = "SELECT * FROM days WHERE user_id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        user = user_repository.select(id)
        for row in results:
            days.append(Day(row['day'], user, row['id']))
    return days

