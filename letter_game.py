import random

def game():
  wordbank = ["bulbasaur", "ivysaur", "venasaur", "squirtle", "wortortle", "blastoise", "charmander", "chareleon", "charizard"]

  answer = random.choice(wordbank)
  correct = []
  incorrect = []

  while len(incorrect) < 5 and len(correct) != len(list(answer)):

    print(answer)

    guess = raw_input("Try to guess a letter in the mystery word. ")


    correct.append(guess)

    print(correct)




game()
