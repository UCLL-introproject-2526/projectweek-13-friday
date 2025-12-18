import pygame

class Enemy:
    def __init__(self, x, y):
        self.facing_right = False
        # sprites
        self.sheets = {
            "idle": pygame.image.load("assets/characters/enemy/idle_1.png").convert_alpha(),
            "walk": pygame.image.load("assets/characters/enemy/walk.png").convert_alpha(),
            "attack": pygame.image.load("assets/characters/enemy/attack_1.png").convert_alpha(),
            "hurt": pygame.image.load("assets/characters/enemy/hurt.png").convert_alpha(),
            "dead": pygame.image.load("assets/characters/enemy/dead.png").convert_alpha()
        }
        
        # (frames, breedte per frame)
        self.animate_data = {
            "idle": {"frames": 6, "width": 768 // 6},
            "walk": {"frames": 7, "width": 896 // 7},
            "attack": {"frames": 5, "width": 640 // 5},
            "hurt": {"frames": 2, "width": 256 // 2},
            "dead": {"frames": 4, "width": 512 // 4}
        }

        self.state = "idle"
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        
        self.scale = 2.7
        
        # position + hitbox
        w = self.animate_data["idle"]["width"] * self.scale
        h = 128 * self.scale
        self.rect = pygame.Rect(x, y, 60 * self.scale, 100 * self.scale)
        self.pos = pygame.Vector2(x, y)

    def change_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            self.current_frame = 0
            self.animation_timer = 0

    def update(self, dt, player_x):
        if self.pos.x < player_x:
            self.facing_right = True
        else:
            self.facing_right = False
        
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.animate_data[self.state]["frames"]
            
            if self.state == "dead" and self.current_frame == self.animate_data["dead"]["frames"] - 1:
                self.current_frame = self.animate_data["dead"]["frames"] - 1

    def draw(self, screen):
        sheet = self.sheets[self.state]
        frame_w = self.animate_data[self.state]["width"]
        frame_h = 128
        
        source_rect = pygame.Rect(self.current_frame * frame_w, 0, frame_w, frame_h)
        frame_surface = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
        frame_surface.blit(sheet, (0, 0), source_rect)
        
        scaled_w = int(frame_w * self.scale)
        scaled_h = int(frame_h * self.scale)
        frame_surface = pygame.transform.scale(frame_surface, (scaled_w, scaled_h))
        
        # fix: als player beweegt, verandert enemy ook zn vision 
        if not self.facing_right:
            frame_surface = pygame.transform.flip(frame_surface, True, False)
        
        draw_x = self.pos.x - (scaled_w // 2)
        draw_y = self.rect.bottom - scaled_h
        
        screen.blit(frame_surface, (draw_x, draw_y))