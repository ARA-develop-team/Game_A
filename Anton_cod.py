import random


def whoseTurn():
    while not win:
        player = 1
        if player == 1:
            turn()
            player += 1
        if player == 2:
            turn()
            player += 1
        if player3 and player == 3:
            turn()
            player += 1
        if player4 and player == 4:
            turn()
            player += 1
        

def turn():
    while True:
        cube = random.randint(0, 6)
        print(cube)
        if cube == 6:
            pass
        if cube != 6:
            pass
        if not cube == 6:
            break


class PlayObjects:
    """objects for playing"""

    def __init__(self, position, user):
        self.position = position
        self.user = user


num = 0
win = False

player3 = False
player4 = False

game = True
while game:
    print('tab')
    stop = input()
    if stop == 'q':
        break
    else:
        print('game start')
        print('How much players?')
        num = int(input())
        if num == 1:
            pass
        if 2 <= num <= 4:

            if num == 3:
                player3 = True
            if num == 4:
                player3 = True
                player4 = True
            print("name(1)")
            name1 = input()
            print("name(2)")
            name2 = input()
            if player3:
                print("name(3)")
                name3 = input()
            if player4:
                print("name(4)")
                name4 = input()





        else:
            print("choose from 1 to 4")  # don`t work correctly without cycle

    turn()
    game = False
