class Player:
    def __init__(self,name, inventory):
        self.name = name
        self.inventory = inventory
        self.current_amount = 0

# currency must only work with ints and can't be negative.
    def add_money(self, amount):
       if isinstance(amount, int) and amount > 0:
            self.current_amount += amount
       else:
           raise ValueError("Please enter an integer bigger than 0 ")
           
    def subtract_money(self, amount):
        if isinstance(amount, int) and self.current_amount >= amount:
            self.current_amount -= amount
        else:
            print("You don't have enough tests to pay for this")

    def __repr__(self):
        return f"name:{self.name}, inventory:{self.inventory}, currency: {self.current_amount}"

#make a player inventory that starts at 0 and can expand
class Inventory:
    def __init__(self):
        self.current_inventory = {}

    def add_to_inventory(self, candy_type, q):
        self.current_inventory[candy_type] = q

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

# must only work with ints, can't be negative, is instance int
class Currency:
    def __init__(self):
        self.current_amount = self.set_current_amount
        
    def add_money(self, amount):
        new_amount = self.current_amount + amount
        return new_amount
    
#can't be negative
    def subtract_money(self, amount):
        
        new_amount = self.current_amount - amount
        return new_amount 
    
    def set_current_amount(self):
        return self.new_amount

        

bag = Inventory()
p1 = Player("Super Senior", bag)
drop = Candy_type("drop","black", "salty")
bubblegum = Candy_type("bubblegum", "pink" ,"strawberry")
napoleon = Candy_type("napoleon", "white", "sour")
bag.add_to_inventory(drop, 1)
bag.add_to_inventory(bubblegum, 5)
print(p1.current_amount)
p1.add_money(10)
print(p1.current_amount)
p1.subtract_money(5)
print(p1)