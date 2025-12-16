import pygame
from Environment.changing_rooms import create_rooms
from avatar_movement import Avatar

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

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

    pygame.display.flip()

pygame.quit()