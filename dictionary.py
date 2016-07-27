my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']

# Count the number of items that overlap between a dictionary and list
def members(dictArg, listArg):
    count = 0
    for thing in dictArg:
      print thing
      print dictArg
      print listArg
      if (thing in listArg):
        count = count + 1
    return count

answer = members(my_dict, my_list)
print answer

# give a count of how many times each word appears in a sentence
def word_count(stringArg):
    counted_words = {}
    word_list = stringArg.split()
    for word in word_list:
        if (word in counted_words):
            counted_words[word] = counted_words[word] + 1
        else:
            counted_words[word] =  1

    return counted_words
