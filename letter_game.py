from __future__ import print_function
import random
import os

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def display_game(correct, incorrect, answer):
  clear()
  print('')
  print('')
  print('')
  for letter in answer:
    if letter in correct:
      print(letter, end='')
    else:
      print('_', end='')
  print('')
  print('Incorrect Guesses: {}/5'.format(len(incorrect)))

def game():
  wordbank = ["bulbasaur", "ivysaur", "venasaur", "squirtle", "wortortle", "blastoise", "charmander", "chareleon", "charizard"]

  answer = random.choice(wordbank)
  correct = []
  incorrect = []

  lets_play = raw_input("Press ENTER to play or Q to quit ")
  if lets_play.lower() != "q":
    while len(incorrect) < 5 and len(correct) != len(set(answer)):

      display_game(correct, incorrect, answer)

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
        if len(correct) == len(set(answer)):
          print("You win! The word was {}!".format(answer))
          break
      else:
        incorrect.append(guess)

    else:
      print("You lost. :( The word was {}!".format(answer))




game()
