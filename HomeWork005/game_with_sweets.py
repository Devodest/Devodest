# 2. Создайте программу для игры с конфетами человек против человека.
#
#     Условие задачи: На столе лежит 2021 конфета. Играют
#     два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#     За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
#     a) Добавьте игру против бота
#
#     b) Подумайте как наделить бота "интеллектом"


import random

s = 241
print(f'On the table candies {s} Two players play by making a move after each other.')
print('In one move, you can pick up no more than 28 candies. ')
print('All of the opponents candies go to the one who made the last move.')
choose = int(input('If you want to play with a computer write 1, if with a player write 2: '))
while True:
    if (choose == 1) or (choose == 2):
        break
    else:
        print('Unfortunately, at the moment, only 2 modes are available.')
        choose = int(input('If you want to play with a computer write 1, if with a player write 2: '))
number_first_player = 0
number_second_player = 0
if choose == 2:
    first_player = input('Enter your name first player: ')
    second_player = input('Enter your name second player: ')
    flag = random.randrange(1, 3)
    if flag == 1:
        print('Player 1 turn')
    else:
        print('Player 2 turn')
    while s > 0:
        if flag == 1:
            if s > 0:
                print(f'Turn player №{flag} - name {first_player}, leftover candy: {s}')
                number_first_player = int(input('Enter how many sweets you want to take away: ', ))
                if (number_first_player > 0) and (number_first_player < 29):
                    s -= number_first_player
                    flag = 2
                    if s == 0:
                        print(f'{first_player} a winner')
                    elif s < 0:
                        print('More candies are introduced than necessary. try again')
                        flag = 1
                        s += number_first_player
                else:
                    print('More candies are introduced than necessary. try again')
                    flag = 1
        if flag == 2:
            if s > 0:
                print(f'Turn player №{flag} - name is {second_player}, leftover candy: {s}')
                number_second_player = int(input('Enter how many sweets you want to take away: ', ))
                if (number_second_player > 0) and number_second_player < 29:
                    s -= number_second_player
                    flag = 1
                    if s == 0:
                        print(f'{second_player}r a winner')
                    elif s < 0:
                        print('More candies are introduced than necessary. try again')
                        flag = 2
                        s += number_second_player
                else:
                    print('More candies are introduced than necessary. try again')
                    flag = 1
elif choose == 1:
    first_player = input('Enter your name: ')
    flag = random.randrange(1, 3)
    if flag == 1:
        print('Player 1 turn')
    else:
        print("turn is bot's")
    while s > 0:
        if flag == 1:
            if s > 0:
                print(f'Turn player №{flag} - name {first_player}, leftover candy: {s}')
                number_first_player = int(input('Enter how many sweets you want to take away: ', ))
                if (number_first_player > 0) and (number_first_player < 29):
                    s -= number_first_player
                    flag = 2
                    if s == 0:
                        print(f'{first_player} a winner')
                    elif s < 0:
                        print('More candies are introduced than necessary. try again')
                        flag = 1
                        s += number_first_player
                else:
                    print('More candies are introduced than necessary. try again')
                    flag = 1

        if flag == 2:
            if s > 0:
                print(f'Turn player №{flag} - name is bot, leftover candy: {s}')
                number_second_player = s % 29
                if number_second_player == 0:
                    number_second_player = random.randrange(1, 29)
                    if number_second_player > s:
                        number_second_player = s
                print(number_second_player)
                s -= number_second_player
                flag = 1
                if s == 0:
                    print('Bot a winner')
