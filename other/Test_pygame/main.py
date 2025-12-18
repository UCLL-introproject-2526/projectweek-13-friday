# import pygame

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# pygame.display.set_caption("Chicken test")

# # Background
# rooms = [
#     pygame.image.load("rooms/farm.jpg").convert(),
#     pygame.image.load("rooms/metro.jpg").convert(),
#     pygame.image.load("rooms/city.png").convert(),
# ]
# rooms = [pygame.transform.scale(room, (1280, 720)) for room in rooms]

# # Labo (special room, only via interaction)
# labo_img = pygame.image.load("rooms/lab.png").convert()
# labo_img = pygame.transform.scale(labo_img, (1280, 720))
# rooms.append(labo_img)
# LAB_ROOM = len(rooms) - 1  # index van labo

# # Chicken
# chicken_left = pygame.image.load("characters/Chicken.png").convert_alpha()
# chicken_right = pygame.transform.flip(chicken_left, True, False)
# chicken_rect = chicken_right.get_rect(center=(640, 620))

# facing_right = False
# speed = 5

# # Egg blaster
# egg_img = pygame.image.load("characters/eggs.png").convert_alpha()
# egg_img = pygame.transform.scale(egg_img, (24, 24))
# eggs = []
# egg_speed = 12

# #Farmer 
# farmer_img_right = pygame.image.load("characters/farmer.png").convert_alpha()
# farmer_img_right = pygame.transform.scale(farmer_img_right, (100, 100))

# farmer_img_left = pygame.transform.flip(farmer_img_right, True, False)

# farmer_rect = farmer_img_right.get_rect(midbottom=(640, 640)) 

# farmer_speed = 1
# farmer_dir = 1  
# FARMER_MIN_X = 150
# FARMER_MAX_X = 1100

# # Farmer stun
# farmer_stunned_until = 0
# FARMER_STUN_MS = 2000

# # Interaction zone (pas coords aan naar je deur)
# barn_door_zone = pygame.Rect(400, 620, 20, 120)

# # Battle mode engagment 
# battle_mode = False

# VISION_LENGTH = 260      # hoe ver de farmer kan zien
# VISION_HALF_HEIGHT = 70  # hoe breed de cone is
# VISION_COOLDOWN_MS = 3000  
# vision_disabled_until = 0

# # Variables
# clock = pygame.time.Clock()
# font = pygame.font.Font(None, 40)
# running = True
# current_room = 0
# prev_room = 0

# def point_in_triangle(p, a, b, c):
#     # barycentric / sign method
#     def sign(p1, p2, p3):
#         return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

#     d1 = sign(p, a, b)
#     d2 = sign(p, b, c)
#     d3 = sign(p, c, a)

#     has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
#     has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

#     return not (has_neg and has_pos)

# #------------------------------------------------------------------------------------------------------

# while running:
#     clock.tick(60)

#     # Recompute each frame
#     near_door = chicken_rect.colliderect(barn_door_zone)

#     # EVENTS
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # Enter / Exit labo with E (optional: E toggles)
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
#             # Als je in labo zit: altijd exit
#             if current_room == LAB_ROOM:
#                 current_room = prev_room
#                 chicken_rect.center = (410, 620)

#             # Anders: enkel enter als je near_door bent
#             elif near_door:
#                 prev_room = current_room
#                 current_room = LAB_ROOM
#                 chicken_rect.left = 0

#         # Shoot egg with SPACE
#         if not battle_mode and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             if facing_right:
#                 spawn_x = chicken_rect.right
#                 vx = egg_speed
#             else:
#                 spawn_x = chicken_rect.left - egg_img.get_width()
#                 vx = -egg_speed

#             spawn_y = chicken_rect.centery - 10
#             egg_rect = egg_img.get_rect(topleft=(spawn_x, spawn_y))
#             eggs.append({"rect": egg_rect, "vx": vx})
        
#         # Quit battle scene    
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
#             battle_mode = False
#             vision_disabled_until = pygame.time.get_ticks() + VISION_COOLDOWN_MS
            
#     #------------------------------------------------------------------------------------------------------
#     # MOVEMENT
#     if not battle_mode:
#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_q] or keys[pygame.K_LEFT]:
#             chicken_rect.x -= speed
#             facing_right = False

#         if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
#             chicken_rect.x += speed
#             facing_right = True

#     # SCREEN BOUNDS (top/bottom altijd, links/rechts niet hard clampen als je edge-switch wilt)
#     if chicken_rect.top < 0:
#         chicken_rect.top = 0
#     if chicken_rect.bottom > 720:
#         chicken_rect.bottom = 720

#     # UPDATE EGGS
#     for egg in eggs:
#         egg["rect"].x += egg["vx"]

#     # --- EGG HIT FARMER (only on farm) ---
#     current_time = pygame.time.get_ticks()
#     if current_room == 0:
#         for egg in eggs[:]:
#             if egg["rect"].colliderect(farmer_rect):
#                 eggs.remove(egg)
#                 farmer_stunned_until = current_time + FARMER_STUN_MS
#                 break  # 1 hit per frame is genoeg

#     # cleanup offscreen
#     eggs = [egg for egg in eggs if -50 < egg["rect"].x < 1280 + 50]
    
#     # ROOM TRANSITIONS (only for normal rooms, NOT labo) 
#     if current_room != LAB_ROOM:
#         # rechts -> volgende normale room (niet labo)
#         if chicken_rect.right >= 1280:
#             if current_room < len(rooms) - 2:  # -2 want laatste is labo
#                 current_room += 1
#                 chicken_rect.left = 0
#             else:
#                 chicken_rect.right = 1280

#         # links -> vorige room
#         elif chicken_rect.left <= 0:
#             if current_room > 0:
#                 current_room -= 1
#                 chicken_rect.right = 1280
#             else:
#                 chicken_rect.left = 0
#     else:
#         # in labo: gewoon niet buiten links/rechts
#         if chicken_rect.left < 0:
#             chicken_rect.left = 0
#         if chicken_rect.right > 1280:
#             chicken_rect.right = 1280
            
#     # NPC update (alleen als je op farm zit)
#     current_time = pygame.time.get_ticks()
#     farmer_stunned = current_time < farmer_stunned_until

#     if current_room == 0 and not battle_mode and not farmer_stunned:
#         farmer_rect.x += farmer_speed * farmer_dir

#         # omkeren bij patrol grenzen
#         if farmer_rect.left <= FARMER_MIN_X:
#             farmer_rect.left = FARMER_MIN_X
#             farmer_dir = 1

#         elif farmer_rect.right >= FARMER_MAX_X:
#             farmer_rect.right = FARMER_MAX_X
#             farmer_dir = -1
    
#     # Farmer vision
#     if current_room == 0 and not farmer_stunned:
#         farmer_eye = (farmer_rect.centerx + 10, farmer_rect.centery - 15)  # ogen

#         if farmer_dir == 1:  # kijkt rechts
#             tip = (farmer_eye[0] + VISION_LENGTH, farmer_eye[1])
#         else:                # kijkt links
#             tip = (farmer_eye[0] - VISION_LENGTH, farmer_eye[1])

#         top = (tip[0], tip[1] - VISION_HALF_HEIGHT)
#         bottom = (tip[0], tip[1] + VISION_HALF_HEIGHT)

#         vision_tri = (farmer_eye, top, bottom)
#     else:
#         vision_tri = None
    
#     # Battle trigger
#     current_time = pygame.time.get_ticks()

#     if (current_room == 0 and not battle_mode
#         and current_time >= vision_disabled_until
#         and not farmer_stunned
#         and vision_tri is not None):
#         chicken_point = chicken_rect.center
#         if point_in_triangle(chicken_point, *vision_tri):
#             battle_mode = True
#             print("BATTLE!")

#     #------------------------------------------------------------------------------------------------------
#     # DRAW
#     screen.blit(rooms[current_room], (0, 0))

#     if facing_right:
#         screen.blit(chicken_right, chicken_rect)
#     else:
#         screen.blit(chicken_left, chicken_rect)

#     for egg in eggs:
#         screen.blit(egg_img, egg["rect"])

#     # Interaction UI 
#     if current_room == LAB_ROOM:
#         text = font.render("Press E to Exit Lab", True, (255, 255, 255))
#         bg = pygame.Rect(0, 0, text.get_width() + 30, text.get_height() + 20)
#         bg.center = (640, 60)
#         pygame.draw.rect(screen, (0, 0, 0), bg, border_radius=10)
#         screen.blit(text, (bg.x + 15, bg.y + 10))

#     elif current_room == 0 and near_door:
#         text = font.render("Press E to Enter Lab", True, (255, 255, 255))
#         bg = pygame.Rect(0, 0, text.get_width() + 30, text.get_height() + 20)
#         bg.center = (640, 60)
#         pygame.draw.rect(screen, (0, 0, 0), bg, border_radius=10)
#         screen.blit(text, (bg.x + 15, bg.y + 10))
        
#     # Draw farmer (alleen in farm)
#     if current_room == 0:
#         if farmer_dir == 1:
#             screen.blit(farmer_img_right, farmer_rect)
#         else:
#             screen.blit(farmer_img_left, farmer_rect)

#         # STUN UI
#         if pygame.time.get_ticks() < farmer_stunned_until:
#             t = font.render("STUNNED!", True, (255, 255, 255))
#             screen.blit(t, (farmer_rect.centerx - t.get_width() // 2, farmer_rect.top - 30))
         
#     # Guard System
#     current_time = pygame.time.get_ticks()
#     if current_room == 0 and not battle_mode and (not farmer_stunned) and vision_tri is not None:
#         vision_surf = pygame.Surface((1280, 720), pygame.SRCALPHA)

#         if current_time < vision_disabled_until:
#             # hoeveel cooldown nog over is (0..1)
#             remaining = vision_disabled_until - current_time
#             progress = 1.0 - (remaining / VISION_COOLDOWN_MS)  # 0 -> 1

#             # knipper sneller naarmate progress dichter bij 1 komt
#             # start traag (0.8s) eind snel (0.12s)
#             period_ms = int(800 - 680 * progress)  # 800 -> 120
#             blink_on = (current_time // period_ms) % 2 == 0

#             # alpha ook laten variëren
#             alpha = 20 if blink_on else 0
#         else:
#             alpha = 60  # normale cone

#         if alpha > 0:
#             pygame.draw.polygon(vision_surf, (255, 255, 0, alpha), vision_tri)
#             screen.blit(vision_surf, (0, 0))
#             pygame.draw.line(screen, (255, 255, 0), vision_tri[0], vision_tri[1], 2)
#             pygame.draw.line(screen, (255, 255, 0), vision_tri[0], vision_tri[2], 2)

#     #Battle scene
#     if battle_mode:
#         overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
#         overlay.fill((0, 0, 0, 160))
#         screen.blit(overlay, (0, 0))

#         text = font.render("BATTLE MODE! (press B to exit)", True, (255, 255, 255))
#         screen.blit(text, (420, 60))
        
#     pygame.display.update()

# pygame.quit()