print('Игра Муха(Мини-Нарды)')
print('Выбирите количество игроков 2-4')
end1=28
end2=35
#Game1
figura1=1
figura11=0
figura2=1
figura22=0
figura33=0
figura44=0
suma=1
kletka=0
kletka2=0
kletka3=0
kletka4=0
#Game2
figura5=4
figura55=0
figura6=4
figura66=0
figura77=0
figura88=0
suma2=1
kletka5=0
kletka6=0
kletka7=0
kletka8=0
game1=True
game=True
game2=True
game3=True
vybor=int(input())
if vybor==2:
    print('Ваше имя игрок 1?')
    name1= str(input( ))
    print('Ваше имя игрок 2?')
    name2= str(input( ))
    print(name1,'Кидайте кубик')
    while game2:
        if kletka>=end1 or kletka2>=end1:
            print('Game1 Win')
            game2=False
        elif kletka5>=end2 or kletka6>=end2:
            print('Game2 Win')
            game2=False 
        else:
            import random

            city_list = ['1','2','3','4','5','6']
            dostyp=str(input( ))
            if dostyp=='F':
                tort=(random.choice(city_list))                
                print(name1,'Кубик кинут - ', tort)
                #figura11=1
                #figura11+=3
                #figura11-=2
                #figura11-=1
                game1=True
                while game:
                    if tort=='6':
                        print('Хотите ли вы вывести фигуру?(YES-NO)')
                        vyvod=str(input( ))
                        if vyvod=='YES':
                            print('Какую фигуру? 1-4')
                            vod=int(input())
                            if vod==1:
                                figura11=1
                                kletka+=1
                            elif vod==2:
                                figura22=1
                                kletka2+=1
                            elif vod==3:
                                figura33=1
                                kletka3+=1
                            elif vod==4:
                                figura44=1
                                kletka4+=1
                            else:
                                print('error')
                        else:
                            print('Выбирите чем ходить 1-4')
                            vod2=int(input())
                            if vod2==1:
                                kletka=(int(kletka)+int(tort))
                            elif vod2==2:
                                kletka2=(int(kletka2)+int(tort))
                            elif vod2==3:
                                kletka3=(int(kletka3)+int(tort))
                            else:
                                kletka4=(int(kletka4)+int(tort))
                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                        print('Фигура 1- ', figura11 )
                        print('Фигура 2- ', figura22 )
                        print('Фигура 3- ', figura33 )
                        print('Фигура 4- ', figura44 )
                        while game1:
                            print(name1,'Кидайте кубик')
                            dostyp=str(input( ))
                            if dostyp=='F':
                                tort=(random.choice(city_list))
                                print(name1,'Кубик кинут - ', tort)
                                if tort=='6' and kletka==figura1:
                                    print('Выбирите чем вы хотите походить 1-4')
                                    vod=int(input())
                                    if vod==1:
                                        kletka=(int(kletka)+int(tort))
                                    elif vod==2:
                                        kletka2=(int(kletka2)+int(tort))
                                    elif vod==3:
                                        kletka3=(int(kletka3)+int(tort))
                                    else:       
                                        kletka4=(int(kletka4)+int(tort))
                                    print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                    print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                    print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                    print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                    print('Фигура 1- ', figura11 )
                                    print('Фигура 2- ', figura22 )
                                    print('Фигура 3- ', figura33 )
                                    print('Фигура 4- ', figura44 ) 
                                elif tort=='6':
                                    print('Хотите ли вы вывести фигуру?(YES-NO)')
                                    vyvod=str(input( ))
                                    if vyvod=='YES':
                                        print('Выберете какую 1-4')
                                        vod=int(input())
                                        if vod==1:
                                            figura11=1
                                            kletka+=1
                                        elif vod==2:
                                            figura22=1
                                            kletka2+=1
                                        elif vod==3:
                                            figura33=1
                                            kletka3+=1
                                        elif vod==4:
                                            figura44=1
                                            kletka4+=1
                                        else:
                                            print('error')
                                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                        print('Фигура 1- ', figura11 )
                                        print('Фигура 2- ', figura22 )
                                        print('Фигура 3- ', figura33 )
                                        print('Фигура 4- ', figura44 )     
                                    else:
                                        print('Выбирите чем ходить 1-4')
                                        vod2=int(input())
                                        if vod2==1:
                                            kletka=(int(kletka)+int(tort))
                                        elif vod2==2:
                                            kletka2=(int(kletka2)+int(tort))
                                        elif vod2==3:
                                            kletka3=(int(kletka3)+int(tort))
                                        else:
                                            kletka4=(int(kletka4)+int(tort))
                                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка') 
                                        print('Фигура 1- ', figura11 )
                                        print('Фигура 2- ', figura22 )
                                        print('Фигура 3- ', figura33 )
                                        print('Фигура 4- ', figura44 )
                                elif tort=='1' or '2' or '3' or '4' or '5':
                                    print('Выбирите чем ходить 1-4')
                                    vod2=int(input())
                                    if vod2==1:
                                        kletka=(int(kletka)+int(tort))
                                    elif vod2==2:
                                        kletka2=(int(kletka2)+int(tort))
                                    elif vod2==3:
                                        kletka3=(int(kletka3)+int(tort))
                                    else:
                                        kletka4=(int(kletka4)+int(tort))
                                    print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                                    print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                                    print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                                    print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                                    print('Фигура 1- ', figura11 )
                                    print('Фигура 2- ', figura22 )
                                    print('Фигура 3- ', figura33 )
                                    print('Фигура 4- ', figura44 ) 
                                    break
                                    #game1=False

                    elif tort=='1' or '2' or '3' or '4' or '5':
                        print(name1,'у вас есть фигура YES-NO')#BAG
                        top=str(input())
                        if top=='YES':
                            print('Выбирите чем ходить 1-4')
                            vod2=int(input())
                            if vod2==1:
                                kletka=(int(kletka)+int(tort))
                            elif vod2==2:
                                kletka2=(int(kletka2)+int(tort))
                            elif vod2==3:
                                kletka3=(int(kletka3)+int(tort)) 
                            else:
                                kletka4=(int(kletka4)+int(tort))
                        else:
                            print('OK')
                        print('Местонахождение Фигуры 1-', kletka, 'Клеточка')
                        print('Местонахождение Фигуры 2-', kletka2, 'Клеточка')
                        print('Местонахождение Фигуры 3-', kletka3, 'Клеточка')
                        print('Местонахождение Фигуры 4-', kletka4, 'Клеточка')
                        print('Фигура 1- ', figura11 )
                        print('Фигура 2- ', figura22 )
                        print('Фигура 3- ', figura33 )
                        print('Фигура 4- ', figura44 )
                        print('Ход слд. игрока', name2)
                        print(name2,'Кидайте кубик')
                        dostyp=str(input( ))
                        if dostyp=='F':
                            tort=(random.choice(city_list))
                            print(name2,'Кубик кинут - ', tort)
                            #tort=('6')###### 
                            if tort=='6':
                                print('Хотите ли вы вывести фигуру?(YES-NO)')
                                vyvod=str(input( ))
                                if vyvod=='YES':
                                    print('Какую фигуру? 1-4')
                                    vod=int(input())
                                    if vod==1:
                                        figura55=1
                                        kletka5+=8
                                    elif vod==2:
                                        figura66=1
                                        kletka6+=8
                                    elif vod==3:
                                        figura77=1
                                        kletka7+=8
                                    else:
                                        print('error')
                                else:
                                    print('Выбирите чем ходить 1-4')
                                    vod2=int(input())
                                    if vod2==1:
                                        kletka5=(int(kletka5)+int(tort))
                                    elif vod2==2:
                                        kletka6=(int(kletka6)+int(tort))
                                    elif vod2==3:
                                        kletka7=(int(kletka7)+int(tort)) 
                                    else:
                                        kletka8=(int(kletka8)+int(tort))
                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                print('Фигура 1- ', figura55 )
                                print('Фигура 2- ', figura66 )
                                print('Фигура 3- ', figura77 )
                                print('Фигура 4- ', figura88 )
                                while game3:
                                    print(name2,'Кидайте кубик')
                                    dostyp=str(input( ))
                                    if dostyp=='F':
                                        tort=(random.choice(city_list))
                                        print(name2,'Кубик кинут - ', tort)
                                        #tort=('6')#########
                                        if tort=='6' and kletka5==figura5:
                                            print('Выбирите чем вы хотите походить 1-4')
                                            vod2=int(input())
                                            if vod2==1:
                                                 kletka5=(int(kletka5)+int(tort))
                                            elif vod2==2:
                                                 kletka5=(int(kletka5)+int(tort))
                                            elif vod2==3:
                                                 kletka5=(int(kletka5)+int(tort)) 
                                            else:       
                                                 kletka6=(int(kletka6)+int(tort))
                                            print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                            print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                            print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                            print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                            print('Фигура 1- ', figura55 )
                                            print('Фигура 2- ', figura66 )
                                            print('Фигура 3- ', figura77 )
                                            print('Фигура 4- ', figura88 ) 
                                            #break
                                        elif tort=='6':
                                            print('Хотите ли вы вывести фигуру?(YES-NO)')
                                            vyvod=str(input( ))
                                            if vyvod=='YES':
                                                print('Выберете какую 1-4')
                                                vod=int(input())
                                                if vod==1:
                                                    figura55=1
                                                    kletka5+=8
                                                elif vod==2:
                                                    figura66=1
                                                    kletka6+=8
                                                elif vod==3:
                                                    figura77=1
                                                    kletka7+=8
                                                elif vod==4:
                                                    figura88=1
                                                    kletka8+=8 
                                                else:
                                                    print('error')
                                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                                print('Фигура 1- ', figura55 )
                                                print('Фигура 2- ', figura66 )
                                                print('Фигура 3- ', figura77 )
                                                print('Фигура 4- ', figura88 )
                                            else:
                                                print('Выбирите чем ходить 1-4')
                                                vod2=int(input())
                                                if vod2==1:
                                                    kletka5=(int(kletka5)+int(tort))
                                                elif vod2==2:
                                                    kletka6=(int(kletka6)+int(tort))
                                                elif vod2==3:
                                                    kletka7=(int(kletka7)+int(tort))
                                                else:
                                                    kletka8=(int(kletka8)+int(tort))
                                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                                print('Фигура 1- ', figura55 )
                                                print('Фигура 2- ', figura66 )
                                                print('Фигура 3- ', figura77 )
                                                print('Фигура 4- ', figura88 ) 
                                                break

                                        else:
                                            print('Выбирите чем ходить 1-4')
                                            vod2=int(input())
                                            if vod2==1:
                                                kletka5=(int(kletka5)+int(tort))
                                            elif vod2==2:
                                                kletka6=(int(kletka6)+int(tort))
                                            elif vod2==3:
                                                kletka7=(int(kletka7)+int(tort)) 
                                            else:
                                                kletka8=(int(kletka8)+int(tort))
                                            print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                            print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                            print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                            print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                            print('Фигура 1- ', figura55 )
                                            print('Фигура 2- ', figura66 )
                                            print('Фигура 3- ', figura77 )
                                            print('Фигура 4- ', figura88 )
                                            print('Ход слд. игрока', name1)
                                            print(name1,'Кидайте кубик')
                                            tort=(random.choice(city_list))
                                            print(name1,'Кубик кинут - ', tort)
                                            break
                                            #game=False
                            else:
                                print(name2,'у вас есть фигура YES-NO')
                                top=str(input())
                                if top=='YES':
                                    print('Выбирите чем ходить 1-4')
                                    vod2=int(input())
                                    if vod2==1:
                                        kletka5=(int(kletka5)+int(tort))
                                    elif vod2==2:
                                        kletka6=(int(kletka6)+int(tort))
                                    elif vod2==3:
                                        kletka7=(int(kletka7)+int(tort))
                                    else:
                                        kletka8=(int(kletka8)+int(tort))
                                else:
                                    print('OK')
                                print('Местонахождение Фигуры 1-', kletka5, 'Клеточка')
                                print('Местонахождение Фигуры 2-', kletka6, 'Клеточка')
                                print('Местонахождение Фигуры 3-', kletka7, 'Клеточка')
                                print('Местонахождение Фигуры 4-', kletka8, 'Клеточка')
                                print('Фигура 1- ', figura55 )
                                print('Фигура 2- ', figura66 )
                                print('Фигура 3- ', figura77 )
                                print('Фигура 4- ', figura88 )
                                print('Ход слд. игрока', name1)
                                print(name1,'Кидайте кубик')
                                #tort=(random.choice(city_list))
                                #print(name1,'Кубик кинут - ', tort)
                                break
                                #game=False
                    #else:
                        #print('Ход слд. игрока', name2)                 
            #else:
                #game=False       
                else:
                    print('Ход слд. игрока',name1)
                    #game=False
                
    #else:
        #game2=False
        #print('game over')
elif vybor==3:
    print('will be ready in version v2.0')
elif vybor==4:
    print('will be ready in version v3.0')
else:
    print('Game over')

#import random

#city_list = [1, 2, 3, 4, 5, 6]
#print("Выбор случайного города из списка - ", random.choice(city_list))

