# if в какой-то степени главнее elif
'''
a = 2
b = 5
if a < 3 < b and a == 3:
    print('Верно')
else:
    print('Ты шо ахуэл?')
'''

'''
T = float(input('Введите температуру на улице: '))
if  T <= -30:
    print('Супер холодно')
elif -30 < T <= -15:
    print('холодно')
elif -15 < T <= 0:
    print('\'так\nсебе\'')
elif 0 < T <= 15:
    print('сойдёт')
elif 15 < T <= 30:
    print('хорошо')
else:
    print('жарко')
'''
'''
number = float(input('Введите число: '))
if number >= 0:
    if number == 0:
        print('Ноль')
    else: print('число положительное')
else:
    print('число отрицательное')
'''

'''
x = 0.1
while x < 1: # Пока
    print(round(x, 2))
    x += 0.1
'''
'''
list = [1, 2, 3, 4, 'hello']
for i in list: # Для i в ...
    print(i)
'''

import random

first_dice = random.randint(1, 6)
second_dice = random.randint(1, 6)
sum = first_dice + second_dice
if sum > 11:
    print('Пуша топ')
print(f'На первом кубике выпало: {first_dice}. \nНа втором кубике выпало: {second_dice}.\nСумма {sum} ')

while True:
    x = input('Хотите продолжить? ')
    if x == 'нет':
        print('пока')
        break
    else:
        print('А ты смельчак! ')

