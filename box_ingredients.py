self.inventory_slots = [
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
    {"name": None, "count": 0},
]



if candy:
    self.current_candy_sprite = CandySprite(candy, (640, 360))

    # 1️⃣ Eerst kijken: bestaat dit snoepje al?
    for slot in self.inventory_slots:
        if slot["name"] == candy:
            slot["count"] += 1
            return  # stop hier → klaar

    # 2️⃣ Anders: eerste lege slot zoeken
    for slot in self.inventory_slots:
        if slot["name"] is None:
            slot["name"] = candy
            slot["count"] = 1
            return





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



font = pygame.font.Font(None, 28)

for i in range(len(self.inventory_slots)):
    slot = self.inventory_slots[i]

    if slot["name"] is not None:
        rect = inventory_rects[i]

        # snoep-afbeelding
        image_path = candy_images[slot["name"]]
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (64, 64))

        self.screen.blit(
            image,
            (rect.x + 5, rect.y + 5)
        )

        # teller
        if slot["count"] > 1:
            text = font.render(str(slot["count"]), True, (255, 255, 255))
            self.screen.blit(
                text,
                (rect.right - 20, rect.bottom - 20)
            )
