from random import randrange


def bot_do():
    global balance
    while True:
        temp = rand_box_bot()
        if temp < balance:
            break
    balance -= temp


def player_output(temp):
    text = ''
    if balance > 0:
        player_do(temp)
        text += f'Осталось {str(balance)} конфет\nБот конфеты взял, '
    else:
        return 'Конфеты кончились, победил Бот'
    if balance > 0:
        bot_do()
        text += f'\n\nОсталось {str(balance)} конфет\nТвой ход, сколько возьмешь?'
    else:
        return 'Конфеты кончились, победил Ты'
    return text


def bot_output(temp):
    text = ''
    if balance > 0:
        bot_do()
        text += f'Бот конфеты взял,\n'
    else:
        return 'Конфеты кончились, Ты победил'
    if balance > 0:
        player_do(temp)
        text += f'\nОсталось {str(balance)} конфет\nТвой ход, сколько возьмешь?\n'
    else:
        return 'Конфеты кончились, победил Ты'
    return text


def player_do(num):
    global balance
    if 0 < num < 11:
        balance -= num
    else:
        return 'Столько брать нельзя'


def rand_box_bot():
    global balance
    while True:
        box = randrange(1, 11)
        if box <= balance:
            break
    return box

balance = 50