class Food:
    def __init__(self, name, calories, day, user, eaten=False, id=None):
        self.name = name
        self.calories = calories
        self.day = day
        self.user = user
        self.eaten = eaten
        self.id = id

    def eat(self):
        self.eaten = True

    def un_eat(self):
        self.eaten = False
    
