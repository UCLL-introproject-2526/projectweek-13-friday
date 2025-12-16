import pygame 
from pathlib import Path

#Global path variable 
BASE_DIR = Path(__file__).resolve().parent.parent
ROOMS_DIR = BASE_DIR / "Rooms"

#Afbeeldingen inladen in lijst (preparation)
rooms = []

for img_path in sorted(ROOMS_DIR.glob("*.png")):
    image = pygame.image.load(img_path).convert_alpha()
    rooms.append(image)
    
print(len(rooms))