# text helpers!!

import pygame

def draw_prompt(screen, text, x, y):
    font = pygame.font.SysFont(None, 28)
    surf = font.render(text, True, (255, 255, 255))
    rect = surf.get_rect(center=(x, y))
    bg_rect = rect.inflate(10, 10) # schaduw text...
    pygame.draw.rect(screen, (0, 0, 0), bg_rect)
    screen.blit(surf, rect)