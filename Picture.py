import pygame
import pygame.surface

from pygame.draw import *

def DrawBackgroundLine(color, coord, size):
    rect(screen, color, (0, coord, 400, size))

def DrawBird(location, rotangle):
    Bird1 = pygame.Surface((100, 30), pygame.SRCALPHA)
    Bird1 = pygame.transform.rotate(Bird1, rotangle)
    arc(Bird1, (255, 255, 255), (50, 0, 50, 30), 0.2, 3, 3)
    arc(Bird1, (255, 255, 255), (0, 0, 50, 30), 0.2, 3, 3)
    screen.blit(Bird1, location)

def DrawBigBird(size, location):
    BigBird = pygame.Surface((size, size * 2 / 3), pygame.SRCALPHA)
    #тело и голова
    ellipse(BigBird, (255, 255, 255), (size / 6, size / 3.5, size / 2.3, size / 5))
    ellipse(BigBird, (255, 255, 255), (size / 2, size / 3.3, size / 4.3, size / 10))
    ellipse(BigBird, (255, 255, 255), (size * 2 / 3, size / 3.75, size / 7.5, size / 10))
    ellipse(BigBird, (0, 0, 0), (size / 1.36, size / 3.53, size / 30, size / 32))
    #клюв
    polygon(BigBird, (255, 165, 0), ((size / 1.25, size / 3.3), (size / 1.15, size / 3.53), (size / 1.13, size / 3.3), (size / 1.15, size / 3), (size / 1.26, size / 3)))
    #крылья
    polygon(BigBird, (255, 255, 255), (
    (size / 2.1, size / 3.3), (size / 3.6, size / 3.3), (size / 3, size / 4), (size / 20, size / 20), (size / 2.8, size / 6.7), (size / 2, size / 4.3)))
    screen.blit(BigBird, location)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 500))

DrawBackgroundLine((0, 0, 64),0,70)
DrawBackgroundLine((133, 64, 148),70,30)
DrawBackgroundLine((255, 128, 192),100,60)
DrawBackgroundLine((255, 108, 142),160,80)
DrawBackgroundLine((254, 196, 1),240,40)
DrawBackgroundLine((0, 100, 100),280,220)

DrawBird((100, 100), 3)
DrawBird((50, 60), 3)
DrawBird((280, 80), 3)

DrawBigBird(300, (50, 220))

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()