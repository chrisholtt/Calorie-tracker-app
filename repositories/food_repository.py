from db.run_sql import run_sql

from models.user import User
from models.food import Food




def delete_all():
    sql = "DELETE FROM foods"
    run_sql(sql)