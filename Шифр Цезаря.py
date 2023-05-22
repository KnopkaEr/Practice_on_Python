print('Введите строку для шифрования: ', end='')
stroka = input()
print('Задайте направление. Право - 1, Лево - 2: ', end='')
napr = int(input())
print('Выберите язык. Английский - 1, Русский - 2: ', end='')
lang = int(input())
print('Задайте шаг сдвига (в числах): ', end='')
shag = int(input())

if lang == 2:
    lang_s = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

elif lang == 1:
    lang_s = 'abcdefghijklmnopqrstuvwxyz'


def sh_c(n, alfa_vit, sh, p):
    s = ''
    for i in range(len(p)):
        if p[i].lower() in alfa_vit:
            if n == 1:
                k = alfa_vit.index(p[i].lower()) + sh
                if k > len(alfa_vit):
                    m = k - len(alfa_vit)
                    if p[i] == p[i].lower():
                        s = s + alfa_vit[m]
                    else:
                        s = s + alfa_vit[m].upper()
                elif k <= len(alfa_vit):
                    if p[i] == p[i].lower():
                        s = s + alfa_vit[k]
                    else:
                        s = s + alfa_vit[k].upper()
            elif n == 2:
                k = alfa_vit.index(p[i].lower()) - sh
                if p[i] == p[i].lower():
                    s = s + alfa_vit[k]
                else:
                    s = s + alfa_vit[k].upper()

        else:
            s = s + p[i]
    print(s)


sh_c(napr, lang_s, shag, stroka)
# разобраться с английским алфавитом, шагами влево и заглавными буквамм