name = "Mathew Ostrander"
msg = "Hello World!"
output = name + " says: " + msg
print(output)

# del output

if bool(output) == False:
  print("What happened to my message?")
elif output:
  print("I already said something")
else:
  print("How did you get here?")
