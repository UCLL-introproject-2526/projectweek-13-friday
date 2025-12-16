import pygame
from Environment.changing_rooms import create_rooms
from avatar_movement import Avatar

class Game:
    def __init__(self):
        # pygame initialisatie
        pygame.init()
        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Super Senior Graduation")
        self.clock = pygame.time.Clock()

        # maak rooms + schaal achtergronden automatisch naar scherm
        self.rooms = create_rooms(self.WIDTH, self.HEIGHT)
        self.current_room = self.rooms[0]

        # current room index (voor de simpele lijst-implementatie)
        self.current_room_index = 0
        self.current_room = self.rooms[self.current_room_index]

        # player
        self.player = Avatar(600, 400, "Chicken.png")

        # game loop
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def switch_rooms(self):
        # moved = False

        # # Naar links
        # if self.player.position[0] < 0 and self.current_room_index > 0:
        #     self.current_room_index -= 1
        #     self.player.position[0] = self.WIDTH - 1
        #     moved = True

        # # Naar rechts
        # elif self.player.position[0] + self.player.image.get_width() > self.WIDTH and self.current_room_index < len(self.rooms) - 1:
        #     self.current_room_index += 1
        #     self.player.position[0] = 1 - self.player.image.get_width()
        #     moved = True

        # # Update huidige kamer alleen als we daadwerkelijk gewisseld zijn
        # if moved:
        #     self.current_room = self.rooms[self.current_room_index]
        # ------------------------------------------------------------------
        # # huidige kamer
        # idx = self.current_room_index

        # # naar links
        # if self.player.position[0] < 0 and idx > 0:
        #     idx -= 1
        #     self.player.position[0] = self.WIDTH
        
        # # naar rechts
        # elif self.player.position[0] > self.WIDTH and idx < len(self.rooms) - 1:
        #     idx += 1
        #     self.player.position[0] = -self.player.image.get_width()

        # # update current room!
        # self.current_room_index = idx
        # self.current_room = self.rooms[idx]
        

        # -------------------- vorige implementatie --------------------------
        # Controleer of de speler buiten het scherm gaat en switch van kamer 
        # Naar links
        if self.player.position[0] + self.player.image.get_width() < 0 and self.current_room.left is not None:
            self.current_room = self.rooms[self.current_room.left]
            self.player.position[0] = self.WIDTH

        # Naar rechts
        if self.player.position[0] > self.WIDTH and self.current_room.right is not None:
            self.current_room = self.rooms[self.current_room.right]
            self.player.position[0] = -self.player.image.get_width()

    def update(self, elapsed_seconds):
        # Update speler en kamer 
        keys = pygame.key.get_pressed()
        self.player.update(elapsed_seconds, keys)
        self.switch_rooms()

    def draw(self):
        # Teken huidige kamer en speler
        self.screen.blit(self.current_room.image, (0, 0))
        self.player.render(self.screen)
        pygame.display.flip()

    def run(self):
        # Hoofdgame loop
        while self.running:
            elapsed_seconds = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(elapsed_seconds)
            self.draw()

        pygame.quit()
