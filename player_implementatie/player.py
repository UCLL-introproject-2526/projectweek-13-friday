from player_implementatie.students import Student

class Player_:
    def __init__(self,name, inventory):
        self.name = name
        self.current_inventory = inventory
        self.current_assignments = 0

# currency must only work with ints and can't be negative.
    def add_assignments(self, amount):
       if isinstance(amount, int) and amount > 0:
            self.current_assignments += amount
       else:
           raise ValueError("Please enter an integer bigger than 0 ")
           
    def submit_assigments(self, amount):
        if isinstance(amount, int) and self.current_assignments >= amount:
            self.current_assignments -= amount
        else:
            print("You don't have enough tests to pay for this")
    
    def get_assignments(self):
        return self.current_assignments 
    
    def get_inventory(self):
        return self.current_inventory


    def __repr__(self):
        return f"name:{self.name}, inventory:{self.current_inventory}, assignments: {self.current_assignments}"

#make a player inventory that starts at 0 and can expand
class Inventory:
    def __init__(self):
        self.current_inventory = {}

    def add_to_inventory(self, candy_type, q):
        if candy_type not in self.current_inventory:
            self.current_inventory[candy_type] = 0
        self.current_inventory[candy_type] += q

    def decrease_inventory(self, candy_type, q):
        if candy_type not in self.current_inventory:
            self.current_inventory[candy_type] = 0
        self.current_inventory[candy_type] -= q

    def has_candy(self, candy_type):
        return candy_type in self.current_inventory

    def get_quantity(self, candy_type):
        return self.current_inventory.get(candy_type, 0)

    #print the q/ value of the candy in the bag
    def __repr__(self):
        return f"{self.current_inventory}"
    
        
#make an object for a candy type
class Candy_type:
    def __init__(self, name, colour, flavour ):
        self.colour = colour
        self.flavour = flavour
        self.name = name

#print the name/ key of the candy in the bag
    def __repr__(self):
        return f"{self.name}"
 
# test