import pygame
from screen import Button
def shop1():
    pygame.init()
    FPS = 60
    run = True
    screen_x=500
    screen_y=500
    possition=0
    my_fond = pygame.font.SysFont('monospace', 20)
    st=pygame.image.load('right.png')
    st1= pygame.image.load('left.png')
    stand = pygame.image.load('ship3.png')
    stand2 = pygame.image.load('ship2.jpg')
    stand5 = pygame.image.load('pou.png')
    stand3 = pygame.transform.scale(stand2, (250, 250))
    stand4 = pygame.transform.scale(stand, (250, 250))
    right = pygame.transform.scale(st, (50, 50))
    left = pygame.transform.scale(st1, (50, 50))
    right.set_colorkey((255, 255, 255))
    left.set_colorkey((255, 255, 255))
    sc=pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()
    butt=[]
    ship=[stand4,stand3,stand5]
    def butt_pos(screen_x,screen_y,butt):
        extra = 10
        text=['Buy','','']
        color=(0, 128, 0)
        for i in range(3):
            if i==2:
                ex=-1
            else:
                ex=i
            widht=50
            height=50
            if i==0:
                widht = 150
            x=(screen_x/2)-(widht/2)+(extra+widht+widht)*ex
            y=screen_y-(screen_y/5)-height
            butt.append(Button(x,y,widht,height,text[i],color,i))
        x=screen_x/20
        y=screen_y/20
        widht=180
        height=250
        butt.append(Button(x, y, widht, height, text[1], color, len(butt)))
        widht=250
        height=250
        x=screen_x-(screen_x/20+widht)
        y=screen_y/20
        butt.append(Button(x, y, widht, height, text[1], color, len(butt)))
    def click(move,ship,p):
        if move>0:
            p += 1
            if p>(len(ship)-1):
                p=0
        elif move<0:
            p-=1
            if p<0:
                p=(len(ship)-1)
        return p







    pygame.display.update()
    butt_pos(screen_x,screen_y,butt)

    while run:
        sc.fill((169, 169, 169))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run=False
            if i.type == pygame.MOUSEBUTTONUP:
                if i.button == 1:
                    x3 = i.pos[0]
                    y3 = i.pos[1]
                    for button in butt:
                        if button.press(x3,y3):
                            if button.index==1:
                                move=1
                                possition=click(move,ship,possition)
                            if button.index==2:
                                move = -1
                                possition = click(move, ship, possition)
        for button in butt:
            if button.index!=1 and button.index!=2:
                button.draw1(sc,my_fond)
            if button.index==1:
                sc.blit(right,[button.x,button.y])
            elif button.index==2:
                sc.blit(left,[button.x,button.y])
            elif button.index==4:
                sc.blit(ship[possition],[button.x,button.y])



        clock.tick(FPS)
        pygame.display.update()

#shop()