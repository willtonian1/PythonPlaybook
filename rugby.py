import pygame
import time



def setup():
	#initiation
	pygame.init()

	#window setup
	pygame.display.set_caption('Rugby Moves')
	window = pygame.display.set_mode((800, 600))
	background = pygame.Surface((800, 600))
	background.fill(pygame.Color('#00ff00'))
	window.blit(background, (0, 0))
#font
	font = pygame.font.Font('freesansbold.ttf', 32)


#function section

def getCo(click_position):
		global click_path
		click_path.append(str(click_position))
	
		book = open("playbook.txt", 'a')
		book.write(str(click_position) + ',')
		book.close()
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


#main loop 
	


def start():
	is_running = True
	while is_running:
	    
	    #inputs
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            is_running = False
	        
	        #keys pressed
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_r:
	                print("yesss")
	                c_count = 0
	                current_no +=1
	
	    #mouse pressed
	    if event.type == pygame.MOUSEBUTTONUP:
	        pos = pygame.mouse.get_pos()
	        getCo(pos)   #taking mouse co-ordinates and saving them
	        draw_point(pos, current_no)  #circle drawing and number render
	        if c_count >= 1:  #checks if it is the first point (no arrow)
	            draw_arrow()  #connects previous and current point
	
					
	        prev_pos = pos
	        c_count +=1
	        time.sleep(1)
	
	
	    pygame.display.update() #update the window


