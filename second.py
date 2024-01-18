import pygame
pygame.init()
gameWindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("my game")

exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("CLICKED RIGHT")


pygame.quit()
quit()