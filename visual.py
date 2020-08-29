import pygame
import random

# здесь определяются константы, классы и функции
FPS = 60


class Cube:
    def __init__(self, x, y, wight, list_img, number_current_img=random.randint(0, 5)):
        self.x = x
        self.y = y
        self.wight = wight
        self.list_img = list_img
        self.number_current_img = number_current_img

    def draw(self, surface):
        pygame.draw.rect(window, (230, 230, 230), (self.x, self.y, self.wight, self.wight))
        surface.blit(self.list_img[self.number_current_img], self.x, self.y)

    def dice_roll(self):
        self.number_current_img = random.randint(0, 5)
        return self.number_current_img + 1


# здесь происходит инициация, создание объектов и др.
pygame.init()
window = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
green = 0, 100, 0
my_font = pygame.font.SysFont('Agency FB', 100)

# если надо до цикла отобразить объекты на экране
pygame.display.update()

# главный цикл
while True:

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    # --------
    # изменение объектов и многое др.
    # --------
    clock.tick(FPS)
    # обновление экрана
    pygame.display.update()