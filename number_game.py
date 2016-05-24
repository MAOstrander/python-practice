import random

def game():
  # Generate a number between 1-10
  answer = random.randint(1, 10)
  guesses = []

  while len(guesses) < 5:

    # Let the player guess a number
    guess = raw_input("Guess a number between 1 and 10: ")

    try:
      guess = int(guess)
      # Compare the guess to the random number
      if guess < 1 or guess > 10:
        print("Hey, something between 1 and 10 please!")

      elif guess==answer:
        print("You got it!!!")
        break
      elif guess > answer:
      # Let the player the result of the comparison
        print("Sorry, your guess was too high. Try again.")
      elif guess < answer:
        print("Sorry, your guess was too low. Try again.")
      guesses.append(guess)
    except ValueError:
      print("That's not a number!")
  else:
    print("You lost!")

  play_again = raw_input("Do you want to play again? Y/n ")
  if play_again.lower() != 'n':
    game()



game()
