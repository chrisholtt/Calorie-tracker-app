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

def delete(id):
    sql = "DELETE FROM users WHERE ID = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        users.append(User(row['name'], row['id']))
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        result = result[0]
        user = User(result['name'], result['id'] )
    return user