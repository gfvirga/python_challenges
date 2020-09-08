# Example solution for an interview question
# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.

def get_num_stickers(word):
    sticker = {}
    total_full_stickers = 0
    
    # Buy a sticker
    def buy_sticker():
        # Cutting the facebook word into letters and putting a dictionary
        for cut in "facebook":
            if cut in sticker:
                sticker[cut] += 1
            else:
                sticker[cut] = 1

    # Buys the first sticker
    buy_sticker()

    # Loops through the word for each letter
    for letter in word.replace(" ", ""):
        # If finds the letter in current sticker dictionary
        if letter in sticker:
            # Take a letter away
            sticker[letter] -= 1
            # If the letter amount available is 0 - add to the total sticker counter and buys another sticker adding to the new letter to the dictionary hash
            if sticker[letter] == 0:
                total_full_stickers += 1
                buy_sticker()
        # If not it will break
        else:
            print "Letter not in facebook"
            break

    return total_full_stickers

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
