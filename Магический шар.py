import random
import sys

v = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
     'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
     'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
     'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
f = False
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print("Тебя зовут...", end=' - ')
name = input()
print('Привет,', name, '!')
while True:
    print('Я смогу ответить на любой твой вопрос,', name, ". Спрашивай:")
    q = input()
    print(random.choice(v))
    print('Если ответ не достаточен для тебя, можешь спросить еще что-то! Спрашиваем?', 'Y/N?')
    f = True
    while f:
        r = input()
        if r == 'Y':
            f = False
        elif r == 'N':
            print('Возвращайся если возникнут вопросы!')
            sys.exit()
        else:
            print('Я не понял ответа!.. Y//N?')
