import random
words = ['ВОДКА', 'КОМПЬЮТЕР', 'ТЕЛЕФОН', 'МУЗЫКА', 'КОЛЕСО', 'ДОМОФОН', 'БАНАН', 'ШАПКА', 'КОФЕМОЛКА', 'КАРАНДАШ',
         'АНАНАС', 'АВТОБУС', 'КАЧЕЛИ', 'РЕЖИМ', 'РАДИО', 'КЛАВИАТУРА', 'КОШКА', 'СОБАКА', 'ТЕЛЕВИЗОР', 'РЕСПУБЛИКА',
         'МЕЛОЧЬ', 'ГОРНОЛЫЖНЫЙ', 'КОСМОНАВТ', 'РЕСТОРАН', 'МОРОЖЕНОЕ', 'ЧУГУН', 'ДУХОВКА', 'ДОЛЖНОСТЬ', 'КВАРТИРА',
         'КОНТРОЛЬ', 'ПРОГРАММА', 'СТРУКТУРА', 'ОСОБЕННОСТЬ', 'УСЛОВИЕ', 'РЕСУРС', 'АКЦИЯ', 'ТЕРРИТОРИЯ', 'РАЗВИТИЕ',
         'МАСТЕРСТВО', 'ЗАДАЧА', 'МАТЕРИАЛ', 'ПРОЦЕСС', 'ФИЛОСОФИЯ', 'ШКОЛА', 'НАБЛЮДЕНИЕ', 'ИННОВАЦИЯ', 'БИБЛИОТЕКА',
         'ПЕРСПЕКТИВА', 'КОМПЬЮТЕР', 'ВЛИЯНИЕ', 'СИСТЕМА', 'ФУНКЦИЯ', 'КОМПОНЕНТ', 'ПРИНЦИП', 'КОМПЕТЕНТНОСТЬ',
         'ГРАДИЕНТ', 'ФОРМАТ', 'РЕКЛАМА', 'КОНКУРЕНТ', 'ОБЪЕКТ', 'ОПЕРАЦИЯ', 'РАЗНООБРАЗИЕ', 'ЭФФЕКТ', 'СООТВЕТСТВИЕ',
         'СЛОЖНОСТЬ', 'ДИФФЕРЕНЦИАЛ', 'ВЕРОЯТНОСТЬ', 'ПОВЕДЕНИЕ', 'ДОКУМЕНТ', 'КОМПЛЕКС', 'ДЕЙСТВИТЕЛЬНОСТЬ',
         'КАТЕГОРИЯ', 'КОМПЕНСАЦИЯ', 'СПЕЦИАЛИСТ', 'ИНФОРМАЦИЯ']
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_word():
    return random.choice(words)

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


ura = '(✯◡✯)'


def play(word):
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print()
    print(display_hangman(tries))
    print()
    print('Попыток:', tries)
    print(*word_completion, sep='')

    while tries > 0:
        print('Введите букву или слово целиком: ', end='')
        s_user = input().upper()
        if s_user in guessed_words or s_user in guessed_letters:
            print('Где то я уже такое слышал! (◕‿◕) Введи то, чего еще не было: ')
            continue
        else:
            if len(s_user) > 1:
                guessed_words.append(s_user)
                guessed = False
                for j in range(len(s_user)):
                    if s_user[j] not in alf:
                        guessed = True
                    else:
                        continue
                if guessed:
                    print('Нельзя вводить ничего, кроме букв! :)')
                    continue
                if s_user == word:
                    print('Поздравляем, вы угадали слово! Вы победили!', ura)
                    print(word)
                    break
                elif s_user != word:
                    tries = tries - 1
                    print("Попытка потрачена! Осталось", tries, end=' ')
                    if tries == 5:
                        print('попыток')
                    elif 2 <= tries <= 4:
                        print('попытки')
                    elif tries == 1:
                        print('попытка')
                    print(display_hangman(tries))
                    continue
            elif len(s_user) == 1:
                guessed_letters.append(s_user)
                if s_user not in alf:
                    print('Нельзя вводить ничего, кроме букв! :)')
                    continue
                if s_user in word:
                    for i in range(len(word)):
                        if word[i] == s_user:
                            word_completion[i] = s_user
                            temp = ''.join(word_completion)
                    print(temp)
                    if temp == word:
                        print('Поздравляем, вы угадали слово! Вы победили!', ura)
                        break
                    else:
                        continue
                else:
                    tries = tries - 1
                    print("Попытка потрачена! Осталось", tries, end=' ')
                    if tries == 5:
                        print('попыток')
                    elif 2 <= tries <= 4:
                        print('попытки')
                    elif tries == 1:
                        print('попытка')
                    print(display_hangman(tries))
                    print(temp)
                    continue
    if tries == 0:
        print('А слово было простое: ', word)


play(get_word())
print('Сыграем еще разок? (Да/Нет): ')
answer = input().lower()
if answer == 'да':
    play(get_word())
elif answer == 'нет':
    print('Возвращайся еще! Пока! ٩(｡•́‿•̀｡)۶')
else:
    print('Я не понял ответа ╮( ˘ ､ ˘ )╭ Но если захочешь еще раз сыграть, ты знаешь где меня найти!')


