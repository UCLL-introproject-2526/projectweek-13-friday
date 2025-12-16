import pygame

class Room:
    def __init__(self, index, img_path):
        # combine index w room + load background img
        self.index = index
        self.image = pygame.image.load(img_path).convert()  

        # positieverandering voor later... buren!!
        self.left = None
        self.right = None

def create_rooms():
    # lijst in volgorde van hoedat de kamers staan..
    []

    room_images = [
        "Rooms/classroom.png",   # index 0
        "Rooms/cafetaria.png",   # index 1
        "Rooms/bathroom.png",    # index 2    
    ]

    rooms = {}

    # "enumerate geeft zowel de positie (index) als het item zelf (image_path) in de lijst"
    # elke afbeelding --> room object in dict 'rooms'
    for index, image_path in enumerate(room_images):
        rooms[index] = Room(index, image_path)

    for index in rooms:
        # niet eerste kamer? -> maak left buur!
        if index > 0:
            rooms[index].left = index - 1
        
        # niet laatste kamer? -> maak right buur!
        if index < len(rooms) - 1:
            rooms[index].right = index + 1

    return rooms