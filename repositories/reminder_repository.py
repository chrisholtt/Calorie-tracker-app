from db.run_sql import run_sql
from models.reminder import Reminder


def set_reminder(reminder, completed, user_id, day_id):
    sql = """
    INSERT INTO reminders (reminder, completed, user_id, day_id)
    VALUES (%s, %s, %s, %s)
    """
    values = [reminder, completed, user_id, day_id]
    run_sql(sql, values)

def get_reminders(user_id, day_id):
    reminders = []
    sql = """
    SELECT * FROM reminders
    WHERE user_id = %s AND day_id = %s
    ORDER BY completed
    """

    values = [user_id, day_id]
    result = run_sql(sql, values)

    if result:
        for row in result:
            reminders.append(Reminder(row['reminder'], row['completed'], row['id']))
        return reminders


def delete(id):
    sql = """
    DELETE FROM reminders
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


def select(id):
    reminder = None
    sql = """
    SELECT * FROM reminders
    WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)
    print(result)

    if result:
        result = result[0]
        reminder = Reminder(result['reminder'], result['completed'], result['id'])
        return reminder


def complete(bool, id):
    sql = """
    UPDATE reminders SET completed = %s
    WHERE id = %s
    """
    values = [bool, id]
    run_sql(sql, values)