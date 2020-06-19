import pygame
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
#pygame.draw.circle(screen, THECOLORS["grey"],[320, 240], 150, 0)
pygame.draw.rect(screen, THECOLORS["gold"],[0, 0, 150, 100], 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

'''
import pygame
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
pygame.draw.circle(screen, THECOLORS["red"],[320,240], 30, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
'''
