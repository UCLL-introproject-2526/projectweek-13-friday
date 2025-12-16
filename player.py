import students
class Player:
    def __init__(self,name, inventory):
        self.name = name
        self.inventory = inventory
        self.current_assignments = 0

# currency must only work with ints and can't be negative.
    def add_assigments(self, amount):
       if isinstance(amount, int) and amount > 0:
            self.current_assignments += amount
       else:
           raise ValueError("Please enter an integer bigger than 0 ")
           
    def submit_assigments(self, amount):
        if isinstance(amount, int) and self.current_assignments >= amount:
            self.current_assignments -= amount
        else:
            print("You don't have enough tests to pay for this")
 # interaction between player and student where inventory goes down and assignments get added         
    def delivery_transaction(self, player, student, payment):
        if student.demand["order"][0] in player.current_inventory and student.demand["order"][1] <= player.current_inventory[student.demand["order"][0]]:
            player.add_assignments(payment)
            player.decrease_inventory(student.demand["order"][0], student.demand["order"][1])


    def __repr__(self):
        return f"name:{self.name}, inventory:{self.inventory}, assignments: {self.current_assignments}"

#make a player inventory that starts at 0 and can expand
class Inventory:
    def __init__(self):
        self.current_inventory = {}

    def add_to_inventory(self, candy_type, q):
        self.current_inventory[candy_type] = q

    def decrease_inventory(self, candy_type, q):
        self.current_inventory[candy_type] -= q

    #print the q/ value of the candy in the bag
    def __repr__(self):
        return f"{self.current_inventory}"
    
        
#make an object for a candy type
class Candy_type:
    def __init__(self,name, colour, flavour ):
        self.colour = colour
        self.flavour = flavour
        self.name = name

#print the name/ key of the candy in the bag
    def __repr__(self):
        return f"{self.name}"


        
# test

bag = Inventory()
p1 = Player("Super Senior", bag)
drop = Candy_type("drop","black", "salty")
bubblegum = Candy_type("bubblegum", "pink" ,"strawberry")
napoleon = Candy_type("napoleon", "white", "sour")
bag.add_to_inventory(drop, 1)
bag.add_to_inventory(bubblegum, 5)
print(p1.current_assignments)
p1.add_assigments(10)
print(p1.current_assignments)
p1.submit_assigments(5)
print(p1)