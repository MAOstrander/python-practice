from __future__ import print_function

shopping_list = []

def show_help():
  print("\nSeperate eah item with a comma.")
  print("Type DONE to qui, SHOW to see the current list, and HELP to get this message.")

def show_list():
  count = 1
  for item in show_list:
    print("{}: {}".format(count, item))
    count += 1

print("Give me a list fo things you want to shop for.")
show_help()

while True:
  new_stuff = input("> ")

  if new_stuff == "DONE":
    print("\nHere's your list:")
    show_list()
    break
  elif new_stuff == "HELP":
    show_help()
    continue
  elif new_stuff == "SHOW":
    show_list()
    continue
  else:
    new_list = new_stuff.split(",")
    index = input("Do you want to reorder your list? Press enter to put item at the end of list. Type a number and hit enter to put item at that spot.\n You have {} item(s) in your list.".format(len(shopping_list)))
