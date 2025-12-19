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
        self.student_to_draw = []
        self.student_locations = {}

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

        # check if player is near students because we need to make a pop up when they are near
        self.nearby_student = None
        closest_distance = game.WIDTH
        interaction_distance = 100

        for student, student_x in self.student_locations.items():
            distance = abs(player.rect.centerx - student_x)
            
            if distance < interaction_distance and distance < closest_distance:
                closest_distance = distance
                self.nearby_student = student

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game.start_fade("hallway", self.return_x)
                
                elif event.key == pygame.K_f and hasattr(self, 'nearby_student') and self.nearby_student:
                    # Get the order details
                    candy_type = self.nearby_student.order["order"][0]
                    quantity = self.nearby_student.order["order"][1]
                    
                    # Check if player has enough candy
                    if game.player_info.current_inventory.has_candy(candy_type) and \
                    quantity <= game.player_info.current_inventory.get_quantity(candy_type):
                        
                        # Perform the transaction
                        payment = quantity * 2
                        game.player_info.add_assignments(payment)
                        game.player_info.current_inventory.decrease_inventory(candy_type, quantity)
                        
                        # UPDATE THE UI SLOTS - ADD THIS:
                        for slot in game.inventory_slots:
                            if slot["name"] == candy_type:
                                slot["count"] -= quantity
                                if slot["count"] <= 0:  # If all used up, clear the slot
                                    slot["name"] = None
                                    slot["count"] = 0
                                break
                        
                        print(f"✅ Delivery successful! +{payment} assignments")
                        print(f"Current assignments: {game.player_info.current_assignments}")
                        print(f"Current inventory: {game.player_info.current_inventory}")
                    else:
                        have = game.player_info.current_inventory.get_quantity(candy_type)
                        print(f"❌ Not enough {candy_type}! Need {quantity}, you have {have}")


        # for event in events:
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
        #         # return op plaats waar je binnenkwam (positielogica)
        #         game.start_fade("hallway", self.return_x)

        for event in events:
            if event.type == pygame.KEYDOWN:  # Check this FIRST
                if event.key == pygame.K_e:
                    game.start_fade("hallway", self.return_x)
                
                elif event.key == pygame.K_f and hasattr(self, 'nearby_student') and self.nearby_student:  
                    print(f"Interacting with {self.nearby_student.name}")
            
    

    def draw(self, screen, player, game):
        screen.fill((40, 60, 120))
    
    #commented out because it already get's done in game.py
        # n_to_draw = min(3, len(self.students))  # pak maximaal 3 studenten, of minder als er minder zijn
        # students_to_draw = random.sample(self.students, n_to_draw)

        x = 50
        y = 500

        self.student_locations = {}
        for student in self.students_to_draw:
            self.student_locations[student] = x
            rect = pygame.Rect(x , y ,50,50)
            pygame.draw.rect(screen, student.color, rect)
            x = x + 400
        

        # print(f"Students to draw: {len(self.students_to_draw)}")
        # print(f"Student locations: {self.student_locations}")
        # print(f"Player position: {player.rect.centerx}, {player.rect.centery}")

        self.nearby_student = None
        closest_distance = game.WIDTH
        interaction_distance = 80
        
        for student, student_x in self.student_locations.items():
            distance = abs(player.rect.centerx - student_x)
            # print(f"Distance to {student.name}: {distance}")
            
            if distance < interaction_distance and distance < closest_distance:
                closest_distance = distance
                self.nearby_student = student
                # print(f"Found nearby student: {student.name}")




        # kamertitle!!!
        font = pygame.font.SysFont(None, 48)
        title = font.render(self.name, True, (255, 255, 255))
        screen.blit(title, (50, 50))
        
        # exit prompt onderaan scherm
        draw_prompt(screen, "Press E to exit room", 640, 680)

        if self.nearby_student:
            order_text = str(self.nearby_student)  
            draw_prompt(screen, order_text, 640, 620)
            draw_prompt(screen, "Press F to deliver", 640, 650)
        
        player.draw(screen)