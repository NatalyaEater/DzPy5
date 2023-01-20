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

a = [1, 1, 1,
    1, 1, 1,
    1, 1, 1]


if i==1:
    print ('Введите значение от 1 до 9')
    step=int(input())
    a[step-1]='X'
if i==0:
    stepbot=randint(0,8)
    a[stepbot]='O'
    
    
  