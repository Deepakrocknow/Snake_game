import pygame
import random
import os

pygame.mixer.init()
pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

bgimg = pygame.image.load("snake.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

bgi = pygame.image.load("gameover.jpg")
bgi = pygame.transform.scale(bgi,(screen_width,screen_height)).convert_alpha()

bgpop = pygame.image.load("intro.jpg")
bgpop = pygame.transform.scale(bgpop,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption("SnakeGame")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)



def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x,y, size, size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((135, 206, 235))
        gameWindow.blit(bgpop, (0, 0))
        text_screen("Welcome to Snake Game",white,200,250)
        text_screen("Press Space_bar To Play Snake Game",white,100,300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5

    size = 20
    fps = 60
    snake_list = []
    snake_length = 1
    if (not os.path.exists("highscore.txt")):
         with open("highscore.txt","w") as f:
             f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            gameWindow.blit(bgi, (0, 0))
            text_screen("Press Enter To Continue",red,250,400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x= -init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                          velocity_y = -init_velocity
                          velocity_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                         score+=10

            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length +=5
                if score> int(highscore):
                    highscore = score



            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,size,size])


            pygame.draw.rect(gameWindow, (0,255,0), [food_x, food_y, size, size])
            text_screen("score : " + str(score)+"                                         Highscore : "+str(highscore), red, 5, 5)
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del(snake_list[0])

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
                game_over = True
                pygame.mixer.music.load('gameover.mp3.mp3')
                pygame.mixer.music.play()
                # gameWindow.blit(bgimg, (0, 0))

            plot_snake(gameWindow, white, snake_list, size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
