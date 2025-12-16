import player
import students
import random
#make an order after an amount of time passes
class Transaction:
    def __init__(self, player, student):
        self.location = self.set_spawn_location()

#assign spawnpoint
    def set_spawn_location(self):
        with open('locations.txt', 'r', encoding= 'utf-8') as file:
            rooms = file.readlines()
            current_room = random.choice(rooms)
        return current_room
    
    def new_order(self, student, time):
        pass
    def __repr__(self):
        return f'current room {self.location}'

#test
school = Transaction("Super Senior", "Mark")
print(school.location)