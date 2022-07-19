

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
chars = list(characters)

def test():
  for char in document:
    if char in chars:
      del chars[chars.index(char)]
    else: 
      return False

  return True

print(test())