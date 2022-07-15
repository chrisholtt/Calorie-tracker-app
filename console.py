import pdb
from controllers.users_controller import user
from models.user import User
from models.food import Food
from models.day import Day

import repositories.user_repository as user_repository
import repositories.food_repository as food_repository
import repositories.day_repository as day_repository

food_repository.delete_all()
day_repository.delete_all()
user_repository.delete_all()


# Setting up the users:
user1 = User("Chris")
user_repository.save(user1)
print(user1.name, user1.id)

user2 = User("Jack")
user_repository.save(user2)
print(user2.name, user2.id)


# Setting up the days:





