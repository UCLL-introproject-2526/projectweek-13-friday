import pygame

# dictionary met key tuple kleur en smaak en value recept, recept wil je later in inventory
recipes = {
    ("rood", "appel"): "Rode appel snoep",
    ("rood", "banaan"): "Rode banaan snoep",
    ("rood", "druif"): "Rode druif snoep",

    ("geel", "appel"): "Gele appel snoep",
    ("geel", "banaan"): "Gele banaan snoep",
    ("geel", "druif"): "Gele druif snoep",

    ("blauw", "appel"): "Blauwe appel snoep",
    ("blauw", "banaan"): "Blauwe banaan snoep",
    ("blauw", "druif"): "Blauwe druif snoep",
}


# 1 klikbaar ingredient vb. rood, appel ...
class Ingredient:
    def __init__(self, name, type):
        self.name = name    # inhoud ingerdient
        self.type = type     # soort ingredient: kleur of smaak



class Mixingpot:
    def __init__(self):
        self.kleur = None  # er is nog geen kleur gekozen
        self.smaak = None  # er is nog geen smaak gekozen



    # functie wordt aangeroepen als speler klikt op een ingredient
    def add_ingredient(self, ingredient):
        if ingredient.type == "kleur":      # eerst kijken wat voor ingredient het is
            self.kleur = ingredient.name
        if ingredient.type == "smaak":
            self.smaak = ingredient.name

        if self.kleur and self.smaak:       # checkt of er een smaak en kleur is gekozen
            return self.mix()
        
        return None        # wachten tot er 2 dingen zijn gekozen
    

    # functie wordt aangeroepen als er 2 ingredienten zijn gekozen

    def mix(self):
        key = (self.kleur, self.smaak)     # maakt de key


        if key in recipes:          # zoekt de key in recepten en geeft de value
            candy = recipes[key]
        else:
            candy = None            # geen recept gevonden
        

        self.kleur = None       # mixing pot leeg maken
        self.smaak = None
        return candy        # geeft het resultaat terug



# ingredient object aanmaken : kleuren
# rood = Ingredient("rood", "kleur")
# geel = Ingredient("geel", "kleur")
# blauw = Ingredient("blauw", "kleur")


# # ingredient objecten aanmaken : smaken
# appel = Ingredient("appel", "smaak")
# banaan = Ingredient("banaan", "smaak")
# druif = Ingredient("druif", "smaak")
#---------------------------------------------------------------------------------------------------------------


# zichtbaar ingredient op scherm
class IngredientSprite:
    def __init__(self, ingredient, image_path, pos):
        self.ingredient = ingredient
        # self.image = pygame.image.load(image_path).convert_alpha() 
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (128, 128))

        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# # sprite objecten aanmaken
# rood_sprite = IngredientSprite(rood, "ingredient_assets/kleur/snoep_red.png", (100, 500))
# geel_sprite = IngredientSprite(geel, "ingredient_assets/kleur/snoep_yellow.png", (200, 500))
# blauw_sprite = IngredientSprite(blauw, "ingredient_assets/kleur/snoep_blue.png", (300, 500))


# appel_sprite = IngredientSprite(appel, "ingredient_assets/smaak/appel.png", (600, 500))
# banaan_sprite = IngredientSprite(banaan, "ingredient_assets/smaak/banaan.png", (700, 500))
# druif_sprite = IngredientSprite(druif, "ingredient_assets/smaak/druif.png", (800, 500))


# # lijst met sprites:
# ingredient_sprites = [
#     rood_sprite, geel_sprite, blauw_sprite,
#     appel_sprite, banaan_sprite, druif_sprite
# ]

# # afbeeldingen koppelen aan juiste snoep recept

candy_images = {
    # Rood
    "Rode appel snoep": "ingredients/snoep/rood_appel.png",
    "Rode banaan snoep": "ingredients/snoep/rood_banaan.png",
    "Rode druif snoep": "ingredients/snoep/rood_grape.png",

    # Geel
    "Gele appel snoep": "ingredients/snoep/geel_appel.png",
    "Gele banaan snoep": "ingredients/snoep/geel_banaan.png",
    "Gele druif snoep": "ingredients/snoep/geel_grape.png",

    # Blauw
    "Blauwe appel snoep": "ingredients/snoep/blauw_appel.png",
    "Blauwe banaan snoep": "ingredients/snoep/blauw_banaan.png",
    "Blauwe druif snoep": "ingredients/snoep/blauw_grape.png",
}


# zichtbaar snoepje op scherm
class CandySprite:
    def __init__(self, candy_name, pos):
        # self.image = pygame.image.load(candy_images[candy_name]).convert_alpha()
        self.image = pygame.transform.scale(pygame.image.load(candy_images[candy_name]).convert_alpha(), (82, 82))
        self.rect = self.image.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)



