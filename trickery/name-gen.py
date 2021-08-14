import random
def splitIntoChars(text):
  res = []
  for i in text:
    res.append(i)

chars = splitIntoChars("abcdefghijklmnopqrstuvwxyz")
print(char[random.randint(0, len(chars))])