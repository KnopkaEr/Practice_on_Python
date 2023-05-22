timur, ruslan = input(), input()
b, k, ya, sp, n = ['ящерица', 'ножницы'], ['бумага', 'Спок'], ['камень', 'ножницы'], ['ящерица', 'бумага'], ['камень', 'Спок']
v = ['бумага', 'камень', 'ящерица', 'Спок', 'ножницы']
t = v.index(timur)
r = v.index(ruslan)
if (t == 0 and ruslan in b) \
        or (t == 1 and ruslan in k) \
        or (t == 2 and ruslan in ya) \
        or (t == 3 and ruslan in sp) \
        or (t == 4 and ruslan in n):
    print('Руслан')
elif (r == 0 and timur in b) \
        or (r == 1 and timur in k) \
        or (r == 2 and timur in ya) \
        or (r == 3 and timur in sp) \
        or (r == 4 and timur in n):
    print('Тимур')
else:
    print('ничья')