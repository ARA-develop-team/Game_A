print('Игра Муха(Мини-Нарды) v1.0!')
print('Выбирите количество игроков 2-4')


def proVerka(kletka5):
    if kletka5 > 28:
        kletka5 -= 28
        return kletka5
    elif kletka5 < 28:
        kletka5 = kletka5
        return kletka5
    else:
        print('gtg')


def proVerka1(kletka):
    if kletka>28:
        figura11+=1
        return figura11
        del city_list1[0]
    elif kletka<28:
        figura11=figura11
        return figura11
    else:
        print('gtg')

def proVerka2(kletka2):
    if kletka2>28 and figura11==2:
        figura22+=1
        return figura22
        del city_list1[0]
    elif kletka2>28:
        figura22+=1
        return figura22
        del city_list1[1]
    elif kletka2<28:
        figura22=figura22
        return figura22
    else:
        print('gtg')

def proVerka3(kletka3):
    if kletka3>28 and figura11==2 and figura22==2:
        figura33+=1
        return figura33
        del city_list1[0]
    elif kletka3>28 and figura11==2 or figura22==2:
        figura33+=1
        return figura33
        del city_list1[1]
    elif kletka3>28:
        figura33+=1
        return figura33
        del city_list1[2]
    elif kletka3<28:
        figura33=figura33
        return figura33
    else:
        print('gtg')

def proVerka4(kletka4):
    if kletka4>28 and figura11==2 and figura22==2 and figura33==2:
        figura44+=1
        return figura44
        del city_list1[0]
    elif kletka4>28 and figura11==2 and figura22==2:
        figura44+=1
        return figura44
        del city_list1[1]
    elif kletka4>28 and figura11==2 or figura22==2 or figura33==2:
        figura44+=1
        return figura44
        del city_list1[2]
    elif kletka4>28:
        figura44+=1
        return figura44
        del city_list1[3]
    elif kletka4<28:
        figura44=figura44
        return figura44
    else:
        print('gtg')

'''def proVerka5(kletka5): Надо подумать!
    if kletka5>7:
        figura55+=1
        return figura55
        del city_list3[0]
    elif kletka5<7:
        figura55=figura55
        return figura55
    else:
        print('gtg')

def proVerka6(kletka6):
    if kletka6>7 and figura55==2:
        figura66+=1
        return figura66
        del city_list3[0]
    elif kletka6>7:
        figura66+=1
        return figura66
        del city_list3[1]
    elif kletka6<7:
        figura66=figura66
        return figura66
    else:
        print('gtg')

def proVerka7(kletka7):
    if kletka7>7 and figura55==2 and figura66==2:
        figura77+=1
        return figura77
        del city_list3[0]
    elif kletka7>7 and figura55==2 or figura66==2:
        figura77+=1
        return figura77
        del city_list3[1]
    elif kletka7>7:
        figura77+=1
        return figura77
        del city_list3[2]
    elif kletka7<7:
        figura77=figura77
        return figura77
    else:
        print('gtg')

def proVerka8(kletka8):
    if kletka8>28 and figura11==2 and figura22==2 and figura33==2:
        figura44+=1
        return figura44
        del city_list1[0]
    elif kletka4>28 and figura11==2 and figura22==2:
        figura44+=1
        return figura44
        del city_list1[1]
    elif kletka4>28 and figura11==2 or figura22==2 or figura33==2:
        figura44+=1
        return figura44
        del city_list1[2]
    elif kletka4>28:
        figura44+=1
        return figura44
        del city_list1[3]
    elif kletka4<28:
        figura44=figura44
        return figura44
    else:
        print('gtg')'''
end1 = 28
end2 = 7
# Game1
figura1 = 1
figura11 = 0
figura2 = 1
figura22 = 0
figura33 = 0
figura44 = 0
suma = 0
kletka = 0
kletka2 = 0
kletka3 = 0
kletka4 = 0
# Game2
figura5 = 8
figura55 = 0
figura6 = 8
figura66 = 0
figura77 = 0
figura88 = 0
suma2 = 0
kletka5 = 0
kletka6 = 0
kletka7 = 0
kletka8 = 0
game1 = True
game = True
game2 = True
game3 = True
vybor = int(input())
if vybor == 2:
    print('Ваше имя игрок 1?')
    name1 = str(input())
    print('Ваше имя игрок 2?')
    name2 = str(input())
    print(name1, 'Кидайте кубик')
    while game2:
        if kletka >= end1 and kletka2 >= end1 and kleyka3 >= end1 and kletka4 >= end1 and suma == 4:
            print(game1, 'Win')
            game2 = False
            k = int(input())
        elif kletka5 >= end2 and kletka6 >= end2 and kletka7 >= end2 and kletka8 >= end2 and suma2 == 4:
            print(game2, ' Win')
            game2 = False
            p = int(input())
        else:
            import random

            city_list = ['1', '2', '3', '4', '5', '6']
            dostyp = str(input())
            if dostyp == 'F':
                tort = (random.choice(city_list))
                print(name1, 'Кубик кинут - ', tort)
                game1 = True
                while game:
                    if tort == '6':
                        print('Хотите ли вы вывести фигуру?(YES-NO)')
                        vyvod = str(input())
                        if vyvod == 'YES':
                            print('Какую фигуру? 1-4')
                            vod = int(input())
                            if vod == 1:
                                figura11 = 1
                                kletka += 1
                                suma += 1
                            elif vod == 2:
                                figura22 = 1
                                kletka2 += 1
                                suma += 1
                            elif vod == 3:
                                figura33 = 1
                                kletka3 += 1
                                suma += 1
                            elif vod == 4:
                                figura44 = 1
                                kletka4 += 1
                                suma += 1
                            else:
                                print('error')
                        else:
                            print('Выбирите чем ходить 1-4')
                            vod2 = int(input())
                            if vod2 == 1:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka11 = kletka
                                for i in city_list3:
                                    kletka = (int(kletka) + int(tort))
                                    figura11=(proVerka1(figura11))
                                    if i < kletka and i > kletka11:
                                        kletka = (int(kletka) - int(tort))
                                        a = (int(i))
                                        break
                                    elif kletka == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            elif vod2 == 2:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka22 = kletka2
                                for i in city_list3:
                                    kletka2 = (int(kletka2) + int(tort))
                                    figura22 = (proVerka2(figura22))
                                    if i < kletka2 and i > kletka22:
                                        kletka2 = (int(kletka2) - int(tort))
                                        a2 = (int(i))
                                        break
                                    elif kletka2 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka2 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka2 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka2 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            elif vod2 == 3:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka33 = kletka3
                                for i in city_list3:
                                    kletka3 = (int(kletka3) + int(tort))
                                    figura33 = (proVerka3(figura33))
                                    if i < kletka3 and i > kletka33:
                                        kletka3 = (int(kletka3) - int(tort))
                                        a3 = (int(i))
                                        break
                                    elif kletka3 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka3 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka3 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka3 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            else:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka44 = kletka4
                                for i in city_list3:
                                    kletka4 = (int(kletka4) + int(tort))
                                    figura44 = (proVerka4(figura44))
                                    if i < kletka4 and i > kletka44:
                                        kletka4 = (int(kletka4) - int(tort))
                                        a4 = (int(i))
                                        break
                                    elif kletka4 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka4 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka4 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka4 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                        print('Фигура 1- ', figura11)
                        print('Фигура 2- ', figura22)
                        print('Фигура 3- ', figura33)
                        print('Фигура 4- ', figura44)
                        while game1:
                            print(name1, 'Кидайте кубик')
                            dostyp = str(input())
                            if dostyp == 'F':
                                tort = (random.choice(city_list))
                                print(name1, 'Кубик кинут - ', tort)
                                if tort == '6' and kletka == figura1:
                                    print('Выбирите чем вы хотите походить 1-4')
                                    vod = int(input())
                                    if vod == 1:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka11 = kletka
                                        for i in city_list3:
                                            kletka = (int(kletka) + int(tort))
                                            figura11 = (proVerka1(figura11))
                                            if i < kletka and i > kletka11:
                                                kletka = (int(kletka) - int(tort))
                                                a = (int(i))
                                                break
                                            elif kletka == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    elif vod == 2:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka22 = kletka2
                                        for i in city_list3:
                                            kletka2 = (int(kletka2) + int(tort))
                                            figura22 = (proVerka2(figura22))
                                            if i < kletka2 and i > kletka22:
                                                kletka2 = (int(kletka2) - int(tort))
                                                a2 = (int(i))
                                                break
                                            elif kletka2 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka2 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka2 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka2 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    elif vod == 3:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka33 = kletka3
                                        for i in city_list3:
                                            kletka3 = (int(kletka3) + int(tort))
                                            figura33 = (proVerka3(figura33))
                                            if i < kletka3 and i > kletka33:
                                                kletka3 = (int(kletka3) - int(tort))
                                                a3 = (int(i))
                                                break
                                            elif kletka3 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka3 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka3 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka3 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break

                                    else:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka44 = kletka4
                                        for i in city_list3:
                                            kletka4 = (int(kletka4) + int(tort))
                                            figura44 = (proVerka4(figura44))
                                            if i < kletka4 and i > kletka44:
                                                kletka4 = (int(kletka4) - int(tort))
                                                a4 = (int(i))
                                                break
                                            elif kletka4 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka4 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka4 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka4 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                    print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                    print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                    print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                    print('Фигура 1- ', figura11)
                                    print('Фигура 2- ', figura22)
                                    print('Фигура 3- ', figura33)
                                    print('Фигура 4- ', figura44)
                                elif tort == '6':
                                    print('Хотите ли вы вывести фигуру?(YES-NO)')
                                    vyvod = str(input())
                                    if vyvod == 'YES':
                                        print('Выберете какую 1-4')
                                        vod = int(input())
                                        if vod == 1:
                                            figura11 = 1
                                            kletka += 1
                                            suma += 1
                                        elif vod == 2:
                                            figura22 = 1
                                            kletka2 += 1
                                            suma += 1
                                        elif vod == 3:
                                            figura33 = 1
                                            kletka3 += 1
                                            suma += 1
                                        elif vod == 4:
                                            figura44 = 1
                                            kletka4 += 1
                                            suma += 1
                                        else:
                                            print('error')
                                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                        print('Фигура 1- ', figura11)
                                        print('Фигура 2- ', figura22)
                                        print('Фигура 3- ', figura33)
                                        print('Фигура 4- ', figura44)
                                    else:
                                        print('Выбирите чем ходить 1-4')
                                        vod2 = int(input())
                                        if vod2 == 1:
                                            city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                            kletka11 = kletka
                                            for i in city_list3:
                                                kletka = (int(kletka) + int(tort))
                                                figura11 = (proVerka1(figura11))
                                                if i < kletka and i > kletka11:
                                                    kletka = (int(kletka) - int(tort))
                                                    a = (int(i))
                                                    break
                                                elif kletka == kletka5:
                                                    figura55 -= 1
                                                    kletka5 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 1 противника')
                                                    print('Фигура 1- ', figura55)
                                                elif kletka == kletka6:
                                                    figura66 -= 1
                                                    kletka6 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 2 противника')
                                                    print('Фигура 2- ', figura66)
                                                elif kletka == kletka7:
                                                    figura77 -= 1
                                                    kletka7 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 3 противника')
                                                    print('Фигура 3- ', figura77)
                                                elif kletka == kletka8:
                                                    figura88 -= 1
                                                    kletka8 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 4 противника')
                                                    print('Фигура 4- ', figura88)
                                                else:
                                                    break
                                        elif vod2 == 2:
                                            city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                            kletka22 = kletka2
                                            for i in city_list3:
                                                kletka2 = (int(kletka2) + int(tort))
                                                figura22 = (proVerka2(figura22))
                                                if i < kletka2 and i > kletka22:
                                                    kletka2 = (int(kletka2) - int(tort))
                                                    a2 = (int(i))
                                                    break
                                                elif kletka2 == kletka5:
                                                    figura55 -= 1
                                                    kletka5 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 1 противника')
                                                    print('Фигура 1- ', figura55)
                                                elif kletka2 == kletka6:
                                                    figura66 -= 1
                                                    kletka6 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 2 противника')
                                                    print('Фигура 3- ', figura66)
                                                elif kletka2 == kletka7:
                                                    figura77 -= 1
                                                    kletka7 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 3 противника')
                                                    print('Фигура 3- ', figura77)
                                                elif kletka2 == kletka8:
                                                    figura88 -= 1
                                                    kletka8 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 4 противника')
                                                    print('Фигура 4- ', figura88)
                                                else:
                                                    break
                                        elif vod2 == 3:
                                            city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                            kletka33 = kletka3
                                            for i in city_list3:
                                                kletka3 = (int(kletka3) + int(tort))
                                                figura33 = (proVerka3(figura33))
                                                if i < kletka3 and i > kletka33:
                                                    kletka3 = (int(kletka3) - int(tort))
                                                    a3 = (int(i))
                                                    break
                                                elif kletka3 == kletka5:
                                                    figura55 -= 1
                                                    kletka5 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 1 противника')
                                                    print('Фигура 1- ', figura55)
                                                elif kletka3 == kletka6:
                                                    figura66 -= 1
                                                    kletka6 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 2 противника')
                                                    print('Фигура 2- ', figura66)
                                                elif kletka3 == kletka7:
                                                    figura77 -= 1
                                                    kletka7 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 3 противника')
                                                    print('Фигура 3- ', figura77)
                                                elif kletka3 == kletka8:
                                                    figura88 -= 1
                                                    kletka8 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 4 противника')
                                                    print('Фигура 4- ', figura88)
                                                else:
                                                    break
                                        else:
                                            city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                            kletka44 = kletka4
                                            for i in city_list3:
                                                kletka4 = (int(kletka4) + int(tort))
                                                figura44 = (proVerka4(figura44))
                                                if i < kletka4 and i > kletka44:
                                                    kletka4 = (int(kletka4) - int(tort))
                                                    a4 = (int(i))
                                                    break
                                                elif kletka4 == kletka5:
                                                    figura55 -= 1
                                                    kletka5 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 1 противника')
                                                    print('Фигура 1- ', figura55)
                                                elif kletka4 == kletka6:
                                                    figura66 -= 1
                                                    kletka6 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 2 противника')
                                                    print('Фигура 2- ', figura66)
                                                elif kletka4 == kletka7:
                                                    figura77 -= 1
                                                    kletka7 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 3 противника')
                                                    print('Фигура 3- ', figura77)
                                                elif kletka4 == kletka8:
                                                    figura88 -= 1
                                                    kletka8 = 0
                                                    suma2 -= 1
                                                    print('Вы скушали фигуру 4 противника')
                                                    print('Фигура 4- ', figura88)
                                                else:
                                                    break
                                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                        print('Фигура 1- ', figura11)
                                        print('Фигура 2- ', figura22)
                                        print('Фигура 3- ', figura33)
                                        print('Фигура 4- ', figura44)
                                elif tort == '1' or '2' or '3' or '4' or '5':
                                    print('Выбирите чем ходить 1-4')
                                    vod2 = int(input())
                                    if vod2 == 1:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka11 = kletka
                                        for i in city_list3:
                                            kletka = (int(kletka) + int(tort))
                                            figura11 = (proVerka1(figura11))
                                            if i < kletka and i > kletka11:
                                                kletka = (int(kletka) - int(tort))
                                                a = (int(i))
                                                break
                                            elif kletka == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    elif vod2 == 2:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka22 = kletka2
                                        for i in city_list3:
                                            kletka2 = (int(kletka2) + int(tort))
                                            figura22 = (proVerka2(figura22))
                                            if i < kletka2 and i > kletka22:
                                                kletka2 = (int(kletka2) - int(tort))
                                                a2 = (int(i))
                                                break
                                            elif kletka2 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka2 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka2 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka2 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    elif vod2 == 3:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka33 = kletka3
                                        for i in city_list3:
                                            kletka3 = (int(kletka3) + int(tort))
                                            figura33 = (proVerka3(figura33))
                                            if i < kletka3 and i > kletka33:
                                                kletka3 = (int(kletka3) - int(tort))
                                                a3 = (int(i))
                                                break
                                            elif kletka3 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka3 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka3 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka3 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    else:
                                        city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                        kletka44 = kletka4
                                        for i in city_list3:
                                            kletka4 = (int(kletka4) + int(tort))
                                            figura44 = (proVerka4(figura44))
                                            if i < kletka4 and i > kletka44:
                                                kletka4 = (int(kletka4) - int(tort))
                                                a4 = (int(i))
                                                break
                                            elif kletka4 == kletka5:
                                                figura55 -= 1
                                                kletka5 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura55)
                                            elif kletka4 == kletka6:
                                                figura66 -= 1
                                                kletka6 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura66)
                                            elif kletka4 == kletka7:
                                                figura77 -= 1
                                                kletka7 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura77)
                                            elif kletka4 == kletka8:
                                                figura88 -= 1
                                                kletka8 = 0
                                                suma2 -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura88)
                                            else:
                                                break
                                    print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                    print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                    print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                    print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                    print('Фигура 1- ', figura11)
                                    print('Фигура 2- ', figura22)
                                    print('Фигура 3- ', figura33)
                                    print('Фигура 4- ', figura44)
                                    break
                                    # game1=False

                    elif tort == '1' or '2' or '3' or '4' or '5':
                        print(name1, 'у вас есть фигура YES-NO')  # BAG
                        top = str(input())
                        if top == 'YES':
                            print('Выбирите чем ходить 1-4')
                            vod2 = int(input())
                            if vod2 == 1:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka11 = kletka
                                for i in city_list3:
                                    kletka = (int(kletka) + int(tort))
                                    figura11 = (proVerka1(figura11))
                                    if i < kletka and i > kletka11:
                                        kletka = (int(kletka) - int(tort))
                                        a = (int(i))
                                        break
                                    elif kletka == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            elif vod2 == 2:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka22 = kletka2
                                for i in city_list3:
                                    kletka2 = (int(kletka2) + int(tort))
                                    figura22 = (proVerka2(figura22))
                                    if i < kletka2 and i > kletka22:
                                        kletka2 = (int(kletka2) - int(tort))
                                        a2 = (int(i))
                                        break
                                    elif kletka2 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka2 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka2 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka2 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            elif vod2 == 3:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka33 = kletka3
                                for i in city_list3:
                                    kletka3 = (int(kletka3) + int(tort))
                                    figura33 = (proVerka3(figura33))
                                    if i < kletka3 and i > kletka33:
                                        kletka3 = (int(kletka3) - int(tort))
                                        a3 = (int(i))
                                        break
                                    elif kletka3 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka3 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka3 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka3 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                            else:
                                city_list3 = [kletka5, kletka6, kletka7, kletka8]
                                kletka44 = kletka4
                                for i in city_list3:
                                    kletka4 = (int(kletka4) + int(tort))
                                    figura44 = (proVerka4(figura44))
                                    if i < kletka4 and i > kletka44:
                                        kletka4 = (int(kletka4) - int(tort))
                                        a4 = (int(i))
                                        break
                                    elif kletka4 == kletka5:
                                        figura55 -= 1
                                        kletka5 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 1 противника')
                                        print('Фигура 1- ', figura55)
                                    elif kletka4 == kletka6:
                                        figura66 -= 1
                                        kletka6 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 2 противника')
                                        print('Фигура 2- ', figura66)
                                    elif kletka4 == kletka7:
                                        figura77 -= 1
                                        kletka7 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 3 противника')
                                        print('Фигура 3- ', figura77)
                                    elif kletka4 == kletka8:
                                        figura88 -= 1
                                        kletka8 = 0
                                        suma2 -= 1
                                        print('Вы скушали фигуру 4 противника')
                                        print('Фигура 4- ', figura88)
                                    else:
                                        break
                        else:
                            print('OK')
                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                        print('Фигура 1- ', figura11)
                        print('Фигура 2- ', figura22)
                        print('Фигура 3- ', figura33)
                        print('Фигура 4- ', figura44)
                        print('Ход слд. игрока', name2)
                        print(name2, 'Кидайте кубик')
                        dostyp = str(input())
                        if dostyp == 'F':
                            tort = (random.choice(city_list))
                            print(name2, 'Кубик кинут - ', tort)
                            # tort=('6')######
                            if tort == '6':
                                print('Хотите ли вы вывести фигуру?(YES-NO)')
                                vyvod = str(input())
                                if vyvod == 'YES':
                                    print('Какую фигуру? 1-4')
                                    vod = int(input())
                                    if vod == 1:
                                        figura55 = 1
                                        kletka5 += 8
                                        suma2 += 1
                                    elif vod == 2:
                                        figura66 = 1
                                        kletka6 += 8
                                        suma2 += 1
                                    elif vod == 3:
                                        figura77 = 1
                                        kletka7 += 8
                                        suma2 += 1
                                    elif vod == 4:
                                        figura88 = 1
                                        kletka8 += 8
                                        suma2 += 1
                                    else:
                                        print('error')
                                else:
                                    print('Выбирите чем ходить 1-4')
                                    vod2 = int(input())
                                    if vod2 == 1:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka55 = kletka5
                                        for i in city_list1:
                                            kletka5 = (int(kletka5) + int(tort))
                                            kletka5 = (proVerka(kletka5))
                                            if i < kletka5 and i > kletka55:
                                                kletka5 = (int(kletka5) - int(tort))
                                                a5 = (int(i))
                                                kletka5 = (proVerka(kletka5))
                                                break
                                            # kletka5=(proVerka(kletka5))
                                            elif kletka5 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka5 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka5 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka5 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                    elif vod2 == 2:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka66 = kletka6
                                        for i in city_list1:
                                            kletka6 = (int(kletka6) + int(tort))
                                            kletka6 = (proVerka(kletka6))
                                            if i < kletka6 and i > kletka66:
                                                kletka6 = (int(kletka6) - int(tort))
                                                a6 = (int(i))
                                                kletka6 = (proVerka(kletka6))
                                                break
                                            # kletka6=(proVerka(kletka6))
                                            elif kletka6 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka6 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura33)
                                            elif kletka6 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura44)
                                            elif kletka6 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                    elif vod2 == 3:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka77 = kletka7
                                        for i in city_list1:
                                            kletka7 = (int(kletka7) + int(tort))
                                            kletka7 = (proVerka(kletka7))
                                            if i < kletka7 and i > kletka77:
                                                kletka7 = (int(kletka7) - int(tort))
                                                a7 = (int(i))
                                                kletka7 = (proVerka(kletka7))
                                                break
                                            # kletka7=(proVerka(kletka7))
                                            elif kletka7 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka7 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka7 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka7 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura11)
                                            else:
                                                break
                                    else:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka88 = kletka8
                                        for i in city_list1:
                                            kletka8 = (int(kletka8) + int(tort))
                                            kletka8 = (proVerka(kletka8))
                                            if i < kletka8 and i > kletka88:
                                                kletka8 = (int(kletka8) - int(tort))
                                                a8 = (int(i))
                                                kletka8 = (proVerka(kletka8))
                                                break
                                            # kletka8=(proVerka(kletka8))
                                            elif kletka8 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka8 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka8 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka8 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                print('Фигура 1- ', figura55)
                                print('Фигура 2- ', figura66)
                                print('Фигура 3- ', figura77)
                                print('Фигура 4- ', figura88)
                                while game3:
                                    print(name2, 'Кидайте кубик')
                                    dostyp = str(input())
                                    if dostyp == 'F':
                                        tort = (random.choice(city_list))
                                        print(name2, 'Кубик кинут - ', tort)
                                        # tort=('6')#########
                                        if tort == '6' and kletka5 == figura5:
                                            print('Выбирите чем вы хотите походить 1-4')
                                            vod2 = int(input())
                                            if vod2 == 1:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka55 = kletka5
                                                for i in city_list1:
                                                    kletka5 = (int(kletka5) + int(tort))
                                                    kletka5 = (proVerka(kletka5))
                                                    if i < kletka5 and i > kletka55:
                                                        kletka5 = (int(kletka5) - int(tort))
                                                        a5 = (int(i))
                                                        kletka5 = (proVerka(kletka5))
                                                        break
                                                    # kletka5=(proVerka(kletka5))
                                                    elif kletka5 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka5 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka5 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka5 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                            elif vod2 == 2:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka66 = kletka6
                                                for i in city_list1:
                                                    kletka6 = (int(kletka6) + int(tort))
                                                    kletka6 = (proVerka(kletka6))
                                                    if i < kletka6 and i > kletka66:
                                                        kletka6 = (int(kletka6) - int(tort))
                                                        a6 = (int(i))
                                                        kletka6 = (proVerka(kletka6))
                                                        break
                                                    # kletka6=(proVerka(kletka6))
                                                    elif kletka6 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka6 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura33)
                                                    elif kletka6 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura44)
                                                    elif kletka6 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                            elif vod2 == 3:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka77 = kletka7
                                                for i in city_list1:
                                                    kletka7 = (int(kletka7) + int(tort))
                                                    kletka7 = (proVerka(kletka7))
                                                    if i < kletka7 and i > kletka77:
                                                        kletka7 = (int(kletka7) - int(tort))
                                                        a7 = (int(i))
                                                        kletka7 = (proVerka(kletka7))
                                                        break
                                                    # kletka7=(proVerka(kletka7))
                                                    elif kletka7 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka7 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka7 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka7 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura11)
                                                    else:
                                                        break
                                            else:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka88 = kletka8
                                                for i in city_list1:
                                                    kletka8 = (int(kletka8) + int(tort))
                                                    kletka8 = (proVerka(kletka8))
                                                    if i < kletka8 and i > kletka88:
                                                        kletka8 = (int(kletka8) - int(tort))
                                                        a8 = (int(i))
                                                        kletka8 = (proVerka(kletka8))
                                                        break
                                                    # kletka8=(proVerka(kletka8))
                                                    elif kletka8 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka8 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka8 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka8 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                                        # break
                                        elif tort == '6':
                                            print('Хотите ли вы вывести фигуру?(YES-NO)')
                                            vyvod = str(input())
                                            if vyvod == 'YES':
                                                print('Выберете какую 1-4')
                                                vod = int(input())
                                                if vod == 1:
                                                    figura55 = 1
                                                    kletka5 += 8
                                                    suma2 += 1
                                                elif vod == 2:
                                                    figura66 = 1
                                                    kletka6 += 8
                                                    suma2 += 1
                                                elif vod == 3:
                                                    figura77 = 1
                                                    kletka7 += 8
                                                    suma2 += 1
                                                elif vod == 4:
                                                    figura88 = 1
                                                    kletka8 += 8
                                                    suma2 += 1
                                                else:
                                                    print('error')
                                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                                print('Фигура 1- ', figura55)
                                                print('Фигура 2- ', figura66)
                                                print('Фигура 3- ', figura77)
                                                print('Фигура 4- ', figura88)
                                            else:
                                                print('Выбирите чем ходить 1-4')
                                                vod2 = int(input())
                                                if vod2 == 1:
                                                    city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                    kletka55 = kletka5
                                                    for i in city_list1:
                                                        kletka5 = (int(kletka5) + int(tort))
                                                        kletka5 = (proVerka(kletka5))
                                                        if i < kletka5 and i > kletka55:
                                                            kletka5 = (int(kletka5) - int(tort))
                                                            a5 = (int(i))
                                                            kletka5 = (proVerka(kletka5))
                                                            break
                                                        # kletka5=(proVerka(kletka5))
                                                        elif kletka5 == kletka:
                                                            figura11 -= 1
                                                            kletka = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 1 противника')
                                                            print('Фигура 1- ', figura11)
                                                        elif kletka5 == kletka2:
                                                            figura22 -= 1
                                                            kletka2 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 2 противника')
                                                            print('Фигура 2- ', figura22)
                                                        elif kletka5 == kletka3:
                                                            figura33 -= 1
                                                            kletka3 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 3 противника')
                                                            print('Фигура 3- ', figura33)
                                                        elif kletka5 == kletka4:
                                                            figura44 -= 1
                                                            kletka4 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 4 противника')
                                                            print('Фигура 4- ', figura44)
                                                        else:
                                                            break
                                                elif vod2 == 2:
                                                    city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                    kletka66 = kletka6
                                                    for i in city_list1:
                                                        kletka6 = (int(kletka6) + int(tort))
                                                        kletka6 = (proVerka(kletka6))
                                                        if i < kletka6 and i > kletka66:
                                                            kletka6 = (int(kletka6) - int(tort))
                                                            a6 = (int(i))
                                                            kletka6 = (proVerka(kletka6))
                                                            break
                                                        # kletka6=(proVerka(kletka6))
                                                        elif kletka6 == kletka:
                                                            figura11 -= 1
                                                            kletka = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 1 противника')
                                                            print('Фигура 1- ', figura11)
                                                        elif kletka6 == kletka2:
                                                            figura22 -= 1
                                                            kletka2 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 2 противника')
                                                            print('Фигура 2- ', figura33)
                                                        elif kletka6 == kletka3:
                                                            figura33 -= 1
                                                            kletka3 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 3 противника')
                                                            print('Фигура 3- ', figura44)
                                                        elif kletka6 == kletka4:
                                                            figura44 -= 1
                                                            kletka4 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 4 противника')
                                                            print('Фигура 4- ', figura44)
                                                        else:
                                                            break
                                                elif vod2 == 3:
                                                    city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                    kletka77 = kletka7
                                                    for i in city_list1:
                                                        kletka7 = (int(kletka7) + int(tort))
                                                        kletka7 = (proVerka(kletka7))
                                                        if i < kletka7 and i > kletka77:
                                                            kletka7 = (int(kletka7) - int(tort))
                                                            a7 = (int(i))
                                                            kletka7 = (proVerka(kletka7))
                                                            break
                                                        # kletka7=(proVerka(kletka7))
                                                        elif kletka7 == kletka:
                                                            figura11 -= 1
                                                            kletka = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 1 противника')
                                                            print('Фигура 1- ', figura11)
                                                        elif kletka7 == kletka2:
                                                            figura22 -= 1
                                                            kletka2 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 2 противника')
                                                            print('Фигура 2- ', figura22)
                                                        elif kletka7 == kletka3:
                                                            figura33 -= 1
                                                            kletka3 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 3 противника')
                                                            print('Фигура 3- ', figura33)
                                                        elif kletka7 == kletka4:
                                                            figura44 -= 1
                                                            kletka4 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 4 противника')
                                                            print('Фигура 4- ', figura11)
                                                        else:
                                                            break
                                                else:
                                                    city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                    kletka88 = kletka8
                                                    for i in city_list1:
                                                        kletka8 = (int(kletka8) + int(tort))
                                                        kletka8 = (proVerka(kletka8))
                                                        if i < kletka8 and i > kletka88:
                                                            kletka8 = (int(kletka8) - int(tort))
                                                            a8 = (int(i))
                                                            kletka8 = (proVerka(kletka8))
                                                            break
                                                        # kletka8=(proVerka(kletka8))
                                                        elif kletka8 == kletka:
                                                            figura11 -= 1
                                                            kletka = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 1 противника')
                                                            print('Фигура 1- ', figura11)
                                                        elif kletka8 == kletka2:
                                                            figura22 -= 1
                                                            kletka2 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 2 противника')
                                                            print('Фигура 2- ', figura22)
                                                        elif kletka8 == kletka3:
                                                            figura33 -= 1
                                                            kletka3 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 3 противника')
                                                            print('Фигура 3- ', figura33)
                                                        elif kletka8 == kletka4:
                                                            figura44 -= 1
                                                            kletka4 = 0
                                                            suma -= 1
                                                            print('Вы скушали фигуру 4 противника')
                                                            print('Фигура 4- ', figura44)
                                                        else:
                                                            break
                                                            # break
                                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                                print('Фигура 1- ', figura55)
                                                print('Фигура 2- ', figura66)
                                                print('Фигура 3- ', figura77)
                                                print('Фигура 4- ', figura88)
                                                break

                                        else:
                                            print('Выбирите чем ходить 1-4')
                                            vod2 = int(input())
                                            if vod2 == 1:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka55 = kletka5
                                                for i in city_list1:
                                                    kletka5 = (int(kletka5) + int(tort))
                                                    kletka5 = (proVerka(kletka5))
                                                    if i < kletka5 and i > kletka55:
                                                        kletka5 = (int(kletka5) - int(tort))
                                                        a5 = (int(i))
                                                        kletka5 = (proVerka(kletka5))
                                                        break
                                                    elif kletka5 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka5 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka5 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka5 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                            elif vod2 == 2:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka66 = kletka6
                                                for i in city_list1:
                                                    kletka6 = (int(kletka6) + int(tort))
                                                    kletka6 = (proVerka(kletka6))
                                                    if i < kletka6 and i > kletka66:
                                                        kletka6 = (int(kletka6) - int(tort))
                                                        a6 = (int(i))
                                                        kletka6 = (proVerka(kletka6))
                                                        break
                                                    # kletka6=(proVerka(kletka6))
                                                    elif kletka6 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka6 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura33)
                                                    elif kletka6 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura44)
                                                    elif kletka6 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                            elif vod2 == 3:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka77 = kletka7
                                                for i in city_list1:
                                                    kletka7 = (int(kletka7) + int(tort))
                                                    kletka7 = (proVerka(kletka7))
                                                    if i < kletka7 and i > kletka77:
                                                        kletka7 = (int(kletka7) - int(tort))
                                                        a7 = (int(i))
                                                        kletka7 = (proVerka(kletka7))
                                                        break
                                                    # kletka7=(proVerka(kletka7))
                                                    elif kletka7 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka7 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka7 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka7 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura11)
                                                    else:
                                                        break
                                            else:
                                                city_list1 = [kletka, kletka2, kletka3, kletka4]
                                                kletka88 = kletka8
                                                for i in city_list1:
                                                    kletka8 = (int(kletka8) + int(tort))
                                                    kletka8 = (proVerka(kletka8))
                                                    if i < kletka8 and i > kletka88:
                                                        kletka8 = (int(kletka8) - int(tort))
                                                        a8 = (int(i))
                                                        kletka8 = (proVerka(kletka8))
                                                        break
                                                    # kletka8=(proVerka(kletka8))
                                                    elif kletka8 == kletka:
                                                        figura11 -= 1
                                                        kletka = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 1 противника')
                                                        print('Фигура 1- ', figura11)
                                                    elif kletka8 == kletka2:
                                                        figura22 -= 1
                                                        kletka2 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 2 противника')
                                                        print('Фигура 2- ', figura22)
                                                    elif kletka8 == kletka3:
                                                        figura33 -= 1
                                                        kletka3 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 3 противника')
                                                        print('Фигура 3- ', figura33)
                                                    elif kletka8 == kletka4:
                                                        figura44 -= 1
                                                        kletka4 = 0
                                                        suma -= 1
                                                        print('Вы скушали фигуру 4 противника')
                                                        print('Фигура 4- ', figura44)
                                                    else:
                                                        break
                                            print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                            print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                            print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                            print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                            print('Фигура 1- ', figura55)
                                            print('Фигура 2- ', figura66)
                                            print('Фигура 3- ', figura77)
                                            print('Фигура 4- ', figura88)
                                            print('Ход слд. игрока', name1)
                                            print(name1, 'Кидайте кубик')
                                            tort = (random.choice(city_list))
                                            print(name1, 'Кубик кинут - ', tort)
                                            break
                                            # game=False
                            else:
                                print(name2, 'у вас есть фигура YES-NO')
                                top = str(input())
                                if top == 'YES':
                                    print('Выбирите чем ходить 1-4')
                                    vod2 = int(input())
                                    if vod2 == 1:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka55 = kletka5
                                        for i in city_list1:
                                            kletka5 = (int(kletka5) + int(tort))
                                            kletka5 = (proVerka(kletka5))
                                            if i < kletka5 and i > kletka55:
                                                kletka5 = (int(kletka5) - int(tort))
                                                a5 = (int(i))
                                                kletka5 = (proVerka(kletka5))
                                                break
                                            # kletka5=(proVerka(kletka5))
                                            elif kletka5 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka5 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka5 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka5 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                    elif vod2 == 2:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka66 = kletka6
                                        for i in city_list1:
                                            kletka6 = (int(kletka6) + int(tort))
                                            kletka6 = (proVerka(kletka6))
                                            if i < kletka6 and i > kletka66:
                                                kletka6 = (int(kletka6) - int(tort))
                                                a6 = (int(i))
                                                kletka6 = (proVerka(kletka6))
                                                break
                                            # kletka6=(proVerka(kletka6))
                                            elif kletka6 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka6 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura33)
                                            elif kletka6 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura44)
                                            elif kletka6 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                    elif vod2 == 3:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka77 = kletka7
                                        for i in city_list1:
                                            kletka7 = (int(kletka7) + int(tort))
                                            kletka7 = (proVerka(kletka7))
                                            if i < kletka7 and i > kletka77:
                                                kletka7 = (int(kletka7) - int(tort))
                                                a7 = (int(i))
                                                kletka7 = (proVerka(kletka7))
                                                break
                                            # kletka7=(proVerka(kletka7))
                                            elif kletka7 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka7 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka7 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka7 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura11)
                                            else:
                                                break
                                    else:
                                        city_list1 = [kletka, kletka2, kletka3, kletka4]
                                        kletka88 = kletka8
                                        for i in city_list1:
                                            kletka8 = (int(kletka8) + int(tort))
                                            kletka8 = (proVerka(kletka8))
                                            if i < kletka8 and i > kletka88:
                                                kletka8 = (int(kletka8) - int(tort))
                                                a8 = (int(i))
                                                kletka8 = (proVerka(kletka8))
                                                break
                                            # kletka8=(proVerka(kletka8))
                                            elif kletka8 == kletka:
                                                figura11 -= 1
                                                kletka = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 1 противника')
                                                print('Фигура 1- ', figura11)
                                            elif kletka8 == kletka2:
                                                figura22 -= 1
                                                kletka2 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 2 противника')
                                                print('Фигура 2- ', figura22)
                                            elif kletka8 == kletka3:
                                                figura33 -= 1
                                                kletka3 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 3 противника')
                                                print('Фигура 3- ', figura33)
                                            elif kletka8 == kletka4:
                                                figura44 -= 1
                                                kletka4 = 0
                                                suma -= 1
                                                print('Вы скушали фигуру 4 противника')
                                                print('Фигура 4- ', figura44)
                                            else:
                                                break
                                else:
                                    print('OK')
                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                print('Фигура 1- ', figura55)
                                print('Фигура 2- ', figura66)
                                print('Фигура 3- ', figura77)
                                print('Фигура 4- ', figura88)
                                print('Ход слд. игрока', name1)
                                print(name1, 'Кидайте кубик')
                                # tort=(random.choice(city_list))
                                # print(name1,'Кубик кинут - ', tort)
                                break
                                # game=False
                    # else:
                    # print('Ход слд. игрока', name2)
                # else:
                # game=False
                else:
                    print('Ход слд. игрока', name1)
                    # game=False

    # else:
    # game2=False
    # print('game over')
elif vybor == 3:
    print('will be ready in version v2.0')
elif vybor == 4:
    print('will be ready in version v3.0')
else:
    print('Game over')

# import random

# city_list = [1, 2, 3, 4, 5, 6]
# print("Выбор случайного города из списка - ", random.choice(city_list))


