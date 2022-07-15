class Day:
    def __init__(self, day, id=None):
        self.day = day
        self.target_calroies = 0
        self.foods = []
        self.id = id

    def add_food(self, food):
        self.foods.append(food)
