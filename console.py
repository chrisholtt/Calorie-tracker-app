import pdb
from controllers.users_controller import user
from models.user import User
from models.food import Food
from models.day import Day, setup_days

import repositories.user_repository as user_repository
import repositories.food_repository as food_repository
import repositories.day_repository as day_repository

food_repository.delete_all()
day_repository.delete_all()
user_repository.delete_all()

# Setting up the users:
# user1 = User("Chris")
# user_repository.save(user1)
# print(user1.name, user1.id)

# user2 = User("Jack")
# user_repository.save(user2)
# print(user2.name, user2.id)


# Setting up the days:
# Maybe setup a function for this?
# monday = Day("Monday", user1)
# tuesday = Day("Tuesday", user1)
# wednesday = Day("Wednesday", user1)
# thursday = Day("Thursday", user1)
# friday = Day("Friday", user1)
# saturday = Day("Saturday", user1)
# sunday = Day("Sunday", user1)
# day_repository.save(monday)
# day_repository.save(tuesday)
# day_repository.save(wednesday)
# day_repository.save(thursday)
# day_repository.save(friday)
# day_repository.save(saturday)
# day_repository.save(sunday)



# user1_days = setup_days(user1)
# for day in user1_days:
#     day_repository.save(day)

# user2_days = setup_days(user2)
# for day in user2_days:
#     day_repository.save(day)


# # Setting up food:
# apple = Food("apple", 200, user1_days[0], user1)
# food_repository.save(apple)
# banana = Food("banana", 150, user1_days[0], user1)
# food_repository.save(banana)
# sausage_roll = Food("sausage roll", 300, user1_days[0], user1)
# food_repository.save(sausage_roll)
# chocolate = Food("chocolate", 300, user1_days[0], user1)
# food_repository.save(chocolate)




