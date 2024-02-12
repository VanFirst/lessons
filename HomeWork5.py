import random
a = 100
finish = 300
fix = 7

while 0 < a < 300:
    number = int(input('Введите число: '))
    stavka = int(input('Сделайте ставку: '))
    if a >= stavka:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        sum = first_dice + second_dice
        print(f'На первом кубике выпало: {first_dice}. \nНа втором кубике выпало: {second_dice}.\nСумма: {sum} ')
        if sum < fix and number < fix:
            a = a + stavka
            print('Win' + ' ' + str(a))
        elif sum == number:
            a = a + (stavka * 4)
            print('Win' + ' ' + str(a))
        else:
            a = a - stavka
            print('Loss' + ' ' + str(a))
        if a <= 0 or a >= 300:
            break
        else:
            x = input('Хотите продолжить? (Y или N) ')
            if x == 'N':
                print('Ссыкло!')
                break
            else:
                print('Погнали! ')
    else:
        print('Введите допустимую ставку не более ' + str(a))
if a <= 0:
    print('Ты проиграл!')
elif a > 300:
    print('Победа!')
else:
    print('Ссыкло')




