import pygame

class Avatar:
    def __init__(self, x, y, image_path):
        self.position = [x, y]
        self.image = pygame.image.load(image_path).convert_alpha()
        self.speed = 200

    def update(self, elapsed_seconds, keys):
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed * elapsed_seconds
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed * elapsed_seconds
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed * elapsed_seconds
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed * elapsed_seconds

    def render(self, surface):
        surface.blit(self.image, self.position)