import random
#speed up the process of making students by randomizing a location that hasn't 
#been used last time

class Student:
    def __init__(self, name):
        self.name = name
        self.favourite_sweets = []
        self.order = {}

#add an order to put in the demand dict,  key: order , value candy_type, amount
#randomize a type from the recipe.txt file and randomze an amount from 1-10
#check if it can acces the recipe file -> it's in a folder

    def add_order(self):
        amount = random.randint(1,10)
        with open("delivery_texts/recipes.txt", 'r', encoding= 'utf-8') as file:
            recipe_list = file.readlines()
            for line  in recipe_list:
                name = line.strip().split(':')
                self.favourite_sweets.append(name[0])
                
              
        self.order["order"] = random.choice(self.favourite_sweets), amount

    def __repr__(self):
        if self.order["order"][1] > 1:
           return f'{self.name} wants to order {self.order["order"][1]} pieces of your {self.order["order"][0]} supply'
        else:
            return f'{self.name} wants to order {self.order["order"][1]} piece of your {self.order["order"][0]} supply'
    
#when we reach higher levels, students may have more orders
    def select_order(self,):
        pass
