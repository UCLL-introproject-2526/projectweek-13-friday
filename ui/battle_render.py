import pygame
from .prompt import draw_prompt

def draw_battle_scene(screen, arena, player, ground_img, sky_img, font):
    # backdrop
    screen.blit(sky_img, (0, 0))

    # floor (image size.. 1920x565)
    ground_y = 550      # pas hier vloer hoogte aan..
    screen.blit(ground_img, (0, ground_y))

    arena.enemy.draw(screen)
    player.draw(screen, 0)

    if arena.phase != "intro" or arena.intro_step == "done":
        draw_hp_bar(screen, 50, 50, arena.player_hp, 100, (0, 255, 0), "Student", font)
        draw_hp_bar(screen, 930, 50, arena.enemy_hp, arena.enemy_max_hp, (255, 0, 0), "Guard", font)

    draw_ui_elements(screen, arena, player, font)

def draw_hp_bar(screen, x, y, hp, max_hp, color, label, font):
    pygame.draw.rect(screen, (100, 100, 100), (x, y, 300, 25))
    fill_width = int((max(0, hp) / max_hp) * 300)
    if fill_width > 0:
        pygame.draw.rect(screen, color, (x, y, fill_width, 25))
    lbl = font.render(label, True, (255, 255, 255))
    screen.blit(lbl, (x, y - 30))

def draw_ui_elements(screen, arena, player, font):
    if arena.phase == "intro" and arena.intro_step == "dialogue":
        draw_prompt(screen, "Guard: 'You're not supposed to be here, kid!' (Press E)", 640, 300)
    
    elif arena.phase == "movement":
        dist = abs(player.rect.centerx - arena.enemy.pos.x)
        if dist <= arena.attack_range:
            draw_prompt(screen, "Press E to Attack", 640, 600)
            
    elif arena.phase == "choose":
        overlay = pygame.Surface((400, 200), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (440, 200))
        for i, skill in enumerate(arena.player_skills):
            color = (255, 255, 0) if i == arena.selected_skill else (255, 255, 255)
            txt = font.render(skill.name, True, color)
            screen.blit(txt, (460, 220 + i * 40))

    elif arena.phase in ["player_atk", "enemy_atk", "result"]:
        draw_prompt(screen, arena.result_text, 640, 300)