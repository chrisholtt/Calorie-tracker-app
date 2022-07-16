class Food:
    def __init__(self, name, calories, food_type, day=None, user=None, eaten=False, id=None):
        self.name = name
        self.calories = calories
        self.food_type = food_type
        self.day = day
        self.user = user
        self.eaten = eaten
        self.id = id

    def eat(self):
        self.eaten = True

    def un_eat(self):
        self.eaten = False
    
