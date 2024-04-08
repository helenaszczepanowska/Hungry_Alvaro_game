import pygame
import Topping
import random


class Pizza():
    def __init__(self, x, y, scale):
        self.rect = None
        self.scale = scale
        self.image = pygame.image.load("img/dough_sauce.png")
        self.x = x
        self.y = y
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_last_topping(self):
        self.toppings.pop()

    def generate_pizza(self, toppings_amount, min_amount_topping, max_amount_topping):
        available_toppings = [i for i in range(2, 6)]
        cheese = Topping.Topping(self.x, self.y, Topping.ToppingName(1), 1, self.scale)
        self.toppings.append(cheese)
        random.shuffle(available_toppings)

        for i in range(toppings_amount):
            rand_amount = random.randint(min_amount_topping, max_amount_topping)
            top = Topping.Topping(self.x + 50 * self.scale, self.y + 50 * self.scale,
                                  Topping.ToppingName(available_toppings[i]), rand_amount, self.scale)
            self.add_topping(top)

    def draw_pizza(self, surface):
        width, height = self.image.get_size()
        new_image = pygame.transform.scale(self.image, (int(width * self.scale), int(height * self.scale)))
        self.rect = new_image.get_rect()
        self.rect.topleft = (self.x, self.y)
        surface.blit(new_image, (self.rect.x, self.rect.y))

    def draw_toppings(self, surface):
        for topping in self.toppings:
            topping.draw(surface)
