# здесь подключаются модули
import pygame
def logo1():
    # здесь определяются константы, классы и функции
    FPS = 60

    # здесь происходит инициация, создание объектов и др.
    pygame.init()
    sc=pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    im=pygame.image.load('ado.png')
    im_new=pygame.transform.scale(im, (500, 500))
    def draw():
        sc.fill((255, 255, 255))
        sc.blit(im_new, (0, 0))
        pygame.display.update()
    # если надо до цикла отобразить объекты на экране
    pygame.display.update()
    run=True
    # главный цикл
    while run:
        for i in range(400):
            a=i
            if a!=100:
                draw()
                #run=False
            else:
                run = False


        # цикл обработки событий
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        # --------
        # изменение объектов и многое др.
        # --------

        clock.tick(FPS)
        pygame.display.update()
logo1()