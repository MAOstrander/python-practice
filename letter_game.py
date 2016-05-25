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
    print('Incorrect Guesses: {}/5'.format(len(incorrect)))
    print('')

    guess = raw_input("Try to guess a letter in the mystery word. ").lower()

    if (len(guess) != 1):
      print("Please only guess a single letter")
      continue
    elif guess in correct or guess in incorrect:
      print("You've already guessed that!")
      continue
    elif not guess.isalpha():
      print("This is a letter game, please only guess letters.")
      continue

    if guess in answer:
      correct.append(guess)
    else:
      incorrect.append(guess)

    print(correct)




game()
