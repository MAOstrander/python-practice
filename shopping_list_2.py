from __future__ import print_function

shopping_list = []

def show_help():
  print("\nSeperate each item with a comma.")
  print("Type EXIT to quit, SHOW to see the current list, DONE to remove an item from the list, and HELP to get this message.")

def show_list():
  count = 1
  for item in shopping_list:
    print("{}: {}".format(count, item))
    count += 1

def done_with_item(gone):
  del shopping_list[gone]

print("Give me a list fo things you want to shop for.")
show_help()

while True:
  new_stuff = raw_input("> ")

  if (new_stuff == "EXIT"):
    print("\nHere's your list:")
    show_list()
    break
  elif (new_stuff == "HELP"):
    show_help()
    continue
  elif (new_stuff == "SHOW"):
    show_list()
    continue
  elif (new_stuff == "DONE"):
    show_list()
    del_index = raw_input("Which item do you want to remove? Type the number and hit enter to that item.\n You have {} item(s) in your list.".format(len(shopping_list)))
    del_index = int(del_index) - 1
    done_with_item(del_index)
    continue
  else:
    new_list = new_stuff.split(",")
    index = raw_input("Do you want to order your list? Press enter to put item at the end of list. Type a number and hit enter to put item at that spot.\n You have {} item(s) in your list.".format(len(shopping_list)))
    if index:
      place = int(index) - 1
      for item in new_list:
        shopping_list.insert(place, item.strip())
        place += 1
    else:
      for item in new_list:
        shopping_list.append(item.strip())

