from re import L
from flask import request
from db.run_sql import run_sql

from models.user import User
from models.food import Food




# def save_name_and_calories(name, calories, user_id, type):
#     sql = """
#     INSERT INTO foods (name, calories, user_id, type)
#     VALUES (%s, %s, %s, %s)
#     RETURNING *
#     """
#     values = [name, calories, user_id, type]
#     results = run_sql(sql, values)

def save(food):
    sql = """
    INSERT INTO foods (name, calories, food_type, eaten)
    VALUES ( %s, %s, %s, %s)
    RETURNING *
    """
    values = [ food.name, food.calories, food.food_type, food.eaten]
    results = run_sql(sql, values)
    food.id = results[0]['id']




def delete_all():
    sql = "DELETE FROM foods"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM foods WHERE id = %s"
    values = [id]
    run_sql(sql, values)




# def select_all():
#     foods = []
#     sql = """
#     SELECT id, name, calories, food_type FROM foods
#     """
#     results = run_sql(sql)
#     for row in results:
#         foods.append(Food(row['name'], row['calories'], row['food_type']))
#     return foods



def select_all():
    foods = []
    sql = """
    SELECT * FROM foods
    """
    results = run_sql(sql)
    for row in results:
        foods.append(Food(row['name'], row['calories'], row['food_type'], row['day_id'], row['user_id'], row['eaten'], row['id']))
    return foods


def unassigned_foods():
    foods = []
    sql = """
    SELECT * FROM foods
    WHERE user_id IS NULL
    """
    results = run_sql(sql)
    for row in results:
        foods.append(Food(row['name'], row['calories'], row['food_type'], row['day_id'], row['eaten'], row['id']))
    return foods




def select(id):
    food = None
    sql = "SELECT * FROM foods WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        result = results[0]
        food = Food(result['name'], result['calories'], result['food_type'], result['eaten'] )
    return food
    

# def add_food_to_day(food):
#     sql = """
#     UPDATE foods SET (day_id, user_id) = (%s, %s)
#     WHERE id = %s
#     RETURNING *
#     """
#     values = [day_id, user_id, food_id]
#     result = run_sql(sql, values)
#     return result



def save_food_to_day(food, day_id, user_id):
    sql = """
    INSERT INTO foods (name, calories, food_type, eaten, day_id, user_id)
    VALUES ( %s, %s, %s, %s, %s, %s)
    RETURNING *
    """
    values = [ food.name, food.calories, food.food_type, food.eaten, day_id, user_id]
    results = run_sql(sql, values)
    # food.id = results[0]['id']


def user_foods(user_id, day_id):
    foods = []
    sql = "SELECT * FROM foods WHERE user_id = %s AND day_id = %s"
    values = [user_id, day_id]
    results = run_sql(sql, values)

    if results:
        for result in results:
            foods.append(Food(result['name'], result['calories'], result['food_type'], result['eaten'], result["day_id"], result['id']) ) 
    return foods

def eat(bool, id):
    sql = """
    UPDATE foods SET eaten = %s
    WHERE id = %s
    """
    values = [bool, id]
    run_sql(sql, values)


def get_eaten_cals(user_id, day_id):
    eaten_cals = 0
    sql = """
    SELECT * FROM foods
    WHERE user_id = %s AND day_id = %s
    """
    values = [user_id, day_id]
    results = run_sql(sql, values)

    if results:
        for result in results:
            if result['eaten'] == 'true':
                eaten_cals += result['calories']
        return eaten_cals

def get_eat_cals(calories, eaten_calories):
    eat_calories = 0
    if not calories and not eaten_calories:
        return eat_calories 

    elif calories and eaten_calories:
        eat_calories = calories - eaten_calories
        return eat_calories

    elif calories and eat_calories == 0:
        eat_calories = calories
        return eat_calories



def edit(name, calories, food_type, id):
    sql = """
    UPDATE foods
    SET name = %s, calories = %s, food_type = %s
    WHERE id = %s
    """
    values = [name, calories, food_type, id]
    run_sql(sql, values)