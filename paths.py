import pygame

pygame.init()

game_window = pygame.display.set_mode((500, 400))

while True:
    
    pygame.draw.lines(game_window, (255, 255, 255), True, ((50, 50), (75, 75), (25, 75)), 1)
    
    pygame.display.update()
