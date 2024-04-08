import pygame
import Pizza
import Order
from enum import Enum

class HungryAlvaro:
    def __init__(self, game, difficulty):
        pygame.init()
        self.difficulty = difficulty
        self.is_running = True
        self.game = game
        self.score = 0
        self.name = "Hungry Alvaro"
        self.current_order = -1
        self.orders = []

    def run(self):
        if self.difficulty == 1:
            self.number_of_orders = 3
        elif self.difficulty == 2:
            self.number_of_orders = 5
        else:
            self.number_of_orders = 8
        self.next_order()

    def next_order(self):
        self.current_order += 1
        if self.current_order < self.number_of_orders:
            order = Order.Order(Pizza.Pizza(160, 150, 0.70), 4, 2, 5, self, self.game)
            self.orders.append(order)
            order.make_order()
        else:
            self.display_final_score()

    def display_final_score(self):
        running = True
        while running:
            self.game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            pygame.init()
            text = ("Your final score is: " + str(self.score))
            score_text = self.game.font.render(text, True, (255, 255, 255))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (self.game.screen.get_width()//2, self.game.screen.get_height()//2)
            self.game.screen.blit(score_text, score_text_rect)
            pygame.display.update()




