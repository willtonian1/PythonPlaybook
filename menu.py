import rugby as game
import pygame
import time

#variables declaration
BLACK =     (0, 0, 0)
WHITE = (255,255,255)
c_count = 0 
current_no =10
prev_pos = (0,0)
click_path = []

pygame.init()
pygame.display.set_caption('Rugby Moves Menu')
window = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ffffff'))
window.blit(background, (0, 0))

#font
font = pygame.font.Font('freesansbold.ttf', 32)

if __name__ == "__main__":
	is_menu = True
	while is_menu:
		txt = font.render("Welcome to Menu", False, BLACK)
		window.blit(txt, (100,100))

		a = input("game: ")
		if a == '1':
			game.setup()
			game.start()
			
		pygame.display.update() 
	