# Используемые библиотеки
from random import sample

# Приветственная информация: Сегодня мы потренеруемся расшифровывать морзянку. 
print('Сегодня мы потренеруемся расшифровывать морзянку.')

# Нажмите Enter и начнем
input('Нажмите Enter и начнем\n')

# список английских слов en_words
en_words = ['hot', 'cat', 'dog', 'little', 'work', 'ocean', 'free', 'good', 'luck', 'leon', 'football', 'river']

# Словарь Морзе book_morze
book_morze = {
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", 
  "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", 
  "z": "--..",
  ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
} # the end book_morze


# Функция get_word() получает случайное слово из списка
def get_word():
    word_random = sample(en_words,1)
    print(word_random[0])
    return word_random


# Функция morse_encode() переводит слова на английском языке на азбуку Морзе.
def morse_encode():

    #получаем случайное слово используя функцию get_word(), сохраняя его в переменную word
    print('Случайным образом выпадает слово...')
    word = get_word()

    #считаем количество символов
    count_word = len(word)

    #делим случайное слово на буквы
    add_symbols = list(word[0])
    print(add_symbols)
    global morze_translate
    morze_translate = []
    #цикл перевода символов из слова word на символы из словаря book_morze
    for symbol_en in add_symbols:
        if symbol_en in book_morze.keys():
            morze_translate.append(book_morze[symbol_en])
    morze_translate = ''.join(morze_translate)
    print(morze_translate)

    return add_symbols, morze_translate


#Функция подсчета статитстики
def print_statisics():

    print(f'Всего задачек: {count_answers}')
    print(f'Ваши ответы - - - -  {answers}')
    print(f'Отвечено верно: {answer_true}')
    print(f'Отвечено неверно: {answer_false}')


#Цикл генерации слов, используя функцию и счетчики для статитстики
#используемые переменные
i = 0
answer_true = 0
answer_false = 0
count_answers = 0
answers = []

for i in range(len(en_words)):

    morse_encode()
    print()

    # Ввод ответа пользователя
    print('Введите ответ на азбуке Морзе, используя символы "-" и "." не используя пробелы')
    user_answer = input().lower()

    #считаем сколько раз пользователь ответил
    count_answers += 1

    # Сравниваем ответ пользователя
    if user_answer == morze_translate:
        print('Вы верно ответили')
        answer_true += 1
        inncorrect_answers = answers.append('True')
    else:
        print('Нет. это Не верно, у вас ошибка')
        answer_false += 1
        correct_answers = answers.append('False')





print_statisics()    

# Функция print_ststistics() на основе списка answers =[] выводит [True, False, False, True]....
#  Всего задачек: 5
#  Отвечено верно: 2
#  Отвечено неверно: 2


# Вывести статистику с помощью функции print_ststistics()

# Протестировать работу приложения