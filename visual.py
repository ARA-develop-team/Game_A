import pygame

# здесь определяются константы, классы и функции
FPS = 60

# здесь происходит инициация, создание объектов и др.
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

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