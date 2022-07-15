from db.run_sql import run_sql

from models.user import User
from models.food import Food


def save(user):
    sql = """
    INSERT INTO users (name)
    VALUES (%s)
    RETURNING *
    """

    values = [user.name]
    results = run_sql(sql, values)
    user.id = results[0]['id']

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)