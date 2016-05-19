name = input("What is your name? ")
msg = "Hello World!"
output = name + " says: " + msg
print(output)

# del output
output = None

things = ["yay", "yes", "no", "nope"]

for thing in things:
  print(thing)

def check_message_status():
  if bool(output) == False:
    print("What happened to my message?")
  elif output:
    print("I already said something")
  else:
    print("How did you get here?")

check_message_status()
