import pygame
from pygame.draw import *
from random import randint

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 211, 0)
BLACK = (0, 0, 0)
FPS = 60
SCREEN_SIZE = (1200, 900)
font = pygame.font.Font(None, 150)

class Ball:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def change_pos(self, speed):
        self.y -= speed
    def draw(self, screen):
        # Рисует сам шарик
        circle(screen, self.color, (self.x, self.y), self.r)
        # Рисует блик
        for i in range(self.r):
            circle(screen, [int(c + (255 - c) * i / self.r) for c in self.color],
                   [self.x + int(i / 2), self.y - int(i / 2)], self.r - i)
        # Рисует вереовчку
        lines(screen, BLACK, False, [[self.x, self.y + self.r], [self.x, self.y + 2 * self.r]], 1)
        # Рисует треугольник
        polygon(screen, self.color, [
            (self.x, self.y + self.r),
            (self.x + int(self.r / 10), self.y + self.r + int(self.r / 10)),
            (self.x - int(self.r / 10), self.y + self.r + int(self.r / 10)),
        ])

    def pos_inside(self, pos):
        a = pos[0] - self.x
        b = pos[1] - self.y
        return a ** 2 + b ** 2 < self.r ** 2


class CloseButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect(screen, RED, (0, 0, self.x, self.y))

    def pos_inside(self, pos):
        a = pos[0] - self.x
        b = pos[1] - self.y
        return a < 0 and b < 0


class Game:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        self.closeButton = CloseButton(200, 200)
        self.balls = []
        self.score = 0

    def draw_score(self):
        text = font.render("Score: " + str(self.score), True, YELLOW)
        self.screen.blit(text, [200, 10])

    def add_ball(self):
        x = randint(int(self.screen_size[0] * 0.1), int(self.screen_size[0] * 0.9))
        y = SCREEN_SIZE[1]
        r = randint(10, max(10, min(self.screen_size) * 0.1))
        color = [randint(0, 255) for _ in range(3)]
        self.balls.append(Ball(x, y, r, color))

    def draw(self):
        self.screen.fill(WHITE)
        for ball in self.balls:
            ball.change_pos(5 + self.score / 3)
            ball.draw(self.screen)
        self.closeButton.draw(self.screen)
        self.draw_score()
        pygame.display.update()

    def on_click(self, pos):
        if self.closeButton.pos_inside(pos):
            pygame.quit()
            exit(1)
        for ball in self.balls:
            if ball.pos_inside(pos):
                self.balls.remove(ball)
                self.score += 1


clock = pygame.time.Clock()
game = Game(SCREEN_SIZE)
finished = False

while not finished:
    clock.tick(FPS)
    game.draw()
    game.add_ball()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            game.on_click(pygame.mouse.get_pos())

pygame.quit()