import pygame
import random

pygame.init()

sc = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Game')
#dog_surf = pygame.image.load('dog.bmp')
#dog_surf.set_colorkey((255, 255, 255))
x=230
y=370
widht=20
height=20
speed=5
FPS=60
x4=1
y4=1
stand=pygame.image.load('ship3.png')
#bg = pygame.image.load('bg1.jpg')

left=False
right=True
mo=False
# здесь будут рисоваться фигуры
#pygame.draw.rect(sc,(255, 255, 255),(x,y,widht,height))
class Ship:
    def __init__(self,x,y,widht,height,speed):
        self.x=x
        self.y=y
        self.widht=widht
        self.height=height
        self.speed=speed
    def ship1(self):
        #pygame.draw.rect(sc, (0, 0, 139), (self.x, self.y, self.widht, self.height))
        sc.blit(stand,[self.x,self.y])

    def dvig(self,keys,x4,y4):
        if keys[pygame.K_LEFT]:
            if self.x>=0:
                self.x=(self.x-self.speed)
                x4=self.x
                return x4
        elif keys[pygame.K_RIGHT]:
            if self.x<=380:
                self.x=(self.x+self.speed)
                x4 = self.x
                return x4
        elif keys[pygame.K_UP]:
            if self.y>=0:
                self.y=(self.y-self.speed)
                y4=self.y
                return y4
        elif keys[pygame.K_DOWN]:
            if self.y<=370:
                self.y=(self.y+self.speed)
                y4 = self.y
                return y4
        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            if self.y>=0 and self.x>=0:
                self.y=(self.y-self.speed)
                self.x = (self.x - self.speed)
                y4 = self.y
                x4 = self.x
                return x4,y4
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            if self.y>=0 and self.x<=370:
                self.y=(self.y-self.speed)
                self.x = (self.x + self.speed)
                x4 = self.x
                y4 = self.y
                return x4,y4

x1=230
y1=370
height1=20
widht1=20
speed1=1
run=True
color=(255, 255, 255)
stars=[]
bulle=[]
r=4
y5=1
x5=1
x2=random.randint(0,500)
y2=random.randint(0,500)


class Star:
    def __init__(self,color,r):
        self.color=color
        self.r=r
    def star1(self,x2,y2):
        pygame.draw.circle(sc,self.color,(x2,y2),self.r)






#def draw():
    #sc.blit(bg, (0,0))
   # pygame.display.update()

class Bullet:
    def __init__(self,x1,y1,height1,widht1,speed1):
        self.x1=x1
        self.y1=y1
        self.height1=height1
        self.widht1=widht1
        self.speed1=speed1
        self.fps1=25
    def snar(self):
        pygame.draw.rect(sc,(139, 0, 0),(self.x1,self.y1, self.widht1, self.height1))
    def polet(self):
        self.y1=(self.y1-self.speed1)
    #def check(self):



#bull=Bullet(x1,y1,height1,widht1,speed1)
ship2=Ship(x,y,widht,height,speed)
#ship2.ship1()
pygame.display.update()

while 1:
    sc.fill((0, 0, 0))
    #pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    #bull.snar()
    #ship2.ship1()
    #draw()
    keys = pygame.key.get_pressed()
    ship2.ship1()
    ship2.dvig(keys, x4, y4)
    x5=x4
    y5=y4
    if keys[pygame.K_SPACE]:
        bulle.append(Bullet(x5,y5,height1,widht1,speed1))
    if len(bulle)>0:
        for i in bulle:
            i.snar()
            i.polet()
            if i.y1<=0:
                del bulle[0]
    #ship2.ship1()
    #keys,x4,y4=ship2.dvig(keys,x4,y4)
    #bull.polet(keys,run)
    #draw()
    pygame.display.update()
    #draw()
    clock.tick(FPS)
    ##draw()
    #pygame.display.update()


