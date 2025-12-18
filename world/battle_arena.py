import pygame
from ui.prompt import draw_prompt
from entities.enemy import Enemy
from ui.battle_render import draw_battle_scene

# ---------------------!!! SKILL CLASS !!! ------------- voor qte...

class TimingBar:
    def __init__(self, x, y, width=300, height=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.cursor_pos = 0  # 0 tot 1 (percentage)
        self.speed = 1.5     # snelheid balk links.. rechts..
        self.direction = 1   # 1 is rechts, -1 is links
        self.active = False
        
        self.target_zone = (0.7, 0.85)  # sweet spot!

    def update(self, dt):
        if self.active:
            self.cursor_pos += self.direction * self.speed * dt
            if self.cursor_pos >= 1:
                self.cursor_pos = 1
                self.direction = -1
            elif self.cursor_pos <= 0:
                self.cursor_pos = 0
                self.direction = 1

    def get_result(self):
        # True als cursor in target zone staat
        return self.target_zone[0] <= self.cursor_pos <= self.target_zone[1]

    def draw(self, screen):
        if not self.active: return
        
        # bg balk
        pygame.draw.rect(screen, (50, 50, 50), self.rect)
        # de target zone (groen)
        zone_x = self.rect.x + (self.target_zone[0] * self.rect.width)
        zone_w = (self.target_zone[1] - self.target_zone[0]) * self.rect.width
        pygame.draw.rect(screen, (0, 255, 0), (zone_x, self.rect.y, zone_w, self.rect.height))
        # de bewegende cursor (wit)
        cursor_x = self.rect.x + (self.cursor_pos * self.rect.width)
        pygame.draw.rect(screen, (255, 255, 255), (cursor_x - 2, self.rect.y - 5, 5, self.rect.height + 10))

# ---------------------!!! SKILL CLASS !!! -------------

class Skill:
    def __init__(self, name, damage, text):
        self.name = name
        self.damage = damage
        self.text = text

# ---------------------!!! BATTLE ARENA CLASS !!! -------------

class BattleArena:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)
        self.timing_bar = TimingBar(x=490, y=550) # in midden boven UI

        # voor ending of battle...
        self.winner = None  # wordt "player" of "enemy"
        self.end_message = ""   # adhv outcome fight..
        self.battle_concluded = False 

        # Foto's inladen
        try:
            self.ground_img = pygame.image.load("assets/backgrounds/battle/asphalt.png").convert_alpha()
            self.sky_img = pygame.image.load("assets/backgrounds/battle/sky_battle.png").convert_alpha()
            self.sky_img = pygame.transform.scale(self.sky_img, (1280, 720))
        except:
            print("Error: Battle backgrounds niet gevonden!")
            self.ground_img = pygame.Surface((1280, 200))
            self.sky_img = pygame.Surface((1280, 720))

        # Skills definiëren
        self.player_skills = [
            Skill("Punch", 10, "A quick jab!"),
            Skill("Kick", 15, "A powerful roundhouse!"),
            Skill("Book Throw", 25, "Knowledge is pain!")
        ]
        
        self.enemy_hp = 100
        self.player_hp = 100
        self.enemy_max_hp = 100
        
        self.phase = "intro" 
        self.intro_step = "dialogue" 
        self.selected_skill = 0
        self.result_text = ""
        self.attack_range = 150
        
        # posities + knockback
        self.enemy = Enemy(1350, 350)
        self.enemy_original_x = 700 
        self.knockback_target = 700

        self.knockback_delay = 0.5  # delay voor smoother animation AANPASBAAR!!!
        self.knockback_timer = 0.0

        self.player_knockback_target = 0
        self.player_knockback_delay = 0.4  # delay voor player..
        self.player_knockback_timer = 0.0
        self.has_attacked = False          # heeft enemy al geslagen??? che

    def update(self, player, events, game):
        dt = game.clock.get_time() / 1000
        
        # FIX: Geef de X-positie van de speler door aan de enemy update voor de richting
        self.enemy.update(dt, player.rect.centerx)
        if self.phase == "qte":
            self.timing_bar.update(dt)
            player.update(dt, None) # speler staat stil tijdens QTE NO MOVING
            
        elif self.phase == "intro":
            player.update(dt, None)
            if self.intro_step == "dialogue":
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        self.intro_step = "walking"
                        self.enemy.change_state("walk")
            
            elif self.intro_step == "walking":
                if self.enemy.pos.x > self.enemy_original_x:
                    self.enemy.pos.x -= 150 * dt
                else:
                    self.enemy.pos.x = self.enemy_original_x
                    self.enemy.change_state("idle")
                    self.phase = "movement"

        elif self.phase == "movement":
            keys = pygame.key.get_pressed()
            player.update(dt, keys)
            self.enemy.change_state("idle")
            
            dist = abs(player.rect.centerx - self.enemy.pos.x)
            if dist <= self.attack_range and keys[pygame.K_e]:
                self.phase = "choose"

        # nieuwe fase tussen aanval en slide .. timing fixes onder hier..
        if self.phase == "waiting_for_knockback":
            player.update(dt, None)
            self.knockback_timer += dt
            if self.knockback_timer >= self.knockback_delay:
                self.phase = "player_atk" # NU pas mag hij gaan schuiven
        
        elif self.phase == "player_atk":
            player.update(dt, None)
            speed = 500
            if abs(self.enemy.pos.x - self.knockback_target) > 5:
                if self.enemy.pos.x < self.knockback_target:
                    self.enemy.pos.x += speed * dt
                else:
                    self.enemy.pos.x -= speed * dt
            
            else:
                # CHECK HIER OF ENEMY DOOD IS !!!!
                if self.enemy_hp <= 0:
                    self.enemy.change_state("dead") # state klopt in enemy.py fix!!
                    self.winner = "player"
                    self.end_message = "You won! 'Ugh... you got lucky this time!'"
                    self.phase = "battle_end"
            
        elif self.phase == "enemy_atk":
            player.update(dt, None)
            
            # enemy loopt eerst terug naar originele positie (als nodig)
            if abs(self.enemy.pos.x - self.enemy_original_x) > 5:
                self.enemy.change_state("walk")
                if self.enemy.pos.x < self.enemy_original_x:
                    self.enemy.pos.x += 300 * dt
                else:
                    self.enemy.pos.x -= 300 * dt
            else:
                self.enemy.change_state("attack")
                slide_speed = 500
                dist_to_target = abs(player.rect.x - self.player_knockback_target)
                
                if dist_to_target > 5:
                    if player.rect.x < self.player_knockback_target:
                        player.rect.x += slide_speed * dt
                    else:
                        player.rect.x -= slide_speed * dt
                else:
                    player.rect.x = self.player_knockback_target
                    if self.player_hp <= 0:
                        player.change_state("death") 
                        self.winner = "enemy"
                        self.end_message = "You fainted... 'Don't let me see your face again.'"
                        self.phase = "battle_end"
        
        elif self.phase == "battle_end":
            player.update(dt, None)
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    # RESET PLAYER STATE
                    player.change_state("idle")
                    
                    if self.winner == "enemy":
                        player.rect.x = 100 # Reset naar begin hallway
                    
                    #veranderingen voor after..
                    game.state = "exploration"
                    self.phase = "intro" # reset voor de volgende keer
                    self.intro_step = "dialogue"

        else:
            player.update(dt, None)

        # input handling
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.phase == "choose":
                    if event.key == pygame.K_UP:
                        self.selected_skill = (self.selected_skill - 1) % len(self.player_skills)
                    elif event.key == pygame.K_DOWN:
                        self.selected_skill = (self.selected_skill + 1) % len(self.player_skills)
                    elif event.key == pygame.K_RETURN:
                        self.player_turn(player)
                        self.phase = "qte"
                        self.timing_bar.active = True
                        self.timing_bar.cursor_pos = 0
                
                elif self.phase == "qte":
                    if event.key == pygame.K_SPACE:
                        self.timing_bar.active = False
                        is_hit = self.timing_bar.get_result()
                        # geef de multiplier aan player_turn
                        mult = 1.5 if is_hit else 0.5
                        self.player_turn(player, multiplier=mult)

                elif self.phase == "player_atk" and event.key == pygame.K_e:
                    self.enemy_turn(player)

                elif self.phase == "enemy_atk" and event.key == pygame.K_e:
                    self.enemy.change_state("idle")
                    self.phase = "movement"

    def player_turn(self, player, multiplier=1.0):
        skill = self.player_skills[self.selected_skill]
        final_damage = int(skill.damage * multiplier)
        self.enemy_hp -= skill.damage
        player.change_state("attack")
        self.enemy.change_state("hurt")
        
        # bereken de target maar start nog niet met schuiven
        if player.rect.centerx < self.enemy.pos.x:
            self.knockback_target = self.enemy.pos.x + 120
        else:
            self.knockback_target = self.enemy.pos.x - 120
            
        # zet de timer op 0 en ga naar de wait phase
        self.knockback_timer = 0.0
        self.phase = "waiting_for_knockback" 
        status = "PERFECT!" if multiplier > 1.0 else "MISSED!"
        self.result_text = f"{status} Used {skill.name} for {final_damage} dmg! (Press E)"

    def enemy_turn(self, player):
        self.player_hp -= 10
        player.change_state("hurt")
        
        slide_dir = -1 if self.enemy.pos.x > player.rect.x else 1
        self.player_knockback_target = player.rect.x + (slide_dir * 150)
        
        # fix: borders check: voorkom dat player buiten beeld slide
        if self.player_knockback_target < 0: self.player_knockback_target = 0
        if self.player_knockback_target > 1200: self.player_knockback_target = 1200

        self.phase = "enemy_atk"
        self.result_text = "The enemy counters! (Press E)"

    def draw(self, screen, player, game):
        
        draw_battle_scene(screen, self, player, self.ground_img, self.sky_img, self.font)
        
        if self.phase == "qte":
            self.timing_bar.draw(screen)
            txt = self.font.render("HIT SPACE IN GREEN!", True, (255, 255, 255))
            screen.blit(txt, (self.timing_bar.rect.x, self.timing_bar.rect.y - 35))

        if self.phase == "battle_end":
            pygame.draw.rect(screen, (0, 0, 0), (0, 500, 1280, 220))
            pygame.draw.line(screen, (255, 255, 255), (0, 500), (1280, 500), 3)
            
            msg = self.font.render(self.end_message, True, (255, 255, 255))
            screen.blit(msg, (100, 550))
            
            prompt = self.font.render("[Press E to exit]", True, (150, 150, 150))
            screen.blit(prompt, (100, 620))