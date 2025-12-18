import pygame
from Environment.changing_rooms import create_rooms
from avatar_movement import Avatar
from ingredient_assets.ingredient import Ingredient, Mixingpot, IngredientSprite, CandySprite, recipes, candy_images
from player_implementatie.player import *



class Game:
    def __init__(self):
        # pygame initialisatie
        pygame.init()
        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Super Senior Graduation")
        self.clock = pygame.time.Clock()

        # maak rooms + schaal achtergronden automatisch naar scherm
        self.rooms = create_rooms(self.WIDTH, self.HEIGHT)
        self.current_room = self.rooms[0]

        # current room index (voor de simpele lijst-implementatie)
        self.current_room_index = 0
        self.current_room = self.rooms[self.current_room_index]

        # player

        self.player_inventory = Inventory()
        self.player = Player("Speler1", self.player_inventory)
        self.player_avatar = Avatar(600, "Chicken.png", self.player)

        # game loop
        self.running = True

        # ingredienten
        self.mixing_pot = Mixingpot()
        self.ingredient_sprites = self.ingredient_sprites = [
    IngredientSprite(Ingredient("rood","kleur"), "ingredient_assets/kleur/snoep_red.png", (800,150)),
    IngredientSprite(Ingredient("geel","kleur"), "ingredient_assets/kleur/snoep_yellow.png", (950,150)),
    IngredientSprite(Ingredient("blauw","kleur"), "ingredient_assets/kleur/snoep_blue.png", (1100,150)),

    IngredientSprite(Ingredient("appel","smaak"), "ingredient_assets/smaak/appel.png", (800,275)),
    IngredientSprite(Ingredient("banaan","smaak"), "ingredient_assets/smaak/banaan.png", (950,275)),
    IngredientSprite(Ingredient("druif","smaak"), "ingredient_assets/smaak/grape.png", (1100,275))
    ]
       # lijst van alle IngredientSprite objecten
        self.current_candy_sprite = None


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

        




    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        #controleert of speler met muis klikt
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # haalt postie muis op, zo weten we welk ingredient is geklikt

                for sprite in self.ingredient_sprites:     # kijken op welke sprite is geklikt 
                    if sprite.is_clicked(mouse_pos):        # kijken of muis positie overeen komt
                        candy = self.mixing_pot.add_ingredient(sprite.ingredient)   #stuurt ingredient naar mixing pot
                        if candy:
                            self.current_candy_sprite = CandySprite(candy, (640, 360))
                             # 1️⃣ Eerst kijken: bestaat dit snoepje al?
                            for slot in self.inventory_slots:
                                if slot["name"] == candy:
                                    slot["count"] += 1
                                    return  # stop hier → klaar
                            
                               # 2️⃣ Anders: eerste lege slot zoeken
                            for slot in self.inventory_slots:
                                if slot["name"] is None:
                                    slot["name"] = candy
                                    slot["count"] = 1
                                    return
                            # Voeg candy toe aan player inventory
                            self.player.current_inventory.add_to_inventory(candy, 1)



    def switch_rooms(self):
        # moved = False

        # # Naar links
        # if self.player.position[0] < 0 and self.current_room_index > 0:
        #     self.current_room_index -= 1
        #     self.player.position[0] = self.WIDTH - 1
        #     moved = True

        # # Naar rechts
        # elif self.player.position[0] + self.player.image.get_width() > self.WIDTH and self.current_room_index < len(self.rooms) - 1:
        #     self.current_room_index += 1
        #     self.player.position[0] = 1 - self.player.image.get_width()
        #     moved = True

        # # Update huidige kamer alleen als we daadwerkelijk gewisseld zijn
        # if moved:
        #     self.current_room = self.rooms[self.current_room_index]
        # ------------------------------------------------------------------
        # # huidige kamer
        # idx = self.current_room_index

        # # naar links
        # if self.player.position[0] < 0 and idx > 0:
        #     idx -= 1
        #     self.player.position[0] = self.WIDTH
        
        # # naar rechts
        # elif self.player.position[0] > self.WIDTH and idx < len(self.rooms) - 1:
        #     idx += 1
        #     self.player.position[0] = -self.player.image.get_width()

        # # update current room!
        # self.current_room_index = idx
        # self.current_room = self.rooms[idx]
        

    # -------------------- vorige implementatie --------------------------

        # # Controleer of de speler buiten het scherm gaat en switch van kamer 
        # # Naar links
        # if self.player.position[0] + self.player.image.get_width() < 0 and self.current_room.left is not None:
        #     self.current_room = self.rooms[self.current_room.left]
        #     self.player.position[0] = self.WIDTH

        # # Naar rechts
        # if self.player.position[0] > self.WIDTH and self.current_room.right is not None:
        #     self.current_room = self.rooms[self.current_room.right]
        #     self.player.position[0] = -self.player.image.get_width()

    # ---------------------------------------------------------------------------------------------------------

        player_width = self.player_avatar.image.get_width()

        # LINKS
        if self.player_avatar.position[0] < 0:
            if self.current_room_index > 0:
                self.current_room_index -= 1
                self.current_room = self.rooms[self.current_room_index]
                self.player_avatar.position[0] = self.WIDTH - player_width
            else:
                self.player_avatar.position[0] = 0

        # RECHTS
        elif self.player_avatar.position[0] + player_width > self.WIDTH:
            if self.current_room_index < len(self.rooms) - 1:
                self.current_room_index += 1
                self.current_room = self.rooms[self.current_room_index]
                self.player_avatar.position[0] = 0
            else:
                self.player_avatar.position[0] = self.WIDTH - player_width    

    def update(self, elapsed_seconds):
        # Update speler en kamer 
        keys = pygame.key.get_pressed()
        self.player_avatar.update(elapsed_seconds, keys)
        self.switch_rooms()

    def draw(self):
        # Teken huidige kamer en speler
        self.screen.blit(self.current_room.image, (0, 0))
        self.player_avatar.render(self.screen)
            
        # --- Teken box achter ingredienten ---
        # Bepaal de grootte van de box (past bij je sprites)
        if self.current_room == self.rooms[6]:
            box_rect = pygame.Rect(780, 130, 450, 320)  # (x, y, width, height)
            pygame.draw.rect(self.screen, (50, 50, 50), box_rect)  # donkergrijze box
            pygame.draw.rect(self.screen, (255, 255, 255), box_rect, 2)  # optioneel witte rand

        inv_rect = pygame.Rect(10, 10, 675, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (50, 50, 50), inv_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_rect, 2)  # optioneel witte rand

        inv_item1_rect = pygame.Rect(10, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item1_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item1_rect, 2)  # optioneel witte rand

        inv_item2_rect = pygame.Rect(85, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item2_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item2_rect, 2)  # optioneel witte rand

        inv_item3_rect = pygame.Rect(160, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item3_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item3_rect, 2)  # optioneel witte rand

        inv_item4_rect = pygame.Rect(235, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item4_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item4_rect, 2)  # optioneel witte 
        
        inv_item5_rect = pygame.Rect(310, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item5_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item5_rect, 2)  # optioneel witte rand

        inv_item6_rect = pygame.Rect(385, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item6_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item6_rect, 2)  # optioneel witte rand

        inv_item7_rect = pygame.Rect(460, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item7_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item7_rect, 2)  # optioneel witte 
        
        inv_item8_rect = pygame.Rect(535, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item8_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item8_rect, 2)  # optioneel witte rand

        inv_item9_rect = pygame.Rect(610, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item9_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item9_rect, 2)  # optioneel witte rand


        inventory_rects = [
    inv_item1_rect,
    inv_item2_rect,
    inv_item3_rect,
    inv_item4_rect,
    inv_item5_rect,
    inv_item6_rect,
    inv_item7_rect,
    inv_item8_rect,
    inv_item9_rect,
]
        
        font = pygame.font.Font(None, 28)

        for i in range(len(self.inventory_slots)):  
            slot = self.inventory_slots[i]

            if slot["name"] is not None:
                rect = inventory_rects[i]

                # snoep-afbeelding
                image_path = candy_images[slot["name"]]
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (64, 64))

                self.screen.blit(
                    image,
                    (rect.x + 5, rect.y + 5)
                )

                # teller``
                if slot["count"] > 1:
                    text = font.render(str(slot["count"]), True, (255, 255, 255))
                    self.screen.blit(
                        text,
                        (rect.right - 20, rect.bottom - 20)
                    )

        if self.current_room == self.rooms[6]:
            # teken alle ingrediënten
            for sprite in self.ingredient_sprites:
                sprite.draw(self.screen)

        # # teken gemixt snoepje (als er een is)
        # if self.current_candy_sprite:
        #     self.current_candy_sprite.draw(self.screen)

        pygame.display.flip()

    def run(self):
        # Hoofdgame loop
        while self.running:
            elapsed_seconds = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(elapsed_seconds)
            self.draw()

        pygame.quit()
