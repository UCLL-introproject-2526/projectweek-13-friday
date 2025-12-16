# import pygame
# # import alle kamers..
# from Environment.changing_rooms import create_rooms

# pygame.init()

# # game window.. info..
# WIDTH, HEIGHT = 1280, 720
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()  # frame snelheid..? idk nog uit te zoeken.

# # slaagt alle kamers op in een lijst
# rooms = create_rooms() 
# current_room = rooms[0] # eerste kamer = huidige kamer

# # extra om game te laten runnen
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.blit(current_room.image, (0, 0)) # tekent de afbeelding van de huidige kamer op het scherm
#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()
# ------------------------------------------------------------------------------------------------

import pygame
from Environment.changing_rooms import create_rooms
from avatar_movement import Avatar

pygame.init()




WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
banana_image = pygame.image.load("banaan.png").convert_alpha()
banana_image = pygame.transform.scale(banana_image, (256, 256))
banana_pos = (WIDTH // 2 - 128, HEIGHT // 2 - 128)


# Rooms
rooms = create_rooms()
current_room = rooms[0]

# Player
player = Avatar(600, 400, "Chicken.png")

running = True
while running:
    elapsed_seconds = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(elapsed_seconds, keys)

    # ---- ROOM SWITCHING ----
    if player.position[0] + player.image.get_width() < 0 and current_room.left is not None:
        current_room = rooms[current_room.left]
        player.position[0] = WIDTH

    if player.position[0] > WIDTH and current_room.right is not None:
        current_room = rooms[current_room.right]
        player.position[0] = -player.image.get_width()

    # ---- DRAW ----
    screen.blit(current_room.image, (0, 0))
    player.render(screen)
    # ---- DRAW ----
    screen.blit(current_room.image, (0, 0))

    screen.blit(banana_image, banana_pos)  # <-- BANAAN



    pygame.display.flip()

pygame.quit()
