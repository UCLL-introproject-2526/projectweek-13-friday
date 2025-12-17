from transaction import *

class Level:
    def __init__(self, deliveries_to_complete, order_size, portion_range):
        self.deliveries_to_complete =  deliveries_to_complete
        self.order_size = order_size
        self.portion_range = portion_range 


    def increase_level(self, previous_level):
        self.previous_level = previous_level

    def __repr__(self):
        return f'you need to deliver {self.deliveries_to_complete} with an order size of {self.order_size} and a portion range of {self.portion_range}'

#test
level_01 = Level(5, 1, [1, 5])
print(level_01)