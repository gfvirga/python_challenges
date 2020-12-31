# Test
# card = 5764801
# door = 17807724

door = 15733400
card = 6408062

def loop(code):
    i = 0
    while True: 
        # if (7**i) % 20201227 == code:
        if pow(7, i, 20201227) == code:
            return i
        i +=1

print(f"Part one \nCard: {card ** loop(door) % 20201227}")
print(f"Door: {door ** loop(card) % 20201227}")

# My trash solution took forever to work. I didn't know pow()
# So I didn't solve this one... I replaced the commented out with pow() and it worked.

