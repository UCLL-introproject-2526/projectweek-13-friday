# # import pygame
# # from pygame.display import flip

# # # Functie om de surface te wissen
# # def clear_surface(surface):
# #     surface.fill((0, 0, 0))



# # class Avatar:
# #     def __init__(self, x, y, image_path):
# #         self.position = [x, y]  # private veld voor positie
# #         self.image = pygame.image.load(image_path).convert_alpha()  # laad afbeelding

# #     # tekent avatar op oppervlakt
# #     def render(self, surface):
# #         surface.blit(self.image, self.position) 


# # class State:
# #     def __init__(self):
# #         self.avatar = Avatar(512, 384, "Chicken.png")
# #         self.speed = 200


# #     def update(self, elapsed_seconds, keys):
# #         # Beweeg de cirkel afhankelijk van welke pijltjes ingedrukt zijn
# #         if keys[pygame.K_RIGHT]:
# #             self.avatar.position[0] += self.speed * elapsed_seconds
# #         if keys[pygame.K_LEFT]:
# #             self.avatar.position[0] -= self.speed * elapsed_seconds
# #         if keys[pygame.K_DOWN]:
# #             self.avatar.position[1] += self.speed * elapsed_seconds
# #         if keys[pygame.K_UP]:
# #             self.avatar.position[1] -= self.speed * elapsed_seconds

# #         # Houd de avatar binnen het scherm
# #         self.avatar.position[0] = max(0, min(1024 - self.avatar.image.get_width(), self.avatar.position[0]))
# #         self.avatar.position[1] = max(0, min(768 - self.avatar.image.get_height(), self.avatar.position[1]))

# #     def render(self, surface):
# #         # Wis de surface aan het begin van elke frame
# #         clear_surface(surface)

# #         self.avatar.render(surface)
# #         pygame.display.flip()


# # def create_main_surface():
# #     screen_size = (1024, 768)
# #     return pygame.display.set_mode(screen_size)


# # def main():
# #     pygame.init()
# #     surface = create_main_surface()
# #     state = State()  # startpositie van de cirkel
# #     # Maak een Clock object om de FPS te regelen
# #     clock = pygame.time.Clock()

# #     running = True

# #     while running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 running = False


# #         # Key states ophalen
# #         keys = pygame.key.get_pressed()

# #         elapsed_seconds = clock.tick() / 1000.0  # geen FPS-limiet
# #         state.update(elapsed_seconds, keys)              # update met tijd
# #         state.render(surface)

# # ----------------------------------------------------------------------------------------------------------------
# import pygame

# class Avatar:
#     def __init__(self, x, image_path, player):
#         self.position = [x, 550]  # CHANGE BASED ON LOCATION Y PATH
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.speed = 1000
#         self.player = player

#     def update(self, elapsed_seconds, keys):
#         if keys[pygame.K_RIGHT]:
#             self.position[0] += self.speed * elapsed_seconds
#         if keys[pygame.K_LEFT]:
#             self.position[0] -= self.speed * elapsed_seconds
#         # if keys[pygame.K_DOWN]:
#         #     self.position[1] += self.speed * elapsed_seconds
#         # if keys[pygame.K_UP]:
#         #     self.position[1] -= self.speed * elapsed_seconds

#     def render(self, surface):
#         surface.blit(self.image, self.position)
