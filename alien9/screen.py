import pygame
from textwrap import fill
import time
import math
import random
def meny(sound,score,money,money_file):
    FPS = 60
    screen_x=500
    screen_y=500
    run=True
    color=(25, 25, 112)
    button_list=[]
    widht=150
    height=50
    bg=pygame.image.load('volum1.png')
    bg2=pygame.image.load('volum2.png')
    volum_on = pygame.transform.scale(bg, (40, 40))
    volum_off = pygame.transform.scale(bg2, (40, 40))
    if sound:
        music_play = True
        status_volum=volum_on
    else:
        music_play = False
        status_volum=volum_off

    def music(music):
        if music==True:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
    # my_fond=pygame.font.Font('Hello world',20)

    pygame.init()
    sc=pygame.display.set_mode((screen_x, screen_y))
    my_fond=pygame.font.SysFont('monospace',20)
    #bg=pygame.image.load('screen1.jpg')
    #im_new=pygame.transform.scale(bg, (screen_x, screen_y))
    clock = pygame.time.Clock()
    class Button:
        def __init__(self,x,y,widht,height,text,color,index):
            self.x=x
            self.y=y
            self.widht=widht
            self.height=height
            self.text=text
            self.color=color
            self.index=index
        def draw1(self,sc,my_fond):
            pygame.draw.rect(sc,self.color,(self.x,self.y,self.widht,self.height))
            string=my_fond.render(self.text,1,(255,255,255))
            sc.blit(string,(self.x,self.y))
        def press(self,px,py):
            if self.x<px<self.x+self.widht and self.y<py<self.y+self.height:
                return True
            else:
                return False
    #def draw():
        #sc.blit(im_new, (0,0))
        #pygame.display.update()
    def button_pos(screen_x,screen_y,widht,height,list,color,score):
        extra=10
        text=['Play','Shop']
        text1=[str(score),'']
        text2=[str(money)]
        for i in range(2):
            x=(screen_x/2)-(widht/2)
            y=(screen_y/2)+((height+extra)*i)
            list.append(Button(x,y,widht,height,text[i],color,len(list)))
        for i in range(2):
            widht=100
            height=40
            x=screen_x/20
            y=(screen_y/20)+((height+extra)*i)
            list.append(Button(x,y,widht+((height-widht)*i),height,text1[i],color,len(list)))
        widht = 100
        height = 40
        x=((screen_x/20)*19)-widht
        y=(screen_y/20)
        list.append(Button(x, y, widht, height, text2[0], color,len(list)))



    button_pos(screen_x,screen_y,widht,height,button_list,color,score)
    pygame.display.update()
    while run:
        sc.fill((105, 105, 105))
        #draw()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                money_file.write(str(money))
                money_file.close()
                exit()
            if i.type==pygame.MOUSEBUTTONUP:
                if i.button==1:
                    x3=i.pos[0]
                    y3=i.pos[1]
                    for t in button_list:
                        if t.press(x3,y3):
                            if t.index==0:#start
                                run=False
                                return music_play
                            if t.index==3:
                                if music_play==True:
                                    status_volum=volum_off
                                    music_play=False
                                    #print(music_play)
                                else:
                                    status_volum=volum_on
                                    music_play=True
                                    #print(music_play)
                                music(music_play)

        for button in button_list:
            button.draw1(sc,my_fond)
            if button.index==3:
                sc.blit(status_volum,[button.x,button.y])
        clock.tick(FPS)
        pygame.display.update()