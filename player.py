class Player:
    def __init__(self,current_inventory, current_currency):
        self.inventory = current_inventory
        self.currency = current_currency
        pass

class Inventory:
    def __init__(self):
        self.current_inventory = {}

    def add_to_inventory(self, type, q):
        self.current_inventory[type] = q
    def __repr__(self):
        return f'Inventory(\'{self.current_inventory})'
    
        

class Candy_type:
    def __init__(self,colour, flavour ):
        pass


bag = Inventory()
bag.add_to_inventory('drop', 1)
print(bag)