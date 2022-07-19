# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2

def get_num_stickers(word):
  counter = 0
  chars_available = []
  for char in word:
    if char == " ":
      continue
    if char not in chars_available:
      counter += 1
      chars_available += list("facebook")
    del chars_available[chars_available.index(char)]
  
  return counter

print(get_num_stickers('coffee kebab'))
print(get_num_stickers('book'))
print(get_num_stickers('ffacebook'))