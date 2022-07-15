class Day:
    def __init__(self, day, user, id=None):
        self.day = day
        self.user = user
        self.target_calroies = 0
        self.foods = []
        self.id = id

    def add_food(self, food):
        self.foods.append(food)


def setup_days(user):
    days = []
    days.append( Day("Monday", user))
    days.append( Day("Tuesday", user))
    days.append( Day("Wednesday", user))
    days.append( Day("Thursday", user))
    days.append( Day("Friday", user))
    days.append( Day("Saturday", user))
    days.append( Day("Sunday", user))
    
    return days 