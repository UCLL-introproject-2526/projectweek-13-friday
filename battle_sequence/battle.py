import pygame
from .skills import player_skills


class Battle:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

        # enemy stats
        self.enemy_hp = 20

        # battle zelf
        self.phase = "dialogue"   # dialogue -> choose -> result -> end
        self.selected = 0         # which skill is selected

        self.running = True

        # background shiz..
        self.background = pygame.image.load("Rooms/arena.png").convert()
        self.background = pygame.transform.scale(
            self.background,
            (self.screen.get_width(), self.screen.get_height())
        )

        # dialogue..
        self.dialogue = [
            "Guard: blahblah?",
            "Player: blah blah!",
            "Guard: blah blah blah..",
            "Player: blahblahblah!!!!!"
        ]

        self.dialogue_index = 0

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                # blah blah blah..
                if self.phase == "dialogue":
                    if event.key == pygame.K_SPACE:
                        self.dialogue_index += 1

                        # als dialogue klaar is..
                        if self.dialogue_index >= len(self.dialogue):
                            self.phase = "choose"

                # choose a skill
                elif self.phase == "choose":
                    if event.key == pygame.K_UP:
                        self.selected -= 1
                    if event.key == pygame.K_DOWN:
                        self.selected += 1

                    # keep selection inside list
                    self.selected %= len(player_skills)

                    if event.key == pygame.K_RETURN:
                        self.use_skill()

                # result phase
                elif self.phase == "result":
                    if event.key == pygame.K_SPACE:
                        self.phase = "end"

    def use_skill(self):
        skill = player_skills[self.selected]

        # apply damage
        self.enemy_hp -= skill.damage

        # check if enemy defeated
        if self.enemy_hp <= 0:
            self.result_text += " Enemy defeated!"

        self.phase = "result"

    def draw(self):
        # self.screen.fill((20, 20, 20))    # niet meer nodig want bg is photo..
        self.screen.blit(self.background, (0, 0))

        # draw enemy HP
        hp_text = self.font.render(f"Enemy HP: {self.enemy_hp}", True, (255, 0, 0))
        self.screen.blit(hp_text, (50, 50))

        # dialoog screen
        if self.phase == "dialogue":
            # dialoog box
            pygame.draw.rect(self.screen, (0, 0, 0), (150, 380, 800, 120))
            pygame.draw.rect(self.screen, (255, 255, 255), (150, 380, 800, 120), 2)

            # current dialoog zin
            current_text = self.dialogue[self.dialogue_index]
            text_surface = self.font.render(current_text, True, (255, 255, 255))
            self.screen.blit(text_surface, (170, 420))

        # skill selection screen
        elif self.phase == "choose":
            for i, skill in enumerate(player_skills):
                color = (255, 255, 0) if i == self.selected else (255, 255, 255)
                skill_text = self.font.render(skill.name, True, color)
                self.screen.blit(skill_text, (200, 350 + i * 40))

        # result screen
        elif self.phase == "result":
            text = self.font.render(self.result_text, True, (255, 255, 255))
            self.screen.blit(text, (200, 400))

            continue_text = self.font.render(
                "Press SPACE to continue",
                True,
                (180, 180, 180)
            )
            self.screen.blit(continue_text, (200, 450))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input(events)
            self.draw()

            if self.phase == "end":
                self.running = False

            clock.tick(60)
