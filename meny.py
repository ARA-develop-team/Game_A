import pygame

# здесь определяются константы, классы и функции
FPS = 60

# здесь происходит инициация, создание объектов и др.
pygame.init()
screen_x = 800
screen_y = 800
width=200
button=[]
height=80
sc=pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
class Button:
    def __init__(self,screen_x,screen_y,width,height):
        self.screen_x=screen_x
        self.screen_y=screen_y
        self.width=width
        self.height=height
    def draw(self):
        pygame.draw.rect(sc, (218, 165, 32), (self.screen_x, self.screen_y, self.width, self.height))
def but_pos():
    for i in range(4):
        extra=25
        x=(screen_x/2)-(width/2)
        y = (screen_y/2) - (height*2+extra*2-extra//2)+((height + extra) * i)
        button.append(Button(x,y,width,height))

# если надо до цикла отобразить объекты на экране
pygame.display.update()

# главный цикл
while True:
    sc.fill((128, 128, 128))
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    but_pos()
    for i in button:
        i.draw()
    # --------
    # изменение объектов и многое др.
    # --------
    # задержка
    clock.tick(FPS)
    # обновление экрана
    pygame.display.update()