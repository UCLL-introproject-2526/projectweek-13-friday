# simpel blokje voor nu, beweegt links / rechts

import pygame

class Player:
    def __init__(self, x, y):
        self.idle_sheet = pygame.image.load("assets/characters/schoolgirl/idle.png").convert_alpha()
        self.walk_sheet = pygame.image.load("assets/characters/schoolgirl/walk.png").convert_alpha()
        
        self.scale = 1.8 
        
        self.frame_height = 128
        self.idle_frames = 9
        self.walk_frames = 12
        self.idle_frame_width = 1152 // self.idle_frames
        self.walk_frame_width = 1536 // self.walk_frames
        
        # bereken nieuwe hoogte na scaling
        scaled_h = int(self.frame_height * self.scale)
        
        fixed_y = 580 - (80 * self.scale) # x * self.scale -> x is aanpasbaar!!!
        
        self.rect = pygame.Rect(x, fixed_y, 60 * self.scale, 100 * self.scale) 
        
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.1
        self.state = "idle"
        self.facing_right = True
        self.speed = 350

    # for switching between animations..
    def update(self, dt, keys):
        moving = False
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
            self.state = "walk"
            self.facing_right = False
            moving = True
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
            self.state = "walk"
            self.facing_right = True
            moving = True
        else:
            self.state = "idle"

        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            max_frames = self.walk_frames if self.state == "walk" else self.idle_frames
            self.current_frame = (self.current_frame + 1) % max_frames

    # draw draw draw
    def draw(self, screen, offset_x=0):
        if self.state == "walk":
            sheet = self.walk_sheet
            w, h = self.walk_frame_width, self.frame_height
        else:
            sheet = self.idle_sheet
            w, h = self.idle_frame_width, self.frame_height
            
        source_rect = pygame.Rect(self.current_frame * w, 0, w, h)
        frame_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        frame_surface.blit(sheet, (0, 0), source_rect)
        
        scaled_w = int(w * self.scale)
        scaled_h = int(h * self.scale)
        frame_surface = pygame.transform.scale(frame_surface, (scaled_w, scaled_h))
        
        if not self.facing_right:
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            
        draw_x = self.rect.x - offset_x - (scaled_w - self.rect.width) // 2
        # fix: teken de sprite zodat onderkant = onderkant van collision rect
        draw_y = self.rect.bottom - scaled_h
        
        screen.blit(frame_surface, (draw_x, draw_y))