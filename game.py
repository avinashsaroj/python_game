import pygame,time,random
pygame.init()
white=(255,255,255)
black=(0,0,0)

clk=pygame.time.Clock()
gamewindow=pygame.display.set_mode((800,600))
pygame.display.set_caption('snake game')
pygame.display.update()

fon=pygame.font.SysFont(None,40)
def snake(block,snakelength):
    for xy in snakelength:
        pygame.draw.rect(gamewindow,black,[xy[0],xy[1],15,15])

def message(msg):
    text=fon.render(msg,True,(0,0,0))
    gamewindow.blit(text,[150,250])
def loop():
    close = False
    gameover=False
    apple_x=int(random.randrange(0,800-15))
    apple_y=int(random.randrange(0,600-15))
    x, y = 400, 300
    update_x = 0
    update_y = 0
    slist=[]
    slength=1
    while not close:
        while gameover==True:
            message("Game Over press 'r' to replay and 'q' to quit")
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

        if(x>=800 or x<0 or y>=600 or y<0):
            gameover=True
        x+=update_x
        y+=update_y
        gamewindow.fill(white)
        pygame.draw.rect(gamewindow, black, [apple_x, apple_y, 15, 15])
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        slist.append(snakehead)
        if len(slist) > slength:
            del (slist[0])
        for seg in slist[:-1]:
            if seg==snakehead:
                gameover=True

        snake(15,slist)
        pygame.display.update()
        if (x>=apple_x-15 and x<=apple_x+15) and (y>=apple_y-15 and y<=apple_y+15) :
            apple_x = int(random.randrange(0, 800 - 15))
            apple_y = int(random.randrange(0, 600 - 15))
            slength+=1

        clk.tick(10)


    time.sleep(0.1)
    pygame.quit()
    quit()

loop()
