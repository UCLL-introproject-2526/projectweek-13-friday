# automatic return to hallway OF je gaat naar je lab.. confirmation nodig!

import pygame
from ui.prompt import draw_prompt

class Playground:
    def __init__(self):
        self.confirm_lab = False

    def update(self, player, events, game):
        # keys = pygame.key.get_pressed()
        # player.update(game.clock.get_time() / 1000, keys)

        dt = game.clock.get_time() / 1000
        keys = pygame.key.get_pressed()
        player.update(dt, keys)

        # # contact w muur links = METEEN terug naar hallway (no 'press E to....')
        # if player.rect.left <= 0:
        #     player.rect.left = 0
        #     game.start_fade("hallway", 2900)
        #     return
        
        if player.rect.left <= 0:
            player.rect.left = 0
            # fix problem: spawn de speler in Hallway rechts
            # zodat hij niet direct de trigger 'rect.right >= width' raakt ??
            spawn_x = 3000 - 200 
            game.start_fade("hallway", spawn_x)

        if player.rect.right >= game.WIDTH:
            player.rect.right = game.WIDTH
            self.confirm_lab = True
        else:
            self.confirm_lab = False

        for event in events:
            if self.confirm_lab and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game.start_fade("lab", 50) # go to labo!!!
                    self.confirm_lab = False # reset
                    return # Belangrijk: stop verdere update // lowk ff geen idee.. ma het werkt
                if event.key == pygame.K_ESCAPE:
                    player.rect.x -= 20
                    self.confirm_lab = False

    def draw(self, screen, player, game):
        screen.fill((80, 150, 80))
        player.draw(screen)
        if self.confirm_lab:
            draw_prompt(screen, "Head home? (E / ESC)", 640, 360)