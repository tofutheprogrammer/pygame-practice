import pygame

pygame.init()

game_window = pygame.display.set_mode((500, 400))

while True:
    
    pygame.draw.rect(game_window, (255, 0, 0), (100, 100, 50, 50))
    
    pygame.draw.rect(game_window, (0, 255, 0), (150, 100, 50, 50))
    
    pygame.draw.rect(game_window, (0, 0, 255), (200, 100, 50, 50))
    
    pygame.draw.circle(game_window, (0, 255, 255), (250, 200), 20,10)
    
    pygame.display.update()
