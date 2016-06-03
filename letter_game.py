from __future__ import print_function
import random
import os
import sys

wordbank = ["bulbasaur", "ivysaur", "venasaur", "squirtle", "wortortle", "blastoise", "charmander", "charmeleon", "charizard"]

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def display_game(correct, incorrect, answer):
  clear()
  print('Incorrect Guesses: {}/6'.format(len(incorrect)))
  print('')
  for letter in incorrect:
    print(letter, end=' ')
  print('\n\n')

  for letter in answer:
    if letter in correct:
      print(letter, end='')
    else:
      print('_', end='')
  print('')

def validate(correct, incorrect):
  while True:
    guess = raw_input("Try to guess a letter in the mystery word. ").lower()
    if guess == '':
      print("Try to guess the word!")
    elif (len(guess) > 1):
      print("Please only guess a single letter")
    elif guess in correct or guess in incorrect:
      print("You've already guessed that!")
    elif not guess.isalpha():
      print("This is a letter game, please only guess letters.")
    else:
      return guess


def game(done):
  clear()
  answer = random.choice(wordbank)
  correct = []
  incorrect = []

  while True:
    display_game(correct, incorrect, answer)
    guess = validate(correct, incorrect)

    if guess in answer:
      correct.append(guess)
      found = True
      for letter in answer:
        if letter not in correct:
          found = False
      if found:
        print("YOU WIN! ^.^")
        print("You win! The word was {}!".format(answer))
        done = True
    else:
      incorrect.append(guess)
      if len(incorrect) == 6:
        display_game(correct, incorrect, answer)
        print("You lost. :( The word was {}!".format(answer))
        done = True

    if done:
      again = raw_input("Play again? Y/n ").lower()
      if again != "n":
        return game(done=False)
      else:
        sys.exit()

def welcome():
  start = raw_input("Press any key to start or Q to quit ").lower()
  if start == "q":
    print("Bye!")
    sys.exit()
  else:
    return True

print("Welcome to Word Guesser!")
done=False

while True:
  clear()
  welcome()
  game(done)

