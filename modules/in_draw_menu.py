import pygame

def in_draw_menu(window, open_input, WHITE, font):

    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(30, 30, 100, 60))
    txt = font.render("back", False, WHITE)
    window.blit(txt, (30, 30))

    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(670, 30, 100, 60))
    txt = font.render("Draw", False, WHITE)
    window.blit(txt, (670, 30))


    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(300, 30, 200, 60))
    txt = font.render(str(open_input), False, WHITE)
    window.blit(txt, (300, 30))