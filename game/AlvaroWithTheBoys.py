import pygame
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class AlvaroWithTheBoys():
    def __init__(self, game, difficulty):
        pygame.init()
        self.difficulty = difficulty
        self.game = game
        self.name = "Alvaro with the boys"


    def run(self):
        running = True
        while running:

            self.game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            pygame.init()
            text = ("You chose mode: " + self.name + " and difficulty: " + Difficulty(self.difficulty).name)
            chosen_text = self.game.font.render(text, True, (255, 255, 255))
            chosen_text_rect = chosen_text.get_rect()
            chosen_text_rect.center = (self.game.screen.get_width() // 2, 150)
            self.game.screen.blit(chosen_text, chosen_text_rect)
            self.game.draw_alvaro()
            pygame.display.update()
