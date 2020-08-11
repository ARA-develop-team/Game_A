import pygame
from screen import Button
def shop1():
    pygame.init()
    FPS = 60
    run = True
    screen_x=500
    screen_y=500
    my_fond = pygame.font.SysFont('monospace', 20)
    sc=pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()
    butt=[]
    def butt_pos(screen_x,screen_y,butt):
        extra = 10
        text=['Buy','','']
        color=(0, 128, 0)
        for i in range(3):
            if i==2:
                ex=-1
            else:
                ex=i
            widht=40
            height=40
            x=(screen_x/2)-(widht/2)+(extra+widht)*ex
            y=screen_y-(screen_y/5)-height
            butt.append(Button(x,y,widht,height,text[i],color,i))



    pygame.display.update()
    butt_pos(screen_x,screen_y,butt)

    while run:
        sc.fill((169, 169, 169))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run=False
        for button in butt:
            button.draw1(sc,my_fond)


        clock.tick(FPS)
        pygame.display.update()

#shop()