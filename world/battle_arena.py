import pygame
from ui.prompt import draw_prompt

class Skill:
    def __init__(self, name, damage, text):
        self.name = name
        self.damage = damage
        self.text = text

class BattleArena:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)
        self.player_skills = [          # ff snel aangemaakt door chatgpt.. pas aan later..
            Skill("Punch", 10, "A quick jab!"),
            Skill("Kick", 15, "A powerful roundhouse!"),
            Skill("Book Throw", 25, "Knowledge is pain!")
        ]
        
        # battle stats
        self.enemy_hp = 100
        self.player_hp = 100
        self.enemy_max_hp = 100
        self.phase = "movement" # movement, choose, result
        self.selected_skill = 0
        self.result_text = ""
        self.attack_range = 150
        
        # Assets (Zorg dat deze bestaan of gebruik tijdelijke rects)
        self.enemy_img = pygame.Surface((120, 180)) # Placeholder
        self.enemy_img.fill((255, 50, 50))
        self.enemy_pos = pygame.Vector2(1000, 450)

    def update(self, player, events, game):
        dt = game.clock.get_time() / 1000
        
        if self.phase == "movement":
            keys = pygame.key.get_pressed()
            player.update(dt, keys)
            
            # Afstand checken
            dist = abs(player.rect.centerx - self.enemy_pos.x)
            if dist <= self.attack_range and keys[pygame.K_e]:
                self.phase = "choose"

        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.phase == "choose":
                    if event.key == pygame.K_UP:
                        self.selected_skill = (self.selected_skill - 1) % len(self.player_skills)
                    if event.key == pygame.K_DOWN:
                        self.selected_skill = (self.selected_skill + 1) % len(self.player_skills)
                    if event.key == pygame.K_RETURN:
                        self.execute_turn()
                
                elif self.phase == "result":
                    if event.key == pygame.K_e:
                        if self.enemy_hp <= 0:
                            game.start_fade("hallway", 100) # Terug naar start gang
                        else:
                            self.phase = "movement"

    def execute_turn(self):
        skill = self.player_skills[self.selected_skill]
        self.enemy_hp -= skill.damage
        self.result_text = f"Used {skill.name}! {skill.text}"
        
        if self.enemy_hp > 0:
            damage = 10
            self.player_hp -= damage
            self.result_text += f" Enemy hits back for {damage}!"
        else:
            self.result_text = "Enemy Defeated! Press E to exit."
            
        self.phase = "result"

    def draw(self, screen, player, game):
        # Achtergrond
        screen.fill((20, 20, 20))
        pygame.draw.rect(screen, (50, 50, 50), (0, 580, 1280, 140)) # Vloer
        
        # Enemy & Player
        screen.blit(self.enemy_img, self.enemy_pos)
        player.draw(screen, 0) # Geen offset in arena
        
        # UI: HP Bars
        self.draw_hp_bar(screen, 50, 50, self.player_hp, 100, (0, 255, 0), "Student")
        self.draw_hp_bar(screen, 930, 50, self.enemy_hp, self.enemy_max_hp, (255, 0, 0), "Guard")

        # Menu overlays
        if self.phase == "movement":
            dist = abs(player.rect.centerx - self.enemy_pos.x)
            if dist <= self.attack_range:
                draw_prompt(screen, "Press E to Attack", 640, 600)
                
        elif self.phase == "choose":
            overlay = pygame.Surface((400, 200), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (440, 200))
            for i, skill in enumerate(self.player_skills):
                color = (255, 255, 0) if i == self.selected_skill else (255, 255, 255)
                txt = self.font.render(skill.name, True, color)
                screen.blit(txt, (460, 220 + i * 40))

        elif self.phase == "result":
            draw_prompt(screen, self.result_text, 640, 300)

    def draw_hp_bar(self, screen, x, y, hp, max_hp, color, label):
        # Achterkant balk
        pygame.draw.rect(screen, (100, 100, 100), (x, y, 300, 25))
        # Gevulde balk
        fill_width = int((hp / max_hp) * 300)
        if fill_width > 0:
            pygame.draw.rect(screen, color, (x, y, fill_width, 25))
        # Label
        lbl = self.font.render(label, True, (255, 255, 255))
        screen.blit(lbl, (x, y - 30))