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
run3=True
stand=pygame.image.load('ship3.png')
im=pygame.image.load('blue2.png')
im_new=pygame.transform.scale(im, (80, 120))
im_new.set_colorkey((255, 255, 255))
#bg = pygame.image.load('bg1.jpg')

left=False
right=True
mo=False
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

    def dvig(self,keys):
        if keys[pygame.K_LEFT]:
            if self.x>=0:
                self.x=(self.x-self.speed)
        if keys[pygame.K_RIGHT]:
            if self.x<=380:
                self.x=(self.x+self.speed)
        if keys[pygame.K_UP]:
            if self.y>=0:
                self.y=(self.y-self.speed)
        if keys[pygame.K_DOWN]:
            if self.y<=370:
                self.y=(self.y+self.speed)
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            if self.y>=0 and self.x>=0:
                self.y=(self.y-self.speed)
                self.x = (self.x - self.speed)
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            if self.y>=0 and self.x<=370:
                self.y=(self.y-self.speed)
                self.x = (self.x + self.speed)

    def proverka(self,x,y):
        if (self.x - 10 < x < self.x + 128 + 10) and ((self.y-10) < y < self.y + 128 + 10):
            return False
        elif (self.x - 10 <x +20 < self.x + 128 + 10) and ((self.y-10) <y+20< self.y +128 +10):
            return False
        else:
            return True

x1=230
y1=370
height1=40
widht1=5
speed1=4
run=True
color=(169, 169, 169)
stars=[]
bulle=[]
r=1

class Star:
    def __init__(self,color,r):
        self.color=color
        self.r=r
        self.x=random.randint(-20,520)
        self.y=random.randint(0,500)
        self.speed3=3
        self.speed4=5
        self.speed5=1
    def star1(self):
        pygame.draw.circle(sc,self.color,(self.x,self.y),self.r)
    def dvig2(self,keys):
        self.y += self.speed3
        if self.y>500:
            self.y=0
        if keys[pygame.K_UP]:
            self.y += self.speed4
        elif keys[pygame.K_DOWN]:
            self.y -=self.speed5
        elif keys[pygame.K_LEFT]:
            self.x+=self.speed3
            if self.x>1000:
                self.x=500
            if self.x > 520:
                self.x = -20
        elif keys[pygame.K_RIGHT]:
            self.x-=self.speed3
            if self.x<-1000:
                self.x=0
            if self.x<-20:
                self.x=520

color0=(255,255,255)
widht5=40
height5=40
angry=[]
color_green=(0, 255, 0)
color_red=(255, 0, 0)
new_bullet=[]



class AngryAlien:
    def __init__(self,color0,widht5,height5):
        self.x6=random.randint(50,460)
        self.y6=random.randint(-300,-100)
        self.color0=color0
        self.widht5=widht5
        self.height5=height5
        self.speed8=1
        self.angry_bullet=[]
        self.speed9=1
    def spawn(self):
        #pygame.draw.rect(sc, self.color0, (self.x6, self.y6, self.widht5, self.height5))
        sc.blit(im_new,[self.x6,self.y6])
    def dwig3(self,angry):
        self.y6+=self.speed9
        if self.x6==50:
            self.speed8=1
        elif self.x6==450:
            self.speed8=-1
        self.x6 += self.speed8
        if self.y6>620:
            del angry[0]
    #def proverka2(self,x7,y7):



#po=AngryAlien(color0,widht5,height5)
#def draw():
    #sc.blit(bg, (0,0))
    #pygame.display.update()

class Bullet:
    def __init__(self,x1,y1,height1,widht1,speed1,color):
        self.x1=x1
        self.y1=y1
        self.height1=height1
        self.widht1=widht1
        self.speed1=speed1
        self.fps1=25
        self.color=color
    def snar(self):
        pygame.draw.rect(sc,self.color,(self.x1,self.y1, self.widht1, self.height1))
    def polet(self):
        self.y1=(self.y1-self.speed1)
    def polet2(self):
        self.y1+=self.speed1

def dobavka(angry):
    if len(angry)<5:
        #for al in range(5):
        angry.append(AngryAlien(color0,widht5,height5))

def vistrel(korabel,height1, widht1, speed1, color_red):
    lo=True
    if len(korabel.angry_bullet)>0:
        for po in korabel.angry_bullet:
            if po.y1<korabel.y6+250:
                lo=False
                break
        if lo:
            korabel.angry_bullet.append(Bullet(korabel.x6 + 40, korabel.y6 + 40, height1, widht1, speed1, color_red))

    else:
        korabel.angry_bullet.append(Bullet(korabel.x6+40, korabel.y6+40, height1, widht1, speed1, color_red))


#bull=Bullet(x1,y1,height1,widht1,speed1)
ship2=Ship(x,y,widht,height,speed)
#ship2.ship1()
pygame.display.update()
#for al in range(2):
    #angry.append(AngryAlien(color0, widht5, height5))
for st in range(200):
    stars.append(Star(color,r))
while run3:
    #draw()
    neo = True
    keys = pygame.key.get_pressed()
    sc.fill((0, 0, 0))
    for star in stars:
        star.dvig2(keys)
        star.star1()
    #pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    #bull.snar()
    #ship2.ship1()
    #draw()
    #keys = pygame.key.get_pressed()
    #ship2.ship1()
    ship2.dvig(keys)
    x5=ship2.x+60
    y5=ship2.y+60
    da=True
    if keys[pygame.K_SPACE]:
        for pro in bulle:
            da=ship2.proverka(pro.x1,pro.y1)
            if da==False:
                break
        if da:
            bulle.append(Bullet(x5,y5,height1,widht1,speed1,color_green))

    #for al in range(2):
        #angry.append(AngryAlien(color0,widht5,height5))
    if len(angry)>0:
        for a in angry:
            a.dwig3(angry)
            if a.y6>0:
                vistrel(a,height1, widht1, speed1, color_red)
            if len(a.angry_bullet)>0:
                for bu in a.angry_bullet:
                    bu.snar()
                    bu.polet2()
            a.spawn()
            if a.y6<=0:
                neo=False
    if neo==True:
        dobavka(angry)
    if len(bulle)>0 and len(angry)>0:
        for b in bulle:
            for a1 in angry:
                if(a1.x6 + 5 < b.x1 < a1.x6 + 75) and (a1.y6 < b.y1 < a1.y6 + 115) or (a1.x6 + 5 < b.x1 + 5 < a1.x6 + 75) and (a1.y6 < b.y1 + 40 < a1.y6 + 115):
                    #print('popal')
                    bulle.remove(b)
                    if len(a1.angry_bullet)>0:
                        for q2 in a1.angry_bullet:
                            new_bullet.append(q2)
                        angry.remove(a1)
                    else:
                        angry.remove(a1)
    if len(new_bullet)>0:
        for q3 in new_bullet:
            if (ship2.x + 15 < q3.x1 < ship2.x + 115) and (ship2.y + 30 < q3.y1 < ship2.y + 115) or (ship2.x + 15 < q3.x1 + 5 < ship2.x + 115) and (ship2.y + 30 < q3.y1 + 40 < ship2.y + 115):
                run3=False
                break
    if len(angry)>0:
        for q4 in angry:
            if len(q4.angry_bullet)>0:
                for q3 in q4.angry_bullet:
                    if (ship2.x + 15 < q3.x1 < ship2.x + 115) and (ship2.y + 30 < q3.y1 < ship2.y + 115) or (ship2.x + 15 < q3.x1 + 5 < ship2.x + 115) and (ship2.y + 30 < q3.y1 + 40 < ship2.y + 115):
                        run3 = False
                        break
    if len(angry)>0:
        for q3 in angry:
            if (ship2.x + 5 < q3.x6 + 5 < ship2.x + 123) and (ship2.y + 30 < q3.y6 < ship2.y + 115) or (ship2.x + 5 < q3.x6 + 75 < ship2.x + 123) and (ship2.y + 30 < q3.y6 + 40 < ship2.y + 115):
                run3 = False
                break
    if len(new_bullet)>0:
        for q in new_bullet:
            q.snar()
            q.polet2()
            if q.y1>500:
                new_bullet.remove(q)
    if len(bulle)>0:
        for i in bulle:
            i.snar()
            i.polet()
            if i.y1<=0:
                del bulle[0]
    ship2.ship1()
    #keys,x4,y4=ship2.dvig(keys,x4,y4)
    #bull.polet(keys,run)
    #draw()
    pygame.display.update()
    #draw()
    clock.tick(FPS)
    #draw()
    #pygame.display.update()


