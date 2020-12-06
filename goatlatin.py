# Goat Latin is a made-up language based off of English, sort of like Pig Latin.
# The rules of Goat Latin are as follows:
# 1. If a word begins with a consonant (i.e. not a vowel), remove the first
#    letter and append it to the end, then add 'ma'.
#    For example, the word 'goat' becomes 'oatgma'.
# 2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word.
#    For example, the word 'I' becomes 'Ima'.
# 3. Add one letter "a" to the end of each word per its word index in the
#    sentence, starting with 1. That is, the first word gets "a" added to the
#    end, the second word gets "aa" added to the end, the third word in the
#    sentence gets "aaa" added to the end, and so on.

# Write a function that, given a string of words making up one sentence, returns
# that sentence in Goat Latin. For example:
#
#  string_to_goat_latin('I speak Goat Latin')
#
# would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

s = "I speak Goat Latin"

r= "oatgma"

vowel = ["a","e","o","i","u"]

def translateW(s):
    s_arr = s.split('')
    found_first = False
    res = []
    
    if s_arr[0] not in vowel:
        s_arr.append(char)
        s_arr.append("ma")
        del s_arr[0]  
    elif s_arr[0] in vowel:
        s_arr.append("ma")
    
    return ''.join(s_arr)
    
def string_to_goat_latin(s):

    res = []
    for i, word in enumerate(s):
        s_helper = translateW(s)
        s_helper += "a" * i+i
        res.append(s_helper)
    return " ".join(res)

string_to_goat_latin(s)
