from __future__ import print_function
import random
import os

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def validate(correct, incorrect, guess):
  if guess == '':
    print("Try to guess the word!")
  elif (len(guess) > 1):
    print("Please only guess a single letter")
    return False
  elif guess in correct or guess in incorrect:
    print("You've already guessed that!")
    return False
  elif not guess.isalpha():
    print("This is a letter game, please only guess letters.")
    return False
  return True

def display_game(correct, incorrect, answer, guess):
  clear()
  if validate(correct, incorrect, guess):
    return False
  print('')
  print('')
  print('')
  for letter in answer:
    if letter in correct:
      print(letter, end='')
    else:
      print('_', end='')
  print('')
  print("Bad letters: {}".format(incorrect))
  print('Incorrect Guesses: {}/5'.format(len(incorrect)))

def game():
  wordbank = ["bulbasaur", "ivysaur", "venasaur", "squirtle", "wortortle", "blastoise", "charmander", "charmeleon", "charizard"]

  answer = random.choice(wordbank)
  correct = []
  incorrect = []

  lets_play = raw_input("Press ENTER to play or Q to quit ")
  if lets_play.lower() != "q":
    while len(incorrect) < 5 and len(correct) != len(set(answer)):

      display_game(correct, incorrect, answer, "")

      guess = raw_input("Try to guess a letter in the mystery word. ").lower()
      if display_game(correct, incorrect, answer, guess):
        break

      if guess in answer:
        correct.append(guess)
        if len(correct) == len(set(answer)):
          print("You win! The word was {}!".format(answer))
          break
      else:
        incorrect.append(guess)

    else:
      print("You lost. :( The word was {}!".format(answer))




game()
