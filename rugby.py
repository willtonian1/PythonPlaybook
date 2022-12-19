#TOM WILLIAMS 2021
#Python Playbook
#Currently under re-construction

from re import T
import pygame
import time
import ast
import sys
import modules.animate as animation
import modules.in_draw_menu as menus

# variables declaration
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
c_count = 0
current_no = 10
prev_pos = (0, 0)
click_path = []
open_input = "Unnamed"

# initiation
pygame.init()

# window setup
pygame.display.set_caption('Rugby Moves')
window = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#00ff00'))
window.blit(background, (0, 0))
# font
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.update()

# function section
def generate_string_points(player_array, iteration):
    string = player_array[iteration]
    #print('string1: ' + str(string))
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.split(',')
    print(string)
    return string 

def generate_string_points2(player_array, iteration):
    string = player_array[iteration+1]
    #print('string2: ' + str(string))
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.split(',')
    print(string)
    return string 
      




def draw_menu():
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(250, 200, 300, 100))
    txt = font.render("Python Playbook", False, WHITE)
    window.blit(txt, (260, 230))

    # DRAW BUTTON
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(300, 350, 200, 70))
    txt = font.render("Draw", False, WHITE)
    window.blit(txt, (350, 375))
    pygame.display.update()


def getCo(click_position):
    global click_path
    global font
    click_path.append(str(click_position))

    return print("clickpath: " + str(click_path))


def draw_point(pos, cn):
    global window
    global font
    pygame.draw.circle(window, BLACK, pos, 20)
    pygame.display.update()
    txt = font.render(str(cn), False, WHITE)
    window.blit(txt, pos)
    return 0


def draw_arrow():
    pygame.draw.line(window, (255, 0, 0), prev_pos, pos)
    return 0


def save_clickpath():
    user_text = ''
    #play_name = str(input('Play Name: '))
    #loop for typing input
    entered = False
    while entered == False: #loop for entering title of the move
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
  
                 # Check for backspace
                if event.key == pygame.K_RETURN:
                    entered = True
                    play_name = user_text
                if event.key == pygame.K_BACKSPACE:
  
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
                else:
                    user_text += event.unicode

        pygame.draw.rect(window, (255,0,0), pygame.Rect(300,200,200,36))
        text_surface = font.render(user_text, True, (255, 255, 255))
        window.blit(text_surface, (300,200))
        
        pygame.display.update()


    book = open('user_plays/' + str(play_name) + '.txt', 'w+')
    book.writelines(str(click_path))
    book.close()
    window.blit(background, (0, 0))
    return 0


def open_move():
    global open_input
    current_player_no = 10
    # open a file and read the array.
    user_text = ''
    entered = False
    while entered == False: #loop for entering title of the move
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
  
                 # Check for backspace
                if event.key == pygame.K_RETURN:
                    entered = True
                    open_input = user_text
                if event.key == pygame.K_BACKSPACE:
  
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
                else:
                    user_text += event.unicode

        pygame.draw.rect(window, (255,0,0), pygame.Rect(300,200,200,36))
        text_surface = font.render(user_text, True, (255, 255, 255))
        window.blit(text_surface, (300,200))
        
        pygame.display.update()

    global move
    book = open('user_plays/' + open_input + '.txt', 'r')
    move = ast.literal_eval(book.read())
    window.blit(background, (0, 0))
    book.close()

    # adapting the string and creating a point for circles and the lines too.
    count = 0

    for each_circle in range(len(move)):
        # checking if the item in the list is a point, or a change in player_no
        if isinstance(move[each_circle], int) == False:
            string = move[each_circle]
            string = string.replace('(', '')
            string = string.replace(')', '')
            string = string.split(',')
            print(string)
            point = (int(string[0]), int(string[1]))
            pygame.draw.circle(window, BLACK, point, 20)

            # nnumber drawing
            txt = font.render(str(current_player_no), False, WHITE)
            window.blit(txt, point)

        else:  # means no line will be drawn
            print(str(move[each_circle]))
            count = -1  # means the lines of different players will not be connected!
            current_player_no = move[each_circle]

        # lines drawn
        if count >= 1:
            pygame.draw.line(window, (255, 0, 0), prev_point, point)

        count += 1
        prev_point = point
    return 0


game = True
window.blit(background, (0, 0))
draw_menu()
while game:
    # main loop
    position_for_press = str(pygame.mouse.get_pos())
    position_for_press = position_for_press.replace('(', '')
    position_for_press = position_for_press.replace(')', '')
    position_for_press = position_for_press.split(',')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()

    if (event.type == pygame.MOUSEBUTTONUP) and (300 < int(position_for_press[0]) < 500) and (350 < int(position_for_press[1]) < 420):
        draw_is_running = True
        window.blit(background, (0, 0))
        time.sleep(0.5)
        menus.in_draw_menu(window, open_input, WHITE, font)
    else:
        draw_is_running = False

    while draw_is_running:
        menus.in_draw_menu(window, open_input, WHITE, font)

        # inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                sys.exit()

            # keys pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("yesss")
                    click_path.append(current_no + 1)
                    c_count = 0
                    current_no += 1

                # saving a move
                if event.key == pygame.K_s:
                    print('save')
                    save_clickpath()
                    

                    

                    click_path = []
                    prev_pos = pos
                    c_count = 0
                    menus.in_draw_menu(window, open_input, WHITE, font)

                # bringing up old moves
                if event.key == pygame.K_o:
                    
                    print('open')
                    open_move()
                    click_path = []
                    c_count = 0
                    print("Open input: " + str(open_input))

                    menus.in_draw_menu(window, open_input, WHITE, font)

                # blank
                if event.key == pygame.K_b:
                    print('blank')
                    window.blit(background, (0, 0))
                    click_path = []
                    c_count = 0
                    menus.in_draw_menu(window, open_input, WHITE, font)

                #animate
                if event.key ==pygame.K_a:
                    animation.animate(window, background, move, open_input, WHITE, font)



        # menu inputs!!!
        position_for_press = str(pygame.mouse.get_pos())
        position_for_press = position_for_press.replace('(', '')
        position_for_press = position_for_press.replace(')', '')
        position_for_press = position_for_press.split(',')
        if (event.type == pygame.MOUSEBUTTONUP) and (30 < int(position_for_press[0]) < 130) and (30 < int(position_for_press[1]) < 90):
            window.blit(background, (0, 0))
            print('hello')
            click_path = []
            c_count = 0

            draw_is_running = False
            draw_menu()

        # mouse pressed
        elif event.type == pygame.MOUSEBUTTONUP:
            print('hi')
            pos = pygame.mouse.get_pos()
            getCo(pos)  # taking mouse co-ordinates and saving them
            draw_point(pos, current_no)  # circle drawing and number render
            if c_count >= 1:  # checks if it is the first point (no arrow)
                draw_arrow()  # connects previous and current point

            prev_pos = pos
            c_count += 1
            time.sleep(0.5)

    

        
        
        pygame.display.update()  # update the window
