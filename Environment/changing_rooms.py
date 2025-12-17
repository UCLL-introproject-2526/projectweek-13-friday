import pygame

class Room:
    def __init__(self, index, image_path, screen_width, screen_height):
        self.index = index
        # Laad afbeelding en schaal naar scherm
        raw_image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(raw_image, (screen_width, screen_height))

        self.left = None
        self.right = None

def create_rooms(screen_width, screen_height):
    room_images = [
        "Rooms/office.png",         # index 0
        "Rooms/hallway.png",       # index 1
        "Rooms/classroom.png",   # index 2    
        "Rooms/hallway.png",       # index 3    
        "Rooms/playground.png", # index 4    
        "Rooms/school_exit.png", # index 5    
        "Rooms/lab.png",        # index 6    
    ]

    rooms = {}

    for index, image_path in enumerate(room_images):
        rooms[index] = Room(index, image_path, screen_width, screen_height)

    # Assign neighbors
    for index in rooms:
        if index > 0:
            rooms[index].left = index - 1
        if index < len(rooms) - 1:
            rooms[index].right = index + 1

    return rooms
