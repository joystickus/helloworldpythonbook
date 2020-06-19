# wrap the ball
import pygame, sys
pygame.init()
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode([screen_x,screen_y])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("sphere100.jpg")
x_position = 50
y_position = 50
x_speed = 1
y_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(3)
    screen.fill([255, 255, 255])
    x_position += x_speed
    # y_position += y_speed
    if x_position > screen.get_width():
        x_position = -100
    # if y_position > screen.get_height() - 100 or y_position < 0:
    #     y_speed = - y_speed
    screen.blit(my_ball, [x_position, y_position])
    pygame.display.flip()
pygame.quit()


# # bounce the ball
# import pygame, sys
# pygame.init()
# screen_x = 800
# screen_y = 600
# screen = pygame.display.set_mode([screen_x,screen_y])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("sphere100.jpg")
# x_position = 50
# y_position = 50
# x_speed = 1
# y_speed = 1
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.time.delay(3)
#     screen.fill([255, 255, 255])
#     pygame.draw.rect(screen, [0,0,0], [30, 30, screen_x-60, screen_y-60], 1)
#     x_position += x_speed
#     y_position += y_speed
#     if x_position > screen.get_width() - 130 or x_position < 30:
#         x_speed = - x_speed
#     if y_position > screen.get_height() - 130 or y_position < 30:
#         y_speed = - y_speed
#     screen.blit(my_ball, [x_position, y_position])
#     pygame.display.flip()
# pygame.quit()