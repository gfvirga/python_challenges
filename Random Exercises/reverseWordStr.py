def reverseWordsInString(string):
  words = []
  reading_word = False
  reading_space = False
  word = ""

  for i, c in enumerate(string):
    if reading_word == False and reading_space == False:
      if c.isspace():
        reading_space = True
      else: 
        reading_word = True
    elif reading_space:
      if not c.isspace():
        words.append(word)
        word = ""
        reading_space = False
    elif reading_word:
      if c.isspace():
        words.append(word)
        word = ""
        reading_word = False
    word += c
    print(words)
    print(f"{word} :::")
        
  words.append(word)
  return "".join(reversed(words))

print(reverseWordsInString("AlgoExpert is the best!"))
# print(reverseWordsInString("words, separated, by,    commas"))