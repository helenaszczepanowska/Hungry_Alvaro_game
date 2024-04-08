import pygame
from enum import Enum


class ToppingName(Enum):
    CHEESE = 1
    SALAMI = 2
    HAM = 5
    CHICKEN = 6
    MUSHROOMS = 3
    ONIONS = 8
    PEPPERS = 9
    OLIVES = 10
    CORN = 11
    TOMATOES = 12
    PINEAPPLE = 4
    SPINACH = 14
    ARUGULA = 15


class Topping():
    def __init__(self, x, y, name, quantity, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.name = name
        self.quantity = quantity
        self.image = None
        self.rect = None
        self.set_image()

    def set_image(self):
        if self.name.value == 1:
            self.image = pygame.image.load("img/cheese.png")

        if self.name.value == 2:
            self.image = pygame.image.load("img/salami.png")

        if self.name.value == 3:
            self.image = pygame.image.load("img/mushrooms.png")

        if self.name.value == 4:
            self.image = pygame.image.load("img/pineapple.png")

        # more to do

    def draw(self, surface):
        if self.image:
            width, height = self.image.get_size()
            image = pygame.transform.scale(self.image, (int(width * self.scale), int(height * self.scale)))
            self.rect = image.get_rect()
            self.rect.topleft = (self.x, self.y)
            surface.blit(image, (self.rect.x, self.rect.y))

    def __str__(self):
        formatted_name = self.name.name.replace("_", " ").title()
        return formatted_name
