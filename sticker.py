# Example solution for an interview question

def get_num_stickers(word):
    sticker ={}
    total_full_stickers = 0

    # Buys first sticker
    sticker = buy_sticker("facebook",sticker)

    # Loops through the word for each letter
    for letter in word.replace(" ", ""):
        # If finds the letter in current sticker dictionary
        if letter in sticker:
            # Take a letter away
            sticker[letter] -= 1
            # If the letter amount available is 0 - add to the total sticker counter and buys another sticker adding to the new letter to the dictionary hash
            if sticker[letter] == 0:
                total_full_stickers += 1
                sticker = buy_sticker("facebook",sticker)
        # If not it will break
        else:
            print "Letter not in facebook"
            break

    return total_full_stickers


def buy_sticker(word, sticker):
    # Cutting the facebook word into letters and putting a dictionary
    for cut in word:
        if cut in sticker:
            sticker[cut] += 1
        else:
            sticker[cut] = 1
    return sticker


# word in question
# prints the result of get_num_stickers function
word = "coffee kebab"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "book"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "ffacebook"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "face"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "bab beef"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "cook"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"

word = "what"
print "For the word '" + word + "' need to buy " + str(get_num_stickers(word)) + " stickers!"


# Test
from collections import Counter
test = buy_sticker("facebook", {})
if test == Counter("facebook"):
    print("Tested ok")
else:
    print 1
