import pygame,time,random
pygame.init()
white=(255,255,255)
black=(0,0,0)
window_x=1500
window_y=700
clk=pygame.time.Clock()
gamewindow=pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption('snake game by Avinash')
pygame.display.update()
snake_x=15
snake_y=15
fon=pygame.font.SysFont(None,40)
def snake(block,snakelength):
    for xy in snakelength:
        pygame.draw.rect(gamewindow,black,[xy[0],xy[1],snake_x,snake_y])


def message(msg):
    text=fon.render(msg,True,(0,0,0))
    gamewindow.blit(text,[350,250])
def loop():
    close = False
    gameover=False
    apple_x=int(random.randrange(0,window_x-snake_x))
    apple_y=int(random.randrange(0,window_y-snake_y))
    x, y = window_x/2, window_y/2
    update_x = 0
    update_y = 0
    slist=[]
    slength=1
    while not close:
        while gameover==True:

            message("Game Over press 'r' to replay and 'q' to quit" )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close=True
                        gameover=False
                    if event.key == pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                  update_x=-25
                  update_y=0
               if event.key==pygame.K_RIGHT:
                  update_x=+25
                  update_y=0
               if event.key==pygame.K_UP:
                  update_y=-25
                  update_x=0
               if event.key==pygame.K_DOWN:
                  update_y=+25
                  update_x=0

        if(x>=window_x or x<0 or y>=window_y or y<0):
            gameover=True
        x+=update_x
        y+=update_y
        gamewindow.fill(white)
        pygame.draw.rect(gamewindow, black, [apple_x, apple_y, snake_x, snake_y])
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        slist.append(snakehead)
        if len(slist) > slength:
            del (slist[0])
        for seg in slist[:-1]:
            if seg==snakehead:
                gameover=True

        snake(10,slist)
        pygame.display.update()
        if (x>=apple_x-snake_x and x<=apple_x+snake_x) and (y>=apple_y-snake_y and y<=apple_y+snake_y) :
            apple_x = int(random.randrange(0, window_x - snake_x))
            apple_y = int(random.randrange(0, window_y - snake_y))
            slength=slength+1





        clk.tick(10)


    time.sleep(0.1)
    print(slength*3)

    pygame.quit()
    quit()

loop()
