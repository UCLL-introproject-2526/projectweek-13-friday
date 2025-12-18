# central game loop
# area management
# fades added!!

import pygame
from entities.player_mechanics import Player 
from world.hallway import Hallway
from world.room import Room
from world.playground import Playground
from world.lab import Lab
from ui.menu import Menu
from ui.lab import *
from ingredients.ingredient import Ingredient, Mixingpot, IngredientSprite, CandySprite, candy_images
from player_implementatie.player import Inventory, Player_
from player_implementatie.transaction import Transaction
from player_implementatie.students import Student
import random


# from world.battle_arena import BattleArena

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("GAMEGAMEGAMEGAME")
        self.clock = pygame.time.Clock()
        self.running = True

        # menu initialiseren..
        self.menu = Menu(self.WIDTH, self.HEIGHT)
        self.state = "menu"  # we beginnen sws in het menu

        self.player = Player(100, 520)
        self.areas = {
            "hallway": Hallway(),
            "classroom": Room("Classroom", 600), # 600 is de x van de deur      AANPASBAAR !!!! moet wel passen met locatie van deuren.. 
            "bathroom": Room("Bathroom", 1200),  # 1200 is de x van de deur     AANPASBAAR !!!! bv kijk bij Hallway...
            "principal": Room("Principal Office", 1800),
            "playground": Playground(),
            "lab": Lab(),
            # "battle": BattleArena() # NIEUW!!! test subject for now..
        }
        self.current_area = "hallway"   # spawnpoint (hallway for now.. meest logische)

        rooms = []
        for area in self.areas.values():
            if type(area) == Room:
                rooms.append(area)

        self.students = [
            Student("Alice", (60, 255, 100)),
            Student("Bob", (250, 230, 240)),
            Student("Student1", (66, 130, 240)),
            # Student("student2", (203, 20, 240)),
            # Student("student3",(255, 255, 255)),
            # Student("Student4", (10, 255, 240)),
            # Student("Student5", (200, 130, 10)),
            # Student("student6,",(6, 130, 240)),
            # Student("student7", (66, 106, 240)),
            # Student("Student8", (66, 200, 20)),
        ]

        for student in self.students:
            random.choice(rooms).students.append(student)

        for room in rooms:
            n_to_draw = min(3, len(room.students))
            room.students_to_draw = random.sample(room.students, n_to_draw)



        self.fading = False
        self.fade_alpha = 0
        self.fade_target = None
        self.fade_spawn_x = 0


        # ingredient stuff
        self.mixing_pot = Mixingpot()


        # ingredienten als sprites
        self.ingredient_sprites = [
        IngredientSprite(Ingredient("rood","kleur"), "ingredients/kleur/snoep_red.png", (800,150)),
        IngredientSprite(Ingredient("geel","kleur"), "ingredients/kleur/snoep_yellow.png", (950,150)),
        IngredientSprite(Ingredient("blauw","kleur"), "ingredients/kleur/snoep_blue.png", (1100,150)),
        IngredientSprite(Ingredient("appel","smaak"), "ingredients/smaak/appel.png", (800,275)),
        IngredientSprite(Ingredient("banaan","smaak"), "ingredients/smaak/banaan.png", (950,275)),
        IngredientSprite(Ingredient("druif","smaak"), "ingredients/smaak/grape.png", (1100,275))
        ]

        self.current_candy_sprite = None

        # player inventory
        self.player_inventory = Inventory()
        self.player_info = Player_("Speler1", self.player_inventory)

        # inventory slots
        self.inventory_slots = [
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0}
]



    # swish swish..
    def switch_area(self, area_name, spawn_x):
        self.current_area = area_name
        self.player.rect.x = spawn_x

    # idk zachtere overgang (extra addition)
    def start_fade(self, target_area, spawn_x):
        if not self.fading:
            self.fading = True
            self.fade_target = target_area
            self.fade_spawn_x = spawn_x
            self.fade_alpha = 0

    def handle_fade(self):
        fade_surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        fade_surface.fill((0, 0, 0))
        self.fade_alpha += 25 
        fade_surface.set_alpha(self.fade_alpha)
        self.screen.blit(fade_surface, (0, 0))

        if self.fade_alpha >= 255:
            self.switch_area(self.fade_target, self.fade_spawn_x)
            self.fading = False

    def handle_ingredient_clicks(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for sprite in self.ingredient_sprites:
                    if sprite.is_clicked(mouse_pos):
                        candy = self.mixing_pot.add_ingredient(sprite.ingredient)
                        if candy:
                            
                            # update inventory
                            for slot in self.inventory_slots:
                                if slot["name"] == candy:
                                    slot["count"] += 1
                                    return
                            for slot in self.inventory_slots:
                                if slot["name"] is None:
                                    slot["name"] = candy
                                    slot["count"] = 1
                                    return
                            self.player.current_inventory.add_to_inventory(candy, 1)



    # run.. run.. run..
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            events = pygame.event.get() # events worden hier verzameld !!
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # # ---------------- TEST TRIGGER FOR BATTLE --------------
            # if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_b: # Druk op 'B' om te vechten
            #             print("Debug: Battle gestart!")
            #             self.start_fade("battle", 100)
            # # -------- NOT PERMANENT !!!! -------------------------
            
            self.screen.fill((0, 0, 0)) # menu fix: "wis het scherm aan begin van elke fix"

                
            # if not self.fading:
            #     area = self.areas[self.current_area]
            #     area.update(self.player, events, self)

            # -- MENU STUFF !!
            if self.state == "menu":
                self.state = self.menu.update(events)
                self.menu.draw(self.screen)

            # -- GAMEPLAY ITSELF.. 
            elif self.state == "playing":
                if not self.fading:
                    area = self.areas[self.current_area]
                    area.update(self.player, events, self)

                # teken de wereld
                area = self.areas[self.current_area]
                self.screen.fill((30, 30, 30))
                area.draw(self.screen, self.player, self)
            
                # TRIGGER DE DEUR PROMPTS HIER (nadat de area getekend is!!!)
                if self.current_area == "hallway" and not self.fading:
                    offset_x = max(0, self.player.rect.centerx - 640)
                    offset_x = min(offset_x, area.width - 1280)
                    for door in area.doors:
                        door.update(self.player, events, self, offset_x)
                
                if self.fading:
                    self.handle_fade()
                
                # ingredient-logica
                if self.current_area == "lab" and not self.fading:
                    self.handle_ingredient_clicks(events)
                
                draw_lab_ui(self)
                    

                
                
            pygame.display.flip()
        pygame.quit()