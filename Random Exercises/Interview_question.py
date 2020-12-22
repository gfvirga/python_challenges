s = "I love coding while eating Pizza"
vowels = ["a","e","i","o","u"]
def translateW(w):
    s_helper = ""
    if s[0] not in vowels:
        s_helper = w[:1]
        w = w[1:] + s_helper + "ma"
    else:
        w = w + "ma"
    return w

def alienLanguage(s):
    res = []
    for i, word in enumerate(s.split()):
        res.append(translateW(word)+"a"*i)
    return res

print(alienLanguage(s))