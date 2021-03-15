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

BigBird = pygame.Surface((300, 200))#, pygame.SRCALPHA)
ellipse(BigBird, (255,255,255), (50, 85, 130, 60))
ellipse(BigBird, (255,255,255), (150, 90, 70, 30))
ellipse(BigBird, (255,255,255), (200, 80, 40, 30))
polygon(BigBird, (128, 0, 128), ((240,90),(260,85),(265,90),(260,95),(240,100)))
screen.blit(BigBird, (50, 220))

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()