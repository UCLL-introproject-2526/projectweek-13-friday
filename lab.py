from ingredient import Ingredient

class MixingPot:
    def __init__(self):
        self.contents = []

    def add(self, ingredient):
        self.contents.append(ingredient)

    # alleen mix als combinatie met 2 ingredienten is
    def mix(self):
        if len(self.contents) < 2:
            return None