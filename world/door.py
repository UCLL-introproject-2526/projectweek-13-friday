# deur + hover stuff

import pygame
from ui.prompt import draw_prompt

class Door:
    def __init__(self, x, target_area):
        self.rect = pygame.Rect(x, 400, 100, 180)
        self.target_area = target_area

    def update(self, player, events, game, offset_x):
        if self.rect.colliderect(player.rect):
            draw_prompt(
                game.screen,
                "Press E to enter room",
                self.rect.centerx - offset_x,
                self.rect.top - 30
            )
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    game.start_fade(self.target_area, 200)

    def draw(self, screen, offset_x):
        r = self.rect.copy()
        r.x -= offset_x
        pygame.draw.rect(screen, (120, 60, 0), r)                               # bruin v deur zelf
        pygame.draw.rect(screen, (255, 255, 255), r, 3)                         # witte rand
        pygame.draw.circle(screen, (200, 200, 0), (r.right - 15, r.centery), 6) # deur klink