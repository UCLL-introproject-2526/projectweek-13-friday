# set rooms na deuren + return done!! je zit niet meer vast :)

import pygame
from ui.prompt import draw_prompt

class Room:
    def __init__(self, name, return_x):
        self.name = name
        self.return_x = return_x

    def update(self, player, events, game):
        keys = pygame.key.get_pressed()
        player.update(game.clock.get_time() / 1000, keys)

        # player binnen de kamer houden
        player.rect.left = max(player.rect.left, 0)
        player.rect.right = min(player.rect.right, game.WIDTH)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # return op plaats waar je binnenkwam (positielogica)
                game.start_fade("hallway", self.return_x)

    def draw(self, screen, player, game):
        screen.fill((40, 60, 120))
        
        # kamertitle!!!
        font = pygame.font.SysFont(None, 48)
        title = font.render(self.name, True, (255, 255, 255))
        screen.blit(title, (50, 50))
        
        # exit prompt onderaan scherm
        draw_prompt(screen, "Press E to exit room", 640, 680)
        
        player.draw(screen)