import pygame

pygame.init()

game_window = pygame.display.set_mode((500, 400))

while True:
    
    pygame.draw.rect(game_window, (255, 0, 0), (0, 0, 50, 30))
    
    pygame.display.update()
