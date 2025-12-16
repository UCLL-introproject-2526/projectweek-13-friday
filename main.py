import pygame
# import alle kamers..
from Environment.changing_rooms import create_rooms

pygame.init()

# game window set-up
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # frame snelheid..? idk nog uit te zoeken.

# slaagt alle kamers op in een lijst
rooms = create_rooms() 
current_room = rooms[0] # eerste kamer = huidige kamer

# extra om game te laten runnen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(current_room.image, (0, 0)) # tekent de afbeelding van de huidige kamer op het scherm
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
