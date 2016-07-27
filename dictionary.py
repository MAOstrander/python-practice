my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']

def members(arg1, arg2):
    count = 0
    for thing in arg1:
      print thing
      print arg1
      print arg2
      if (thing in arg2):
        count = count + 1
    return count

answer = members(my_dict, my_list)
print answer
