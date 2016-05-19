item = None
shoplist = []

def show_me(currentlist):
  print("")
  print("You need to get these:")
  for thing in currentlist:
    print(thing)

def instructions():
  print("Type in the items you need from the store, hitting the 'Return' key after each.")
  print("Enter 'SHOW' to see your current list.")
  print("When you are done with your list enter 'DONE'")
  print("Enter 'HELP' to view these instructions again")
  print("")


instructions()
while True:
  item = raw_input("What do you need from the store? ")

  if (item == "DONE"):
    break
  elif (item == "SHOW"):
    show_me(shoplist)
  elif (item == "HELP"):
    instructions()
  else:
    shoplist.append(item)

#After we're out of the list show the list
show_me(shoplist)
