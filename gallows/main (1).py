import random
import json


HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
  /    |
       |
=========''', '''
   +---+
   |   |
   o   |
  /|\  |
  / \  |
       |
=========''']
topics = open("words.json", encoding='utf-8')
json_data = json.load(topics)

def chooseTopic(data):
    topic = random.choice(list(data.keys()))
    words = data[topic].split()
    return words, topic


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]



def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(topic)
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '*' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()



def getGuess(alreadyGuessed):
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, вводите не больше одной буквы за раз!')
        elif guess in alreadyGuessed:
            print('Вы уже пробовали эту букву. Выберите другую')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess



def playAgain():
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
gameIsDone = False
words, topic = chooseTopic(json_data)
secretWord = getRandomWord(words)

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Превосходно! Было загадано слово "' + secretWord + '"! Вы победили!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('У вас не осталось попыток!\nПосле ' + str(len(missedLetters)) + ' ошибок и ' + str(len(correctLetters)) + 'угаданных букв. Загаданное слово:' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            words, topic = chooseTopic(json_data)  #
            secretWord = getRandomWord(words)
        else:
            print("Тогда - до свидания!")
            break