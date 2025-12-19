from player_implementatie.player import Player_, Inventory, Candy_type
from player_implementatie.students import Student
import random
from ui.prompt import *
from world.room import *

#make an order after an amount of time passes
class Transaction:
    def __init__(self, selling_location, student, room):
        self.buyer = room.student_locations[student]
        self.rect = pygame.Rect(selling_location, 400, 10, 100)
    
 # interaction between player and student where inventory goes down and assignments get added     
    def delivery_transaction(self, player, student):
        type = student.order["order"][0]
        quantity = student.order["order"][1]
        payment = quantity * 2
    
        if player.current_inventory.has_candy(type) and quantity <= player.current_inventory.get_quantity(type):
            player.add_assignments(payment)
            player.current_inventory.decrease_inventory(type, quantity) 
        print(f"Current assignments: {player.current_assignments}")
        print(f"Current inventory: {player.current_inventory}")


    # def __repr__(self):
    #     return f'{self.location}'
    
    #def new_order(self, student, time):
    #     pass
#test
#player info
# bag = Inventory()
# p1 = Player_("Super Senior", bag)

# drop = Candy_type("drop","black", "salty")
# bubblegum = Candy_type("bubblegum", "pink" ,"strawberry")
# napoleon = Candy_type("napoleon", "white", "sour")
# sourpatch = Candy_type("sourpatch", "mixed", "sour")
# cola_bottles = Candy_type("cola bottle", "brown", "cola")

# bag.add_to_inventory("drop", 100)
# bag.add_to_inventory("bubblegum", 100)
# bag.add_to_inventory("sourpatch", 100)
# bag.add_to_inventory("cola bottle", 100)


#student info
# student_mark = Student("Mark")
# student_mark.add_order()

#transaction info
# print(student_mark)
# first = Transaction()
# first.delivery_transaction(p1, student_mark)
#bag.decrease_inventory(student_mark.order["order"][0], student_mark.order["order"][1])


