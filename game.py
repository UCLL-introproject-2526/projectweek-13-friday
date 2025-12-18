# central game loop
# area management
# fades added!!

import pygame
from entities.player import Player
from world.hallway import Hallway
from world.room import Room
from world.playground import Playground
from world.lab import Lab
from ui.menu import Menu
from world.battle_arena import BattleArena

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
            "battle": BattleArena() # NIEUW!!! test subject for now..
        }
        self.current_area = "hallway"   # spawnpoint (hallway for now.. meest logische)

        self.fading = False
        self.fade_alpha = 0
        self.fade_target = None
        self.fade_spawn_x = 0

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


    # run.. run.. run..
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            events = pygame.event.get() # events worden hier verzameld !!
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                # ---------------- TEST TRIGGER FOR BATTLE --------------
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_b: # Druk op 'B' om te vechten
                            print("Debug: Battle gestart!")
                            self.start_fade("battle", 100)
                # -------- NOT PERMANENT !!!! -------------------------
            
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
                area = self.areas[self.current_area]
                
                if not self.fading:
                    area.update(self.player, events, self)
                    
                    # NIEUW: Check of we in de battle arena zijn en of het gevecht klaar is
                    if self.current_area == "battle":
                        # Als de arena phase weer op "intro" staat (door de E-toets reset)
                        # OF als je een variabele 'battle_concluded' hebt:
                        if area.phase == "intro" and area.winner is not None:
                             # We gaan terug naar de hallway
                             # Je kunt hier kiezen: altijd naar 100, of bewaar de oude x
                             spawn_pos = 100 if area.winner == "enemy" else self.player.rect.x
                             self.start_fade("hallway", spawn_pos)
                             area.winner = None # Reset winner zodat hij niet blijft faden

                # teken de wereld
                self.screen.fill((30, 30, 30))
                area.draw(self.screen, self.player, self)
            
                # TRIGGER DE DEUR PROMPTS HIER
                if self.current_area == "hallway" and not self.fading:
                    # ... je bestaande deur logica ...
                    offset_x = max(0, self.player.rect.centerx - 640)
                    offset_x = min(offset_x, area.width - 1280)
                    for door in area.doors:
                        door.update(self.player, events, self, offset_x)
                
                if self.fading:
                    self.handle_fade()
            pygame.display.flip()
        pygame.quit()