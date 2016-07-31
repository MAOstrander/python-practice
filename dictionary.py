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

string_dict = {"name": "Mathew", "location": "Tennessee", "job": "Teaching Assistant"}
test_output = "My name is {name} and I am a {job} in {location}."

print test_output.format(**string_dict)

# Take a list of dictionaries and format a string for each, returning a new list of strings
dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

stringo = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(list_of_dicts, sample_string):
  new_thing = []
  for listo in list_of_dicts:
    new_thing.append(sample_string.format(**listo))
  return new_thing

yarp = string_factory(dicts, stringo)
print yarp

# Create a function named most_classes that takes a dictionary of teachers. Each key is a teacher's name and their value is a list of classes they've taught. most_classes should return the teacher with the most classes.

test_classes = {'Mathew Ostrander':['Node'],'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

def most_classes(teachers):
  longest = 0
  most_productive = 'null'
  for person in teachers:
    if len(teachers[person]) > longest:
      longest = len(teachers[person])
      most_productive = person
  return most_productive

# Create a function named num_teachers that takes the same dictionary of teachers and classes. Return the total number of teachers.
def num_teachers(also_teachers):
  count = 0;
  for person in also_teachers:
    count+=1
  return count # or len(also_teachers)

# Create a function named stats that takes the teacher dictionary. Return a list of lists in the format [<teacher name>, <number of classes>].
def stats(still_teachers):
  stat_list = []
  for person in still_teachers:
    stat_list.append([person, len(still_teachers[person])])
  return stat_list

# Write a function named courses that takes the teachers dictionary. It should return a single list of all of the courses offered by all of the teachers

def courses(errything):
  all_classes = []
  for course in errything.values():
    all_classes.extend(course)
  return " ".join(all_classes)

answer = courses(test_classes)
print answer
