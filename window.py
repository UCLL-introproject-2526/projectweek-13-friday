import pygame
from pygame.display import flip
class State:
    def __init__(self):
    
        self.circle_x = 0

    def update(self):
        
        self.circle_x += 1

    def render(self, surface):
        # Clear the screen
        surface.fill((0, 0, 0))

        # Draw the circle at the current x-coordinate
        pygame.draw.circle(
            surface,
            (255, 0, 0),
            (self.circle_x, 384),
            50
        )

        # Copy back buffer to front buffer
        flip()


def create_main_surface():
    screen_size = (1024, 768)
    return pygame.display.set_mode(screen_size)



def main():
    pygame.init()
    surface = create_main_surface()

    state = State()  # startpositie van de cirkel

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        state.update()

        state.render(surface)

       


main()



