import pygame
from ui.prompt import draw_prompt

class Lab:
    def __init__(self):
        self.name = "Lab"

    def update(self, player, events, game):
        keys = pygame.key.get_pressed()
        player.update(game.clock.get_time() / 1000, keys)

        player.rect.left = max(player.rect.left, 0)
        player.rect.right = min(player.rect.right, game.WIDTH)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # ga terug naar playground, spawn aan de rechterkant
                game.start_fade("playground", 1100)

    def draw(self, screen, player, game):
        screen.fill((50, 50, 80))
        font = pygame.font.SysFont(None, 48)
        title = font.render(self.name, True, (255, 255, 255))
        screen.blit(title, (50, 50))
        
        draw_prompt(screen, "Press E to leave Lab", 640, 680)
        player.draw(screen)