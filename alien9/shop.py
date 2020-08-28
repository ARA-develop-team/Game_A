import pygame
from screen import Button
def shop1(money):
    pygame.init()
    FPS = 60
    run = True
    screen_x=500
    screen_y=500
    possition=0
    #price=100
    my_fond = pygame.font.SysFont('monospace', 20)
    st=pygame.image.load('right.png')
    st1= pygame.image.load('left.png')
    stand = pygame.image.load('ship3.png')
    stand2 = pygame.image.load('ship2.jpg')
    stand5 = pygame.image.load('pou.png')

    def info():
        done=False
        c=0
        price_list=[]
        st=''
        price_file = open('price.txt', 'r')
        price_text = price_file.read()
        while not done:
            for letter in price_text[c]:
                c+=1
                if letter==',':
                    price_list.append(int(st))
                    st=''
                    letter=''
                if c==len(price_text):
                    #done=True
                    return price_list
            st+=letter
            #print(st)
    price_list=info()
    #for i in price_list:
        #print(i)
        #price_list[i]=int(price_list[i])
    #mo = pygame.image.load('moneta1.png')
    #im = pygame.transform.scale(mo, (20, 20))
    stand6 = pygame.transform.scale(stand5, (250, 250))
    stand3 = pygame.transform.scale(stand2, (250, 250))
    stand4 = pygame.transform.scale(stand, (250, 250))
    right = pygame.transform.scale(st, (50, 50))
    left = pygame.transform.scale(st1, (50, 50))
    right.set_colorkey((255, 255, 255))
    left.set_colorkey((255, 255, 255))
    sc=pygame.display.set_mode((screen_x, screen_y))
    clock = pygame.time.Clock()
    #price_list=[0,100,200]
    butt=[]
    ship=[stand4,stand3,stand6]
    def butt_pos(screen_x,screen_y,butt,money):
        extra = 10
        text=['','','',str(money)]
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
        butt.append(Button(x, y, widht, height, text[3], color, len(butt)))
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






    def money_ckeck(money,price):
        if money>=price:
            return True
        else:
            return False

    pygame.display.update()
    butt_pos(screen_x,screen_y,butt,money)

    while run:
        sc.fill((169, 169, 169))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                #run=False
                price_file = open('price.txt', 'w')
                for price in price_list:
                    price_file.write(str(price)+',')
                price_file.close()
                return money
            if i.type == pygame.MOUSEMOTION:
                x3 = i.pos[0]
                y3 = i.pos[1]
                for button in butt:
                    button.color = (0, 128, 0)
                    if button.press(x3, y3):
                        if button.index==0:
                            ckeck = money_ckeck(money, price_list[possition])
                            if not ckeck:
                                button.color=(255,0,0)
            if i.type == pygame.MOUSEBUTTONUP:
                if i.button == 1:
                    x3 = i.pos[0]
                    y3 = i.pos[1]
                    for button in butt:
                        if button.press(x3,y3):
                            if button.index==0:
                                ckeck=money_ckeck(money,price_list[possition])
                                if ckeck:
                                    money-=price_list[possition]
                                    price_list[possition]=0
                                else:
                                    print('no money')
                            if button.index==1:
                                move=1
                                possition=click(move,ship,possition,)
                            if button.index==2:
                                move = -1
                                possition = click(move, ship, possition,)
        for button in butt:
            if button.index!=1 and button.index!=2:
                button.draw1(sc,my_fond)
            if button.index==0:
                if price_list[possition]==0:
                    button.text = 'select'
                else:
                    button.text=str(price_list[possition])
            elif button.index==1:
                sc.blit(right,[button.x,button.y])
            elif button.index==2:
                sc.blit(left,[button.x,button.y])
            elif button.index == 3:
                button.text = str(money)
            elif button.index==4:
                sc.blit(ship[possition],[button.x,button.y])


        clock.tick(FPS)
        pygame.display.update()

#shop()