import random

# Generate a number between 1-10
answer = random.randint(1, 10)
print(answer)

while True:

#   # Let the player guess a number
  guess = int(raw_input("Guess a number between 1 and 10: "))

#   # Compare the guess to the random number
  if guess==answer:
    break
  elif guess > answer:
  # Let the player the result of the comparison
    print("Sorry, your guess was too high. Try again.")
  elif guess < answer:
    print("Sorry, your guess was too low. Try again.")


print("You got it!!!")
