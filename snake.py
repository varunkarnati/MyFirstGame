import pygame
import random
import os

pygame.init()





white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,25)

swidth=1000
sheight=700
clock = pygame.time.Clock()



gameWindow=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("Hungry Snake")
pygame.display.update()





#game variables




font=pygame.font.SysFont(None,50)
def screen_text(text,color,x,y):
    text_screen=font.render(text,True,color)
    gameWindow.blit(text_screen,[x,y])
def plot_snake(gameWindow,color,s_list,snake_size):
    for x,y in s_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size ])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((12,75,94))
        screen_text("Wecome to HUNGRY SNAKES", green, 230, 280)
        screen_text("Press Space Bar to Play",green,285,320)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:

                    game_loop()
        pygame.display.update()









#game loop
def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 18
    s_list = []
    fps = 30
    velocityx = 0
    velocityy = 0
    food_x = random.randint(20, swidth / 2)
    food_y = random.randint(20, sheight / 2)
    food_size = 16
    score = 0
    init_velocity=10

    s_length = 1

    while not exit_game :
        if (not os.path.exists("highscore.txt")):
            with open("highscore.txt", "w") as f:
                f.write("0")
        with open("highscore.txt","r") as f:
            highscore=f.read()
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
            gameWindow.fill((46,42,87))
            screen_text("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocityx=init_velocity
                        velocityy=0
                    if event.key==pygame.K_LEFT:
                        velocityx=-10
                        velocityy=0
                    if event.key==pygame.K_UP:
                        velocityy=-10
                        velocityx=0
                    if event.key==pygame.K_DOWN:
                        velocityy=10
                        velocityx = 0
            snake_x+=velocityx
            snake_y+=velocityy
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10

                s_length+=5

                food_x = random.randint(20, swidth / 2)
                food_y = random.randint(20, sheight / 2)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            gameWindow.fill((62,27,124))
            screen_text(("Score:" + str(score )), red, 5, 5)
            if(score<=int(highscore)):
                screen_text(("High Score:" + str(highscore )), red, 155, 5)
            else:
                screen_text(("High Score:" + str(score)), red, 155, 5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            s_list.append(head)

            if len(s_list)>s_length:
                del s_list[0]
            if head in s_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>=swidth or snake_y<0 or snake_y>=sheight:
                game_over=True


            plot_snake(gameWindow,black,s_list,snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)











    #exit
    pygame.quit()
    quit()
welcome()


x=input()
