import pygame
from ingredients.ingredient import candy_images

def draw_lab_ui(self):
    # Alleen tekenen als je in de lab bent
    

        # Inventory achtergrond
        inv_rect = pygame.Rect(10, 10, 675, 75)
        pygame.draw.rect(self.screen, (50, 50, 50), inv_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), inv_rect, 2)

        # assigments border
        inv_rect = pygame.Rect(1120, 10, 150, 70)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), inv_rect, 2)

        # slots
        inv_item1_rect = pygame.Rect(10, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item1_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item1_rect, 2)  # optioneel witte rand

        inv_item2_rect = pygame.Rect(85, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item2_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item2_rect, 2)  # optioneel witte rand

        inv_item3_rect = pygame.Rect(160, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item3_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item3_rect, 2)  # optioneel witte rand

        inv_item4_rect = pygame.Rect(235, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item4_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item4_rect, 2)  # optioneel witte 
        
        inv_item5_rect = pygame.Rect(310, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item5_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item5_rect, 2)  # optioneel witte rand

        inv_item6_rect = pygame.Rect(385, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item6_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item6_rect, 2)  # optioneel witte rand

        inv_item7_rect = pygame.Rect(460, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item7_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item7_rect, 2)  # optioneel witte 
        
        inv_item8_rect = pygame.Rect(535, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item8_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item8_rect, 2)  # optioneel witte rand

        inv_item9_rect = pygame.Rect(610, 10, 75, 75)  # (x, y, width, height)
        pygame.draw.rect(self.screen, (150, 150, 150), inv_item9_rect)  # donkergrijze box
        pygame.draw.rect(self.screen, (255, 255, 255), inv_item9_rect, 2)  # optioneel witte rand

        if self.current_area == "lab":
            # Box achter ingredienten
            box_rect = pygame.Rect(780, 130, 450, 300)
            pygame.draw.rect(self.screen, (150, 150, 150), box_rect)  # donkergrijs
            pygame.draw.rect(self.screen, (255, 255, 255), box_rect, 3)  # witte rand

        inventory_rects = [
    inv_item1_rect,
    inv_item2_rect,
    inv_item3_rect,
    inv_item4_rect,
    inv_item5_rect,
    inv_item6_rect,
    inv_item7_rect,
    inv_item8_rect,
    inv_item9_rect,
]
        
        font = pygame.font.Font(None, 28)       # maakt lettertype aan , (lettertype, grootte)

        for i in range(len(self.inventory_slots)):  
            slot = self.inventory_slots[i]      # huidig slot ophalen

            if slot["name"] is not None:        # is het een leeg vakje -> niets tekenen
                rect = inventory_rects[i]

                # snoep-afbeelding
                image_path = candy_images[slot["name"]]
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (64, 64))

                self.screen.blit(
                    image,
                    (rect.x + 5, rect.y + 5)       # tekent het snoepje wat meer naar binnen in het vakje
                )

                # teller``
                if slot["count"] > 1:       # als er al een snoepje inzit dan:
                    text = font.render(str(slot["count"]), True, (255, 255, 255))   # str() -> want pygame kan geen getallen tekenen
                    self.screen.blit(
                        text,
                        (rect.right - 25, rect.bottom - 20) # count tekenen onderaan het vakje 
                    )

        # Teken alle ingredient sprites
        if self.current_area == "lab":
            for sprite in self.ingredient_sprites:
                sprite.draw(self.screen)

        mouse_position = pygame.mouse.get_pos()
        hovering = False 

        
        for sprite in self.ingredient_sprites:
            if sprite.rect.collidepoint(mouse_position):        # collidepoint kijkt : ligt dit punt binnen de rechthoek?
                hovering = True

        if hovering:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
     


