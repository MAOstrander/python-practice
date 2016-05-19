item = None
shoplist = []

def show_me(currentlist):
  print("")
  print("You need to get these:")
  for thing in currentlist:
    print(thing)

def instructions():
  print("")
  print("Type in the items you need from the store, hitting the 'Return' key after each.")
  print("Enter 'SHOW' to see your current list.")
  print("Enter 'HELP' to view these instructions again")
  print("Enter 'DONE' to finish the list and display")
  print("")

def add_item(thing):
  shoplist.append(thing)
  print("Added {} to list, you have {} things to get.".format(thing, len(shoplist)))


instructions()
print("What do you need from the store?")

while True:
  item = raw_input("=> ")

  if (item == "DONE"):
    break
  elif (item == "SHOW"):
    show_me(shoplist)
  elif (item == "HELP"):
    instructions()
  else:
    add_item(item)

#After we're out of the list show the list
show_me(shoplist)
