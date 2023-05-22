import random
import sys

n = random.randrange(1, 101)
fl = True
print('Добро пожаловать в числовую угадайку')


def is_valid(s):
    cif = '0123456789'
    f = True
    for i in range(len(s)):
        if not f:
            break
        elif s[i] not in cif:
            f = False
    if not f or 1 > int(s) > 100:
        return False
    else:
        return True


while True:
    print("Угадайте число от 1 до 100:")
    st = input()
    if is_valid(st) and int(st) < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif is_valid(st) and int(st) > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif is_valid(st) and int(st) == n:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        fl = False
        sys.exit()
    elif not is_valid(st):
        print('А может быть все-таки введем целое число от 1 до 100?')
