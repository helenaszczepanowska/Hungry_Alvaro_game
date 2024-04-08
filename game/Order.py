import pygame
import Button
import Topping
import Pizza
import Counter


class Order:
    def __init__(self, pizza, toppings_amount, min_amount, max_amount, mode, game):
        self.pizza = pizza
        self.game = game
        self.mode = mode
        self.toppings_amount = toppings_amount
        self.required_pizza = Pizza.Pizza(pizza.x, pizza.y, pizza.scale)
        self.required_pizza.generate_pizza(toppings_amount, min_amount, max_amount)
        self.counter = Counter.Counter(170, 80, game)
        self.pressed_topping = None
        self.setup_buttons()

    def display_order(self):
        position = 0
        for topping in self.required_pizza.toppings:
            text = (str(topping) + " x " + str(topping.quantity))
            topping_text = self.game.font.render(text, True, (255, 255, 255))
            topping_text_rect = topping_text.get_rect()
            topping_text_rect.topleft = (540, 30 + position * 30)
            self.game.screen.blit(topping_text, topping_text_rect)
            position += 1

        if self.pressed_topping:
            text = (str(self.pressed_topping))
        else:
            text = "Choose topping"

        topping_text = self.game.font.render(text, True, (255, 255, 255))
        topping_text_rect = topping_text.get_rect()
        topping_text_rect.topleft = (170, 30)
        self.game.screen.blit(topping_text, topping_text_rect)

    def display_score(self):
        text = ("Score: " + str(self.mode.score))
        score_text = self.game.font.render(text, True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (280, 520)
        self.game.screen.blit(score_text, score_text_rect)

    def check_order(self):
        made = self.pizza.toppings
        required = self.required_pizza.toppings

        for i in range(len(required)):
            if i < len(made):
                if made[i].name == required[i].name and made[i].quantity == required[i].quantity:
                    self.mode.score += 100//(self.toppings_amount + 1)

    def make_order(self):
        running = True
        while running:

            self.game.screen.fill((242, 177, 202))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

            self.pizza.draw_pizza(self.game.screen)
            self.display_order()
            self.counter.draw()
            self.display_buttons()
            self.pizza.draw_toppings(self.game.screen)
            self.display_score()
            pygame.display.update()

    def setup_buttons(self):
        # Toppings
        cheese_img = pygame.image.load("img/cheese.png")
        self.cheese_button = Button.Button(15, 10, cheese_img, 0.15)

        mushrooms_img = pygame.image.load("img/mushrooms.png")
        self.mushrooms_button = Button.Button(15, 80, mushrooms_img, 0.15)

        salami_img = pygame.image.load("img/salami.png")
        self.salami_button = Button.Button(15, 150, salami_img, 0.15)

        pineapple_img = pygame.image.load("img/pineapple.png")
        self.pineapple_button = Button.Button(15, 230, pineapple_img, 0.15)

        # "+", "-"
        minus_img = pygame.image.load("buttons_img/minus_button.png")
        self.minus_button = Button.Button(240, 80, minus_img, 0.07)

        plus_img = pygame.image.load("buttons_img/plus_button.png")
        self.plus_button = Button.Button(280, 80, plus_img, 0.07)

        # Add, Back
        back_img = pygame.image.load("buttons_img/back_button.png")
        self.back_button = Button.Button(15, 500, back_img, 0.25)

        add_img = pygame.image.load("buttons_img/add_button.png")
        self.add_button = Button.Button(90, 500, add_img, 0.25)

        # Done
        done_img = pygame.image.load("buttons_img/done_button.png")
        self.done_button = Button.Button(450, 500, done_img, 0.25)

    def display_buttons(self):
        # Toppings buttons
        if self.cheese_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 10 * self.pizza.scale, self.pizza.y + 10 * self.pizza.scale,
                                  Topping.ToppingName(1), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.mushrooms_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(3), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.salami_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(2), 1,
                                  self.pizza.scale)
            self.pressed_topping = top
        if self.pineapple_button.draw(self.game.screen):
            top = Topping.Topping(self.pizza.x + 50 * self.pizza.scale, self.pizza.y + 50 * self.pizza.scale,
                                  Topping.ToppingName(4),
                                  1,
                                  self.pizza.scale)
            self.pressed_topping = top

        # Counter buttons
        if self.plus_button.draw(self.game.screen):
            self.counter.increment()

        if self.minus_button.draw(self.game.screen):
            self.counter.decrement()

        if self.back_button.draw(self.game.screen):
            self.pizza.remove_last_topping()

        if self.add_button.draw(self.game.screen):
            self.pressed_topping.quantity = self.counter.value
            self.pizza.add_topping(self.pressed_topping)

        if self.done_button.draw(self.game.screen):
            self.check_order()
            pygame.mouse.set_pos(self.game.screen.get_width() // 2, self.game.screen.get_height() // 2)
            self.mode.next_order()
