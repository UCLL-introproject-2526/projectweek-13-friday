import pygame
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((1280, 720))

rooms = []
rooms_path = Path(__file__).parent.parent / "Rooms"

for img_path in rooms_path.glob("*.png"):
    rooms.append(pygame.image.load(str(img_path)).convert())

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(rooms[0], (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()