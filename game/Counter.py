class Counter:
    def __init__(self, x, y, game):
        self.game = game
        self.value = 0
        self.x = x
        self.y = y

    def increment(self):
        if self.value < 10:
            self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

    def draw(self):
        counter_text = self.game.font.render(str(self.value), True, (255, 255, 255))
        self.game.screen.blit(counter_text, (self.x, self.y))
