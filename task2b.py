# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

print('Имеется 2021 конфет,за ход можно забирать не более 28 конфет.Выграл тот,кто делает ход последним')

print('Введите имя  игрока')
oneplayer = input()
twoplayer=('ivan botavich')

i=randint(0,1)
if i==0:
    print (f"Первый ходит {oneplayer}")
if i==1:
    print (f"Первый ходит {twoplayer}")

# игра против умного бота 

count=2021

if i==1:
    stepbot=randint(0,28)
    print (f"{twoplayer} забирает  {stepbot} конфет")
    count=count-stepbot
    print ('Остаток конфеток')
    print (count)

while count>0:
    print('Введите кол-во конфет')
    stepplayer=int(input())
    if stepplayer>28:
        print ('Введите верное кол-во конфет (не более 28)')
    else:
        count=count-stepplayer
        if count<=0:
            print (f'Победил {oneplayer}')
            break
        print ('Остаток конфеток')
        print (count)
        if count<=28:
            print (f"{twoplayer} забирает  {count} конфет")
            count=count-count
            print (f'Победил {twoplayer}')
            break
        if count==29:
            stepbot=randint(0,28)
            print (f"{twoplayer} забирает  {stepbot} конфет")
            count=count-stepbot
            print ('Остаток конфеток')
            print (count)
        else:
            if count<58 and count>28:
                x=count-29
                count=count-x
                print (f"{twoplayer} забирает  {x} конфет")
                print ('Остаток конфеток')
                print (count)
            else:
                stepbot=randint(0,28)
                print (f"{twoplayer} забирает  {stepbot} конфет")
                count=count-stepbot
                print ('Остаток конфеток')
                print (count)