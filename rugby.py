import pygame
import time



BLACK =     (0, 0, 0)
WHITE = (255,255,255)
c_count = 0 
current_no =10

prev_pos = (0,0)
pygame.init()

pygame.display.set_caption('Rugby Moves')
window = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#00ff00'))


font = pygame.font.Font('freesansbold.ttf', 32)

#function section
click_path = []

def getCo(click_position):
    global click_path
    click_path.append(str(click_position))
    return print("clickpath: " + str(click_path))


def draw_point(pos, cn):
    pygame.draw.circle(window, BLACK, pos, 20)
    pygame.display.update()
    txt = font.render(str(cn), False, WHITE)
    window.blit(txt, pos)
    return 0

def draw_arrow():
    pygame.draw.line(window, (255, 0, 0), prev_pos, pos)
    return 0 

is_running = True
window.blit(background, (0, 0))
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("yesss")
                c_count = 0
                current_no +=1

    
 
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        getCo(pos)
        draw_point(pos, current_no)
        if c_count >= 1:
            draw_arrow()
        prev_pos = pos
        c_count +=1
        time.sleep(1)


    #window.blit(background, (0, 0))
    pygame.display.update()


