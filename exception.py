try:
  count = int(input("Give me a number: "))
except NameError:
  print("That's not a number!")
else:
  print("Hi "*count)


def add(twone, twtwo):
  try:
    twone = float(twone)
    twtwo = float(twtwo)
  except ValueError:
    return None
  else:
    return float(twone) + float(twtwo)
