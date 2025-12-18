import pygame

class Menu:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.font = pygame.font.SysFont(None, 74)
        self.txt = self.font.render("super epic cool game", True, (255, 255, 255))
        self.sub_txt = pygame.font.SysFont(None, 36).render("Press SPACE to Start", True, (200, 200, 200))

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "playing"
        return "menu" # blijf in menu als er niks gebeurt !!

    def draw(self, screen):
        screen.fill((20, 20, 40))
        screen.blit(self.txt, (self.w//2 - self.txt.get_width()//2, 200))
        screen.blit(self.sub_txt, (self.w//2 - self.sub_txt.get_width()//2, 400))