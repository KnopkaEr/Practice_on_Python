import random

dig = '0123456789'
ll = 'abcdefghijklmnopqrstuvwxyz'
ul = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
p = '!#$%&*+-=?@^_.'
st_s = 'il1Lo0O'
ch = ''
k = 0
f = True

while f:
    f = True
    print('Введите количество необходимых паролей (цифрами):', end=' ')
    c = int(input())

    print('Введите длину одного пароля (цифрами):', end=' ')
    l_p = int(input())

    print('В пароле нужны цифры? (0 - если да, 1 - если нет):', end=' ')
    yn1 = int(input())
    if yn1 == 0:
        ch = ch + random.choice(dig)

    print('В пароле нужны заглавные буквы? (0 - если да, 1 - если нет):', end=' ')
    yn2 = int(input())
    if yn2 == 0:
        ch = ch + random.choice(ul)

    print('В пароле нужны строчные буквы? (0 - если да, 1 - если нет):', end=' ')
    yn3 = int(input())
    if yn3 == 0:
        ch = ch + random.choice(ll)

    print('В пароле нужны спецсимволы? (0 - если да, 1 - если нет):', end=' ')
    yn4 = int(input())
    if yn4 == 0:
        ch = ch + random.choice(p)

    print('В пароле нужны неоднозначные символы (il1Lo0O)? (0 - если да, 1 - если нет):', end=' ')
    yn5 = int(input())
    if yn4 == 0:
        ch = ch + random.choice(st_s)
    if len(ch) > l_p:
        print()
        print('Задайте такую длину пароля, чтобы влезли все желаемые символы!')
        print()
    if len(ch) <= l_p:
        f = False


def generate_password(len_p, count_p):
    for i in range(count_p):
        chars_p = ''
        while True:
            if yn1 == 0:
                chars_p = chars_p + random.choice(dig)
                if len(chars_p) == len_p:
                    chars_p = chars_p.split()
                    random.shuffle(chars_p)
                    chars_p = ''.join(chars_p)
                    print(i, '. ', chars_p, sep='')
                    break
            if yn2 == 0:
                chars_p = chars_p + random.choice(ul)
                if len(chars_p) == len_p:
                    chars_p = chars_p.split()
                    random.shuffle(chars_p)
                    chars_p = ''.join(chars_p)
                    print(i, '. ', chars_p, sep='')
                    break
            if yn3 == 0:
                chars_p = chars_p + random.choice(ll)
                if len(chars_p) == len_p:
                    chars_p = chars_p.split()
                    random.shuffle(chars_p)
                    chars_p = ''.join(chars_p)
                    print(i, '. ', chars_p, sep='')
                    break
            if yn4 == 0:
                chars_p = chars_p + random.choice(p)
                if len(chars_p) == len_p:
                    chars_p = chars_p.split()
                    random.shuffle(chars_p)
                    chars_p = ''.join(chars_p)
                    print(i, '. ', chars_p, sep='')
                    break
            if yn5 == 0:
                chars_p = chars_p + random.choice(st_s)
                if len(chars_p) == len_p:
                    chars_p = chars_p.split()
                    random.shuffle(chars_p)
                    chars_p = ''.join(chars_p)
                    print(i, '. ', chars_p, sep='')
                    break


generate_password(l_p, c)
