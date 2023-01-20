# Cоздайте программу для игры в ""Крестики-нолики"".
from random import randint

print('Игра в крестики нолики!')
print('Ваш знак Х')
print('Знак бота O')

oneplayer = ('Игрок')
twoplayer = ('ivan botavich')

i = randint(0, 1)
if i == 0:
    print(f"Первый ходит {oneplayer}")
if i == 1:
    print(f"Первый ходит {twoplayer}")

a = [1, 2, 3,4, 5, 6,7, 8, 9]

def print_pole(x):
    print (x[0],' | ',x[1],' | ',x[2])
    print('-'*14)
    print(x[3],' | ',x[4],' | ',x[5])
    print('-'*14)
    print(x[6],' | ',x[7],' | ',x[8])

print_pole(a)

def check_win_i_b(x):
    vic = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    vic_i=0
    for i in vic:
        if x[i[0]] == "X" and x[i[1]] == "X" and x[i[2]] == "X":
            vic_i=1
        if x[i[0]] == "O" and x[i[1]] == "O" and x[i[2]] == "O": 
            vic_i=2
    return vic_i

        
def check_free_i(step):
    while True:
        if a[step-1]=='X' or a[step-1]=='O':
            print ('Выберите другое поле!')
            step=int(input())
        else:
            return step

def check_free_b(stepbot):
    while True:
        if a[stepbot]=='X' or a[stepbot]=='O':
            stepbot=randint(0,8)
        else:
            return  stepbot


while True: 
    if i==0:
        print (f'Ходит {oneplayer}')
        print ('Введите значение от 1 до 9')
        step=int(input())
        step=check_free_i(step)
        a[step-1]='X'
        print_pole(a)
        c=check_win_i_b(a)
        if c==1:
            print(f'Победил {oneplayer}')
            break
        i=1
    if i==1 :
        print (f'Ходит {twoplayer}')
        stepbot=randint(0,8)
        stepbot=check_free_b(stepbot)
        a[stepbot]='O'
        print_pole(a)
        c=check_win_i_b(a)
        if c==2:
            print(f'Победил {twoplayer}')
            break
        i=0
        