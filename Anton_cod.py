import random
import pygame
from visual import boardVisual
from visual import Cube
from visual import screen

class CPlayer:
    """for creating players"""

    def __init__(self, name, npp, startPosition):
        self.name = name
        self.startPosition = startPosition
        self.npp = npp
        self.home = [True, True, True]  # True = Free
        self.havePlace = True
        self.counter = 0
        self.winner = False

    def step(self, board, cube, player):
        if not self.winner:
            findActive(board, self, cube)
            j = int(self.allActive(board, cube))
            if j != -1:
                if j >= 100:
                    self.moveInHome(cube, j - 100)
                elif 100 > j + cube > 27:
                    newI = j + cube - 28
                    self.move(j, newI, board, player)
                else:
                    self.move(j, j + cube, board, player)
                if (j + cube == self.startPosition) or (j + cube - 28 == self.startPosition) and self.isHomeFull():
                    self.winner = True
            else:
                print("нет возможных ходов")

    def moveInHome(self, PCube, index):
        if PCube == 1:
            self.home[index] = True
            self.home[index + 1] = False
            print("шашку переместили из домика", index, "в домик", index + 1)
        elif PCube == 2:
            self.home[index] = True
            self.home[index + 2] = False
            print("шашку переместили из домика", index, "в домик", index + 2)

    def move(self, startI, finishI, desk, PPlayers):
        if self.startPosition == 0 and startI > finishI != 0:
            self.moveToHome(finishI)
            print("шашку переместили с ", startI, " в домик №", finishI - 1 - self.startPosition)
        elif self.startPosition == startI and not desk[startI].newBorn:
            newI = finishI - self.startPosition
            self.moveToHome(newI)
            print("шашку переместили с ", startI, " в домик №", finishI - 1 - self.startPosition)
        elif startI < self.startPosition < finishI:
            newI = finishI - self.startPosition
            self.moveToHome(newI)
            print("шашку переместили с ", startI, " в домик №", finishI - 1 - self.startPosition)
        else:
            desk[finishI].occupy(self.startPosition, PPlayers)
            print("шашку переместили с ", startI, " в ", finishI)
        desk[startI].setFree()

    def moveToHome(self, newI):
        i = newI - 1
        self.home[i] = False
        print("домик №", i, "занят")

    def getChecker(self):
        self.counter += 1
        # board[self.startPosition].invader = self.startPosition
        print("object was created. клетка № ", self.startPosition)
        print(self.counter, " шашек у игрока")

    def deleteChecker(self):
        self.counter -= 1
        print("object was delete. Player № ", self.startPosition)
        print(self.counter, "шашек у игрока")

    def goHome(self, cube, i):
        if cube < 4:
            if cube == 1 and not self.home[0]:
                i.active = False
            elif cube == 2:
                if not self.home[0] or not self.home[1]:
                    i.active = False

            elif cube == 3:
                if not self.home[0] or not self.home[1] or not self.home[2]:
                    i.active = False

        else:
            i.active = False
        print(i.active)

    def isHomeFull(self):
        if not self.home[0] and not self.home[1] and not self.home[2]:
            return True
        else:
            return False

    def allActive(self, desk, cube):
        allActiveCheckers = []
        homeStep = False
        if cube < 3:
            i = -1
            for field in self.home:
                i += 1
                if i != 2 and not field:
                    print("для i =", i, "i+1 =", self.home[i + 1])
                    if cube == 1 and self.home[i + 1]:
                        indexStep = i
                        homeStep = True
                    if cube == 2 and i == 0 and self.home[1] and self.home[2]:
                        homeStep = True
                        indexStep = i

        for field in desk:
            if field.invader == self.startPosition and field.active:
                allActiveCheckers.append(desk.index(field))
        if len(allActiveCheckers) != 0 or homeStep:
            print("выберите шашку:")
            for i in allActiveCheckers:
                print(i)
            if homeStep:
                print(indexStep, "*Home, print 100 + index to chose home")
            choice = False
            while not choice:
                ans = int(input())
                newAns = ans - 100
                if homeStep and indexStep == newAns:
                    choice = True
                for answer in allActiveCheckers:
                    if ans == answer:
                        choice = True
                        break
        else:
            ans = -1  # нет возможних ходов
        return ans


class square:
    """for playSpace"""

    def __init__(self, x, y, width):
        self.free = True
        self.invader = 100
        self.newBorn = False
        self.active = False
        self.x = x
        self.y = y
        self.width = width

    def occupy(self, PInvader, PPlayers):
        if self.free:
            self.free = False
            self.invader = PInvader
            print('клетка занята игроком', PInvader)
        elif self.invader != PInvader:
            p = 0
            while PPlayers[p].startPosition != self.invader:
                p += 1
            PPlayers[p].deleteChecker()  # удалить шашку противника
            self.invader = PInvader
            self.free = False
            print('клетка занята игроком', PInvader)

    def setFree(self):
        self.free = True
        self.invader = 100
        self.newBorn = False

    def freeWay(self, desk, startWay, finishWay, owner):
        p = startWay + 1
        f = finishWay - 1
        isFree = True
        while p <= f and isFree:
            isFree = desk[p].free
            p += 1
        if not isFree:
            self.active = False
        if finishWay < 28 and desk[finishWay].invader == owner.startPosition:
            self.active = False


def findActive(desk, PPlayer, PCube):
    for field in desk:
        if field.invader == PPlayer.startPosition:
            field.active = True  # для того, что бы отсеять те, которые False
            i = desk.index(field)
            if PPlayer.startPosition == i and not field.newBorn:  # вариант №1 (шашка в своем углу. заход в домик)
                PPlayer.goHome(PCube, field)
            elif i + PCube > 27:  # вариант №2 (переход через поле 0)
                newI = i + PCube - 28
                if PPlayer.startPosition == 0:  # игрок у которого 0 - домик.
                    PPlayer.goHome(newI, field)
                    field.freeWay(desk, i, 28, PPlayer)
                    if not desk[0].free:
                        field.active = False
                elif PPlayer.startPosition != 0:
                    field.freeWay(desk, i, 28, PPlayer)  # проверяет клетки от i+1 до 27 и от 0 до newI.
                    field.freeWay(desk, -1, newI, PPlayer)  # и от 0 до newI.
            elif i < PPlayer.startPosition < i + PCube:  # игрок подходит к своему углу (не игрок(0))
                field.freeWay(desk, i, PPlayer.startPosition, PPlayer)
                newI = i + PCube - PPlayer.startPosition
                PPlayer.goHome(newI, field)
            else:
                field.freeWay(desk, i, i + PCube, PPlayer)


num = 1
player = []
board = []
startPoint = [0, 7, 14, 21]
screen_x = 800
screen_y = 800
width = 70
empty = 10
createPlayers = True
game = True
x = (screen_x / 2) - width -(4 * width + 3 * empty - empty // 2)
y= (screen_y / 2) - (4 * width + 3 * empty - empty // 2)

"""game start"""
print('game start')

for c in range(0, 8):
    x = x + (width + empty)
    board.append(square(x, y, width))
for c in range(0, 7):
    y = y + (width + empty)
    board.append(square(x, y, width))
for c in range(0, 7):
    x = x - (width + empty)
    board.append(square(x, y, width))
for c in range(0, 7):
    y = y - (width + empty)
    board.append(square(x, y, width))


while createPlayers:
    if num == 0:
        break
    print('How much players?')

    num = int(input())

    if num == 1:
        pass
    elif 2 <= num <= 4:
        for x in range(0, num):
            print("write your name")
            name = input()
            startPosition = startPoint[x]
            player.append(CPlayer(name, x, startPosition))
        createPlayers = False
    else:
        print("choose from 1 to 4")
        continue

# while game:
#     """checking possible turns"""
#
#     for one in player:
#         for i in pygame.event.get():
#             if i.type == pygame.QUIT:
#                 exit()
#         boardVisual(board)
#         print("***")
#         print(one.name, " стартовая позиция ", "(", one.startPosition, ")")
#         cube = random.randint(1, 6)
#         print("кубик:", cube)
#         while cube == 6:
#             if one.counter < 4 and board[one.startPosition].invader != one.startPosition:
#                 print("do you want to get new checker? _Y/N")
#                 ans = input()
#                 if ans == 'Y':
#                     one.getChecker()
#                     board[one.startPosition].occupy(one.startPosition, player)
#                     board[one.startPosition].newBorn = True
#                     # board[one.startPosition].active = True   удалить в рабочей версии
#
#                 else:
#                     # поиск всех клеток которие могут ходить
#                     one.step(board, cube, player)
#             else:
#                 # поиск всех клеток которие могут ходить
#                 one.step(board, cube, player)
#             if one.winner:
#                 break
#             else:
#                 cube = random.randint(1, 6)
#                 print("кубик:", cube)
#         one.step(board, cube, player)
#         # проверка домика игрока
#         if one.winner:
#             print(one.name, "you win!!!")
#             game = False
#             break

list_img = ['gran1.png', 'gran2.png', 'gran3.png', 'gran4.png', 'gran5.png', 'gran6.png', 'click_her.png']
list_load_img = []
for img in list_img:
    list_load_img.append(pygame.image.load(img))

v_cube = Cube(300, 300, 114, list_load_img)
while game:
    for one in player:
        cube = 6
        v_cube.set_img(6)
        while cube == 6:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONUP:
                    if i.button == 1:
                        if v_cube.collision_click(i.pos):
                            cube = v_cube.set_random_img()
            v_cube.draw(screen)
            boardVisual(board)


