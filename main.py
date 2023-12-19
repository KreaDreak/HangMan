import os
import random

clear = lambda: os.system('cls')

print('Привет, ты попал на интереснейшую игру под названием \'Виселица\'!')
print('Я загадал слово, а твоя задача отгадать его по буквам!')
input('Нажми *Enter*, чтобы продолжить!')
print('Игра НАЧАЛАСЬ!!!!!!!!')
clear()

words = ['огурчик', 'помидор', 'лук', 'чеснок', 'батарейка', 'меллер']
word = random.choice(words)
isWin = True
hp = 10
letters = []

while hp > 0:
    isWin = True

    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Победа!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)

    clear()

    if letter not in word:
        hp = hp - 1

        print('осталось попыток: ', hp)

    if hp == 0:
        print('Проиграл')

