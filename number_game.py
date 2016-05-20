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

  # Let the player the result of the comparison
  print("Sorry, try again.")

print("You got it!!!")
