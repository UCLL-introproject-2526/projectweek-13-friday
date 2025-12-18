# lange gang, camera moves w player

import pygame
from world.door import Door

class Hallway:
    def __init__(self):
        self.width = 3000       # width (totaal)
        self.doors = [          # deuren + specifieke posities
            Door(600, "classroom"),
            Door(1200, "bathroom"),
            Door(1800, "principal")
        ]

    def update(self, player, events, game):
        dt = game.clock.get_time() / 1000
        keys = pygame.key.get_pressed()
        
        # update player (beweging + animatie staat in player.py)
        player.update(dt, keys)

        # check overgang naar playground (rechts)
        if player.rect.right >= self.width:
            player.rect.right = self.width
            game.start_fade("playground", 50)
            return

        # vaste muur (links)
        if player.rect.left <= 0:
            player.rect.left = 0

        # camera offset calculatie
        offset_x = max(0, player.rect.centerx - 640)
        offset_x = min(offset_x, self.width - 1280)

        # update deuren voor pop-up text
        for door in self.doors:
            door.update(player, events, game, offset_x)

    def draw(self, screen, player, game):
        # fix: calculatie overgenomen 2 comments erboven
        offset_x = max(0, player.rect.centerx - 640)
        offset_x = min(offset_x, self.width - 1280)

        screen.fill((70, 70, 70))       # bg color.. (muren)

        # draw tha floooor
        pygame.draw.rect(screen, (100, 100, 100), (-offset_x, 580, self.width, 140))
        # pygame.draw.line(screen, (200, 200, 200), (0, 580), (game.WIDTH, 580), 2) # tekent extra lijn.. idk didnt rlly like it

        # deuren..
        for door in self.doors:
            door.draw(screen, offset_x)

        player.draw(screen, offset_x)