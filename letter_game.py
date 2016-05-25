from __future__ import print_function
import random

def game():
  wordbank = ["bulbasaur", "ivysaur", "venasaur", "squirtle", "wortortle", "blastoise", "charmander", "chareleon", "charizard"]

  answer = random.choice(wordbank)
  correct = []
  incorrect = []

  while len(incorrect) < 5 and len(correct) != len(list(answer)):

    for letter in answer:
      if letter in correct:
        print(letter, end='')
      else:
        print('_', end='')
    print('')
    print(answer)

    guess = raw_input("Try to guess a letter in the mystery word. ")


    correct.append(guess)

    print(correct)




game()
