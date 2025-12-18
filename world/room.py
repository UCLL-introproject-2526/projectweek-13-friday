# set rooms na deuren + return done!! je zit niet meer vast :)

import pygame
import random
from ui.prompt import draw_prompt
from player_implementatie.students import Student

class Room:
    def __init__(self, name, return_x):
        self.name = name
        self.return_x = return_x
        self.students = []

    # def students_in_rooms(self):
    #     student1 = Student("Student1")
    #     student2 = Student("student2")
    #     student3 = Student("student3")

        # return [student1, student2, student3]

    def update(self, player, events, game):
        keys = pygame.key.get_pressed()
        player.update(game.clock.get_time() / 1000, keys)

        # player binnen de kamer houden
        player.rect.left = max(player.rect.left, 0)
        player.rect.right = min(player.rect.right, game.WIDTH)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # return op plaats waar je binnenkwam (positielogica)
                game.start_fade("hallway", self.return_x)

    def draw(self, screen, player, game):
        screen.fill((40, 60, 120))

        n_to_draw = min(3, len(self.students))  # pak maximaal 3 studenten, of minder als er minder zijn

        students_to_draw = random.sample(self.students, n_to_draw)
        x = 50
        y = 436
        for student in students_to_draw:
            rect = pygame.Rect(x , y ,50,50)
            pygame.draw.rect(screen, (120, 33, 250), rect)
            x = x + 100
        
        # kamertitle!!!
        font = pygame.font.SysFont(None, 48)
        title = font.render(self.name, True, (255, 255, 255))
        screen.blit(title, (50, 50))
        
        # exit prompt onderaan scherm
        draw_prompt(screen, "Press E to exit room", 640, 680)
        
        player.draw(screen)