from db.run_sql import run_sql



def set_reminder(reminder, user_id, day_id):
    sql = """
    INSERT INTO reminders (reminder, user_id, day_id)
    VALUES (%s, %s, %s)
    """
    values = [reminder, user_id, day_id]
    run_sql(sql, values)

def get_reminders(user_id, day_id):
    reminders = []
    sql = """
    SELECT * FROM reminders
    WHERE user_id = %s AND day_id = %s
    """

    values = [user_id, day_id]
    result = run_sql(sql, values)

    if result:
        for row in result:
            reminders.append(row['reminder'])
        return reminders
