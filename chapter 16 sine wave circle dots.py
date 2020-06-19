import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])

for x in range(640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
    pygame.draw.circle(screen, [0,0,0],[x, y], 1, 0) 

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
