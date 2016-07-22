test_words = ["When", "I", "was", "a", "young", "warthog"]
vowels = list('aeiou')
answer = []

for word in test_words:
  letters = list(word.lower())

  for vowel in vowels:
    while True:
      try:
        letters.remove(vowel)
      except:
        break
  answer.append(''.join(letters))

print answer
