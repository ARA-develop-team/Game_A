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
        surface.blit(self.list_img[self.number_current_img], (self.x, self.y))

    def collision_click(self, pos):
        if self.x < pos[0] < self.x + self.wight and self.y < pos[1] < self.y + self.wight:
            return True

    def set_random_img(self):
        self.number_current_img = random.randint(0, 5)
        return self.number_current_img + 1

    def set_img(self, number):
        self.number_current_img = number

# здесь происходит инициация, создание объектов и др.
screen_x = 800
screen_y = 800
pygame.init()
screen=pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
green = 0, 100, 0
my_font = pygame.font.SysFont('Agency FB', 100)

# если надо до цикла отобразить объекты на экране
pygame.display.update()



def boardVisual(board):
    for i in board:
        pygame.draw.rect(screen, (211, 211, 211), (i.x, i.y, i.width, i.width))


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


#
# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             exit()
#         if i.type == pygame.MOUSEBUTTONUP:
#             if i.button == 1:
#                 cube.dice_roll(i.pos)
#     screen.fill(green)
#     cube.draw(screen)
#     pygame.display.update()

