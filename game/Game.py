import pygame
import Button
import HungryAlvaro
import MoodyAlvaro
import AlvaroWithTheBoys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pizza Game")
        icon = pygame.image.load("img/pizzaicon.png")
        pygame.display.set_icon(icon)
        self.font = pygame.font.SysFont("", 40)
        self.setup_buttons()
        self.setup_text()

    def setup_buttons(self):
        
        # Hungry Alvaro button
        hungry_alvaro_button_img = pygame.image.load("buttons_img/button_hungry-alvaro.png")
        self.hungry_alvaro_button = Button.Button(500, 250, hungry_alvaro_button_img, 1)

        # Moody Alvaro button
        moody_alvaro_button_img = pygame.image.load("buttons_img/button_moody-alvaro.png")
        self.moody_alvaro_button = Button.Button(500, 305, moody_alvaro_button_img, 1)

        # Alvaro with the boys button
        alvaro_with_the_boys_button_img = pygame.image.load("buttons_img/button_alvaro-with-the-boys.png")
        self.alvaro_with_the_boys_button = Button.Button(500, 360, alvaro_with_the_boys_button_img, 1)

        # Exit button
        exit_button_img = pygame.image.load("buttons_img/button_exit.png")
        self.exit_button = Button.Button(500, 415, exit_button_img, 1)

        # Easy button
        easy_button_img = pygame.image.load("buttons_img/button_easy.png")
        self.easy_button = Button.Button(500, 250, easy_button_img, 1)

        # Medium button
        medium_button_img = pygame.image.load("buttons_img/button_medium.png")
        self.medium_button = Button.Button(500, 305, medium_button_img, 1)

        # Hard button
        hard_button_img = pygame.image.load("buttons_img/button_hard.png")
        self.hard_button = Button.Button(500, 360, hard_button_img, 1)
    
    def setup_text(self):
        self.intro_text = self.font.render("Choose your mode", True, (255, 255, 255))
        self.intro_text_rect = self.intro_text.get_rect()
        self.intro_text_rect.center = (200, 150)

        self.difficulty_text = self.font.render("Choose your difficulty", True, (255, 255, 255))
        self.difficulty_text_rect = self.difficulty_text.get_rect()
        self.difficulty_text_rect.center = (200, 150)
        
    def main_menu(self):
        running = True
        while running:

            self.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.hungry_alvaro_button.draw(self.screen):
                pygame.mouse.set_pos(self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.choose_difficulty(1)
            if self.moody_alvaro_button.draw(self.screen):
                pygame.mouse.set_pos(self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.choose_difficulty(2)
            if self.alvaro_with_the_boys_button.draw(self.screen):
                pygame.mouse.set_pos(self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.choose_difficulty(3)

            if self.exit_button.draw(self.screen):
                running = False

            self.screen.blit(self.intro_text, self.intro_text_rect)
            self.draw_alvaro()
            pygame.display.update()

    def choose_difficulty(self, mode):
        running = True
        while running:

            self.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            if self.easy_button.draw(self.screen):
                self.play(mode, 1)
            if self.medium_button.draw(self.screen):
                self.play(mode, 2)
            if self.hard_button.draw(self.screen):
                self.play(mode, 3)

            self.screen.blit(self.difficulty_text, self.difficulty_text_rect)
            self.draw_alvaro()
            pygame.display.update()

    def play(self, mode, difficulty):
        if mode == 1:
            chosen_mode = HungryAlvaro.HungryAlvaro(self, difficulty)
        elif mode == 2:
            chosen_mode = MoodyAlvaro.MoodyAlvaro(self, difficulty)
        else:
            chosen_mode = AlvaroWithTheBoys.AlvaroWithTheBoys(self, difficulty)
        chosen_mode.run()

    def draw_alvaro(self):
        self.alvaroImg = pygame.image.load("img/alvaro.png")
        self.ciaoImg = pygame.image.load("img/ciao.png")
        self.screen.blit(self.alvaroImg, (100, 450))
        self.screen.blit(self.ciaoImg, (150, 300))

