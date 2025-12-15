class Player:
    def __init__(self,current_inventory):
        self.inventory = current_inventory
        self.current_currency = 0
    def add_currency(self, currency):
        self.current_currency += currency
        pass

#make a player inventory that starts at 0 and can expand
class Inventory:
    def __init__(self):
        self.current_inventory = {}

    def add_to_inventory(self, candy_type, q):
        self.current_inventory[candy_type] = q
    def __repr__(self):
        return f'Inventory(\'{self.current_inventory})'
    
        
#make an object for a candy type
class Candy_type:
    def __init__(self,colour, flavour ):
        self.colour = colour
        self.flavour = flavour


bag = Inventory()
bag.add_to_inventory('drop', 1)
print(bag)