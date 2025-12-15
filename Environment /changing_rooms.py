from pathlib import Path
import pygame

pygame.init()

ROOMS_PATH = Path(__file__).parent.parent / "Rooms"

rooms = []

for image_path in ROOMS_PATH.glob("*"):
    if image_path.suffix in (".avif", ".webp"):
        image = pygame.image.load(image_path)
        rooms.append({
            "name": image_path.stem,
            "image": image
        })