import pygame

# здесь определяются константы, классы и функции
FPS = 60

# здесь происходит инициация, создание объектов и др.
screen_x = 800
screen_y = 800
pygame.init()
screen=pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

def boardVisual():
    for i in :
        pygame.draw.rect(screen, (211, 211, 211), (x, y, widht, height))


    # цикл обработки событий

    # --------
    # изменение объектов и многое др.
    # --------
    clock.tick(FPS)
    # обновление экрана
    pygame.display.update()