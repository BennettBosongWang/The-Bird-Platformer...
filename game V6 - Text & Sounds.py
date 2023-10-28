# 'Ctrl + Alt + N' to run using code runner in VScode.
# This is the version where graphics got better.
import pygame
import time
import os
import math
import random

WIN = pygame.display.set_mode((900, 600))
bird = pygame.image.load('bird.png')
sky = pygame.image.load('Sky.jpg')
alould_arrow_keys = True
alould_WASD_keys = True
run_number = 0
bird_x_premath = 1
bird_y_premath = 1
birdX = 0
birdY = 0
spawn_point_transparency = 200
changeY_by_numbers = []
jump_index = 0
level = 1
move_up = False
small_jump = 0
allow_jumps = False
jump_reverse = 0
show_title_screen = True
level_names = ['Easy Start', 'Squeezing Through', 'Wall-jumps?',
               'Red Lava', 'Squeezing Through Again', 'You Won GameV6']
plat1_x_range = [0, 0]
plat1_y_range = [0, 0]
plat2_x_range = [0, 0]
plat2_y_range = [0, 0]
plat3_x_range = [0, 0]
plat3_y_range = [0, 0]
stored_values = [0, 0]


def gen_text(text: str, text_col: tuple, x: int, y: int):
    font = pygame.font.SysFont('Helvetica', 35, bold=True)
    text_img = font.render(text, True, text_col)
    WIN.blit(text_img, (x, y))


def gen_sound(sound_arg: str):
    if sound_arg == 'thump':
        sound = pygame.mixer.Sound('thump.wav')
        sound.play()
    if sound_arg == 'boom':
        sound = pygame.mixer.Sound('boom.wav')
        sound.play()


def lava_respawn():
    gen_sound('boom')
    global level
    level = 1
    go_00()


def lava():
    global level, birdX, birdY
    bird_points = [birdX, birdY, birdX + 50, birdY, birdX, birdY + 50, birdX + 50, birdY + 50]
    if level == 4:
        if bird_points[7] > 500:
            lava_respawn()
    if level == 5:
        if bird_points[7] > 495:
            lava_respawn()


def restrict_platforms():
    global birdX, birdY, allow_jumps, stored_values, level
    bird_points = [birdX, birdY, birdX + 50, birdY, birdX, birdY + 50, birdX + 50, birdY + 50]
    allow_jumps = False

    if True:
        if plat1_x_range[0] < bird_points[4] < plat1_x_range[1]:  # bird pushes agenst top of plat
            if plat1_y_range[0] < bird_points[5] < (plat1_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True
        if plat1_x_range[0] < bird_points[6] < plat1_x_range[1]:
            if plat1_y_range[0] < bird_points[7] < (plat1_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True

        if plat1_x_range[0] < bird_points[0] < plat1_x_range[1]:  # bird pushes agenst bottom of plat
            if plat1_y_range[0] < bird_points[1] < plat1_y_range[1]:
                birdY = stored_values[1]
        if plat1_x_range[0] < bird_points[2] < plat1_x_range[1]:
            if plat1_y_range[0] < bird_points[3] < plat1_y_range[1]:
                birdY = stored_values[1]

        if plat1_x_range[0] < bird_points[2] < plat1_x_range[1]:  # bird pushes agenst left of plat
            if plat1_y_range[0] < bird_points[3] < plat1_y_range[1]:
                birdX = stored_values[0]
        if plat1_x_range[0] < bird_points[6] < plat1_x_range[1]:
            if plat1_y_range[0] < (bird_points[7] - 2) < plat1_y_range[1]:
                birdX = stored_values[0]

        if plat1_x_range[0] < bird_points[0] < plat1_x_range[1]:  # bird pushes agenst right of plat
            if plat1_y_range[0] < bird_points[1] < plat1_y_range[1]:
                birdX = stored_values[0]
        if plat1_x_range[0] < bird_points[4] < plat1_x_range[1]:
            if plat1_y_range[0] < (bird_points[5] - 2) < plat1_y_range[1]:
                birdX = stored_values[0]

        # Plat 2
        if plat2_x_range[0] < bird_points[4] < plat2_x_range[1]:  # bird pushes agenst top of plat
            if plat2_y_range[0] < bird_points[5] < (plat2_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True

        if plat2_x_range[0] < bird_points[6] < plat2_x_range[1]:
            if plat2_y_range[0] < bird_points[7] < (plat2_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True

        if plat2_x_range[0] < bird_points[0] < plat2_x_range[1]:  # bird pushes agenst bottom of plat
            if plat2_y_range[0] < bird_points[1] < plat2_y_range[1]:
                birdY = stored_values[1]
        if plat2_x_range[0] < bird_points[2] < plat2_x_range[1]:
            if plat2_y_range[0] < bird_points[3] < plat2_y_range[1]:
                birdY = stored_values[1]

        if plat2_x_range[0] < bird_points[2] < plat2_x_range[1]:  # bird pushes agenst left of plat
            if plat2_y_range[0] < bird_points[3] < plat2_y_range[1]:
                birdX = stored_values[0]
        if plat2_x_range[0] < bird_points[6] < plat2_x_range[1]:
            if plat2_y_range[0] < (bird_points[7] - 2) < plat2_y_range[1]:
                birdX = stored_values[0]

        if plat2_x_range[0] < bird_points[0] < plat2_x_range[1]:  # bird pushes agenst right of plat
            if plat2_y_range[0] < bird_points[1] < plat2_y_range[1]:
                birdX = stored_values[0]
        if plat2_x_range[0] < bird_points[4] < plat2_x_range[1]:
            if plat2_y_range[0] < (bird_points[5] - 2) < plat2_y_range[1]:
                birdX = stored_values[0]

        # Plat 3
        if plat3_x_range[0] < bird_points[4] < plat3_x_range[1]:  # bird pushes agenst top of plat
            if plat3_y_range[0] < bird_points[5] < (plat3_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True

        if plat3_x_range[0] < bird_points[6] < plat3_x_range[1]:
            if plat3_y_range[0] < bird_points[7] < (plat3_y_range[1]):
                birdY = stored_values[1]
                allow_jumps = True

        if plat3_x_range[0] < bird_points[0] < plat3_x_range[1]:  # bird pushes agenst bottom of plat
            if plat3_y_range[0] < bird_points[1] < plat3_y_range[1]:
                birdY = stored_values[1]
        if plat3_x_range[0] < bird_points[2] < plat3_x_range[1]:
            if plat3_y_range[0] < bird_points[3] < plat3_y_range[1]:
                birdY = stored_values[1]

        if plat3_x_range[0] < bird_points[2] < plat3_x_range[1]:  # bird pushes agenst left of plat
            if plat3_y_range[0] < bird_points[3] < plat3_y_range[1]:
                birdX = stored_values[0]
        if plat3_x_range[0] < bird_points[6] < plat3_x_range[1]:
            if plat3_y_range[0] < (bird_points[7] - 2) < plat3_y_range[1]:
                birdX = stored_values[0]

        if plat3_x_range[0] < bird_points[0] < plat3_x_range[1]:  # bird pushes agenst right of plat
            if plat3_y_range[0] < bird_points[1] < plat3_y_range[1]:
                birdX = stored_values[0]
        if plat3_x_range[0] < bird_points[4] < plat3_x_range[1]:
            if plat3_y_range[0] < (bird_points[5] - 2) < plat3_y_range[1]:
                birdX = stored_values[0]

        stored_values = [birdX, birdY]


def draw_platforms():
    global plat1_x_range, plat1_y_range, plat2_x_range, plat2_y_range, plat3_x_range, plat3_y_range
    if level == 1:
        gen_plat_list = gen_plat(1, [False, 100, 750, 300, 350]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))
        gen_plat(2, [True])
        gen_plat(3, [True])

    if level == 2:
        gen_plat_list = gen_plat(1, [False, 100, 750, 300, 350]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))

        gen_plat_list = gen_plat(2, [False, 100, 150, 0, 240]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))
        gen_plat(3, [True])

    if level == 3:
        gen_plat_list = gen_plat(1, [False, 100, 750, 300, 350]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))

        gen_plat_list = gen_plat(2, [False, 700, 750, 135, 350]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))
        gen_plat(3, [True])

    if level == 4:
        gen_plat_list = gen_plat(1, [False, 100, 750, 300, 350]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))

        gen_plat_list = gen_plat(2, [False, 0, 900, 500, 600]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255 - random.randint(0, 15)) 
        pygame.draw.rect(surface, (255, 100, 100), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))
        gen_plat(3, [True])

    if level == 5:
        plat1_x_range = [100, 650]
        plat1_y_range = [300, 350]
        rect = pygame.Rect(0, 0, 550, 50) #dimensions
        surface = pygame.Surface((550, 50)) #same as above
        surface.set_alpha(255) #trsnsparency
        pygame.draw.rect(surface, (0, 0, 0), rect) # color
        WIN.blit(surface, (100, 300)) #X & Y

        gen_plat_list = gen_plat(2, [False, 650, 900, 0, 230]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255) 
        pygame.draw.rect(surface, (0, 0, 0), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))

        gen_plat_list = gen_plat(3, [False, 0, 900, 495, 600]) #no plat, far left-pos, far right pos, far top pos, far bottom pos
        rect = pygame.Rect(0, 0, gen_plat_list[0], gen_plat_list[1])
        surface = pygame.Surface((gen_plat_list[0], gen_plat_list[1]))
        surface.set_alpha(255 - random.randint(0, 15)) 
        pygame.draw.rect(surface, (255, 100, 100), rect)
        WIN.blit(surface, (gen_plat_list[2], gen_plat_list[3]))
        gen_plat(3, [True])



def gen_plat(plat_number: int, info):
    global plat1_x_range, plat1_y_range, plat2_x_range, plat2_y_range, plat3_x_range, plat3_y_range
    if info[0] == True:
        if plat_number == 1:
            plat1_x_range = [0, 0]
            plat1_y_range = [0, 0]
        if plat_number == 2:
            plat2_x_range = [0, 0]
            plat2_y_range = [0, 0]
        if plat_number == 3:
            plat3_x_range = [0, 0]
            plat3_y_range = [0, 0]
        return
    if info[0] == False:
        if plat_number == 1:
            plat1_x_range = [info[1], info[2]]
            plat1_y_range = [info[3], info[4]]
        if plat_number == 2:
            plat2_x_range = [info[1], info[2]]
            plat2_y_range = [info[3], info[4]]
        if plat_number == 3:
            plat3_x_range = [info[1], info[2]]
            plat3_y_range = [info[3], info[4]]
        return[info[2] - info[1], info[4] - info[3], info[1], info[3]]


def create_movement_list():
    global movement_list
    original_list = [math.log(i, 1000) * 150 for i in range(1, 5)]
    movement_list = [x - y for x, y in zip(original_list[1:], original_list[:-1])]


def spawnpoint_transparency_sub():
    global spawn_point_transparency
    if spawn_point_transparency > 0:
        spawn_point_transparency -= 3


def go_00():
    global birdX, birdY, spawn_point_transparency
    spawn_point_transparency = 200
    birdX = 0
    birdY = 0


def restrict_area():  # restricts the area the bird
    global birdX, birdY, level, move_up, level_names
    # if the bird goes left
    if birdX < 0:
        go_00()
    # if the bird goes up
    if birdY < 0:
        go_00()
    # if the bird goes down
    if birdY > 550:
        go_00()
    # if the bird goes right
    if birdX > 850:
        level += 1
        print(f'level: {level} - {level_names[level - 1]}')
        go_00()
    lava()
    restrict_platforms()


def prerun_prep():
    global run, jump, level, level_names
    pygame.init()  # initializes music
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)  # plays indefinety
    jump = 40
    run = True
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(f'Script directory: {script_dir}')
    os.chdir(script_dir)
    cwd = os.getcwd()
    print(f'New working directory: {cwd}')
    pygame.init()
    print(f'Pygame version: {pygame.__version__}')
    create_movement_list()
    return run


def draw():
    global birdX, birdY, move_up, small_jump, jump, show_title_screen
    WIN.blit(sky, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        birdX = birdX + bird_x_premath * 7
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        birdX = birdX - bird_x_premath * 7
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        show_title_screen = False
        if allow_jumps:
            jump = 20
    if keys[pygame.K_SPACE]:
        show_title_screen = False

    if jump > 0:
        birdY = birdY - bird_y_premath * movement_list[jump_index]
    birdY = birdY + bird_y_premath * 7
    jump -= 1
    if jump == 18:
        gen_sound('thump')

    rect = pygame.Rect(0, 0, 50, 50)
    surface = pygame.Surface((50, 50))
    surface.set_alpha(spawn_point_transparency)
    pygame.draw.rect(surface, (0, 200, 0), rect)
    WIN.blit(surface, (0, 0))

    WIN.blit(bird, (birdX, birdY))
    draw_platforms()
    text = f'Level: {level} - {level_names[level - 1]}'
    gen_text(text=text, text_col=(0, 0, 0), x=0, y=560)
    if show_title_screen:
        WIN.blit(sky, (-900, 0))
    pygame.display.flip()


def main():
    run = prerun_prep()
    while run:
        time.sleep(0.024)
        global run_number
        run_number += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                WIN.blit(sky, (-1800, 0))
                pygame.mixer.music.fadeout(1000)
                pygame.display.flip()
                time.sleep(1)
                run = False
        spawnpoint_transparency_sub()
        draw()
        restrict_area()
    pygame.quit()


if __name__ == "__main__":
    main()
