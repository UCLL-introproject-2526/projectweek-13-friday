import pygame

class Player:
    def __init__(self, x, y):
        self.scale = 1.8
        self.frame_height = 128
        
        # alle animations in dict want.. too many..
        animation_data = {
            "idle": ("idle.png", 9),    # (name file, aantal frames)
            "walk": ("walk.png", 12),
            "run": ("run.png", 12),
            "attack": ("attack.png", 8),
            "death": ("death.png", 5),
            "dialogue": ("dialogue.png", 11),
            "hurt": ("hurt.png", 3),
            "jump": ("jump.png", 15),
            "opening_door": ("opening_door.png", 4),
            "protection": ("protection.png", 4)
        }

        self.animations = {}
        for state, (file, frame_count) in animation_data.items():
            try:
                sheet = pygame.image.load(f"assets/characters/schoolgirl/{file}").convert_alpha()
                frame_width = sheet.get_width() // frame_count
                self.animations[state] = {
                    "sheet": sheet,
                    "frames": frame_count,
                    "width": frame_width
                }
            except pygame.error:
                print(f"Waarschuwing: kon {file} niet laden.")

        # collision Rect
        self.rect = pygame.Rect(x, y, 60 * self.scale, 100 * self.scale)
        
        # animation status
        self.state = "idle"
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.1
        
        # beweging
        self.facing_right = True
        self.speed = 350

    def change_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            self.current_frame = 0
            self.animation_timer = 0

    def update(self, dt, keys):
        moving = False
        
        if keys:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed * dt
                self.change_state("run" if keys[pygame.K_LSHIFT] else "walk")       # run with shift.. anders gwn walk
                self.facing_right = False
                moving = True
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.speed * dt
                self.change_state("run" if keys[pygame.K_LSHIFT] else "walk")       # same here ''
                self.facing_right = True
                moving = True

        # als we niet bewegen, terug naar idle (behalve bij acties zoals attack/hurt.. in the battle)
        if not moving and self.state not in ["attack", "hurt", "death", "dialogue"]:
            self.change_state("idle")

        # animation logica
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            anim_info = self.animations[self.state]
            
            # Lijst van animaties die NIET mogen loopen
            non_looping = ["attack", "hurt", "death", "opening_door"]

            if self.state in non_looping:
                # Als we bij het laatste frame zijn
                if self.current_frame < anim_info["frames"] - 1:
                    self.current_frame += 1
                else:
                    # Specifiek voor attack/hurt: ga terug naar idle na 1 keer
                    if self.state != "death":
                        self.change_state("idle")
            else:
                # Normale loop voor walk, run, idle
                self.current_frame = (self.current_frame + 1) % anim_info["frames"]
                
    def draw(self, screen, offset_x=0):
        if self.state not in self.animations:
            return

        anim_info = self.animations[self.state]
        sheet = anim_info["sheet"]
        w = anim_info["width"]
        h = self.frame_height

        source_rect = pygame.Rect(self.current_frame * w, 0, w, h)
        frame_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        frame_surface.blit(sheet, (0, 0), source_rect)

        scaled_w = int(w * self.scale)
        scaled_h = int(h * self.scale)
        frame_surface = pygame.transform.scale(frame_surface, (scaled_w, scaled_h))

        if not self.facing_right:
            frame_surface = pygame.transform.flip(frame_surface, True, False)

        # Tekenpositie berekening
        draw_x = self.rect.x - offset_x - (scaled_w - self.rect.width) // 2
        draw_y = self.rect.bottom - scaled_h - 50
        
        screen.blit(frame_surface, (draw_x, draw_y))