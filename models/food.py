class Food:
    def __init__(self, name, calories, eaten=False, id=None):
        self.name = name
        self.calories = calories
        self.eaten = eaten
        self.id = id

    def eat(self):
        self.eaten = True

    def un_eat(self):
        self.eaten = False
    
