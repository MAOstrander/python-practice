try:
  count = int(raw_input("Give me a number: "))
except ValueError:
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
