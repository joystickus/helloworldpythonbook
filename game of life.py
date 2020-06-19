import pygame, time, easygui
from copy import copy

pygame.init()

# offer user to choose resolution of the window
resolution_x = 0
resolution_y = 0
resolution_choices = ['640 × 480', '800 × 600', '1024 × 768', '1280 × 1024', '1440 × 900', '1680 × 1050',
                      '1920 × 1080', '2560 × 1440']
resolution_choice = easygui.choicebox("Please select resolution", choices = resolution_choices, preselect = 1)
if resolution_choice == '640 × 480':
    resolution_x = 640
    resolution_y = 480
elif resolution_choice == '800 × 600':
    resolution_x = 800
    resolution_y = 600
elif resolution_choice == '1024 × 768':
    resolution_x = 1024
    resolution_y = 768
elif resolution_choice == '1280 × 1024':
    resolution_x = 1280
    resolution_y = 1024
elif resolution_choice == '1440 × 900':
    resolution_x = 1440
    resolution_y = 900
elif resolution_choice == '1680 × 1050':
    resolution_x = 1680
    resolution_y = 1050
elif resolution_choice == '1920 × 1080':
    resolution_x = 1920
    resolution_y = 1080
elif resolution_choice == '2560 × 1440':
    resolution_x = 2560
    resolution_y = 1440
screen = pygame.display.set_mode([resolution_x, resolution_y])
screen.fill([255, 255, 255])

cell_size = 30
cell_size_work = copy(cell_size)

#function to scale the field down
def scale():
    new_cell_size = int(resolution_x / (int(resolution_x / cell_size_work) + 2))
    return new_cell_size

field0 = int(cell_size_work / 2)
step = cell_size_work
center_field_x = field0 + step * (int(resolution_x / step / 2) - 1)
center_field_y = field0 + step * (int(resolution_y / step / 2) - 1)
dot_radius = int((cell_size_work / 2) * 0.7)

# function to check a cell to change state
def check(x, y):
    dots = {"dot1": [x - step, y - step],
            "dot2": [x, y - step],
            "dot3": [x + step, y - step],
            "dot4": [x - step, y],
            "dot5": [x + step, y],
            "dot6": [x - step, y + step],
            "dot7": [x, y + step],
            "dot8": [x + step, y + step]}
    count = 0
    center = False
    future = ""
    if screen.get_at([x, y]) == (0, 0, 0, 255):
        center = True
    for value in dots.values():
        if screen.get_at(value) == (0, 0, 0, 255):
            count += 1
    if center and 2 <= count <= 3:
        future = "live"
    elif center and (count < 2 or count > 3):
        future = "die"
    elif not center and count == 3:
        future = "born"
    else:
        future = "nothing"
    return future

# function to check borders
def border_check():
    top_left_starting_point = field0 + step
    top_rignt_starting_point = top_left_starting_point + (step * (int(resolution_x / cell_size_work) - 2))
    bottom_left_starting_point = top_left_starting_point + (step * (int(resolution_y / cell_size_work) - 2))
    presence = False
    while not presence:
        for i in range(int(resolution_x / step - 2)):
            dot_place = [top_left_starting_point + i * step, top_left_starting_point]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(int(resolution_y / step - 2)):
            dot_place = [top_left_starting_point, top_left_starting_point + i * step]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(int(resolution_x / step - 2)):
            dot_place = [top_rignt_starting_point, top_rignt_starting_point + i * step]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
        for i in range(int(resolution_x / step - 2)):
            dot_place = [bottom_left_starting_point + i * step, bottom_left_starting_point]
            if screen.get_at(dot_place) == (0, 0, 0, 255):
                presence = True
                break
    return "yes"

# draw the field
for i in range(0, resolution_x, step):
    pygame.draw.lines(screen, [0, 0, 0], False, [[i, 0], [i, resolution_y]], 1)
    pygame.draw.lines(screen, [0, 0, 0], False, [[0, i], [resolution_x, i]], 1)

pygame.display.flip()

'''
dot0 = [center_field_x + step * 0, center_field_y + step * 0]
dot1 = [center_field_x + step * 0, center_field_y - step * 1]
dot2 = [center_field_x + step * 1, center_field_y - step * 1]
dot3 = [center_field_x - step * 1, center_field_y + step * 0]
dot4 = [center_field_x + step * 0, center_field_y + step * 1]

r_pentomino = [dot0, dot1, dot2, dot3, dot4]

for i in r_pentomino:
    pygame.draw.circle(screen, [0, 0, 0], i, 15, 0)
'''

dot1 = [field0 + step * 2, field0 + step * 1]
dot2 = [field0 + step * 3, field0 + step * 2]
dot3 = [field0 + step * 3, field0 + step * 3]
dot4 = [field0 + step * 2, field0 + step * 3]
dot5 = [field0 + step * 1, field0 + step * 3]
glider = [dot1, dot2, dot3, dot4, dot5]

for i in glider:
    pygame.draw.circle(screen, [0, 0, 0], i, dot_radius, 0)

pygame.display.flip()

#'''
time.sleep(1)
for k in range(30):
    born = []
    die = []
    time.sleep(0.1)
    starting_point = field0 + step
    for i in range(int(resolution_x / step - 2)):
        for j in range(int(resolution_y / step - 2)):
            dot_place = [starting_point + i * step, starting_point + j * step]
            result = check(*dot_place)
            if result == "born":
                born.append(dot_place)
            elif result == "die":
                die.append(dot_place)
    for i in born:
        pygame.draw.circle(screen, [0, 0, 0], i, dot_radius, 0)
    for i in die:
        pygame.draw.circle(screen, [255, 255, 255], i, dot_radius, 0)
    # check = border_check()
    pygame.display.flip()
#'''

try1 = border_check()
print(try1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
