import random
def splitIntoChars(text):
  res = []
  for i in text:
    res.append(i)
  return res

chars = splitIntoChars("abcdefghijklmnopqrstuvwxyz")
print(chars[random.randint(0, len(chars) - 1)])