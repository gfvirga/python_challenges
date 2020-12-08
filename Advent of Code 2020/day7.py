import re
bags = {}
seen = set()
count = 0
file = open('day7input.txt',mode='r')
for line in file.read().split(".\n"):
    line = re.sub("(bags|bag)","",line)
    line = line.replace(".","")
    key, values = line.split(" contain ")
    if 'no other' in values:
        bags[key.strip()] = {}
    else:
        bags[key.strip()] = {bag: time for time, bag in (value.strip().split(" ", 1) for value in values.split(", "))}

# Part One:
def check_shiny(key):
    for k in bags[key].keys():
        print(k + ".")
        if 'shiny gold' == k:
            seen.add(bag)
            break
        check_shiny(k)

for bag in bags.keys():
    print(f"            checking bag: {bag}")
    check_shiny(bag)

print(len(seen))

# Part Two
def Count_shiny(key):
    for k in bags[key].keys():
        print(k + ".")
        if 'shiny gold' == k:
            seen.add(bag)
            break
        check_shiny(k)

for bag in bags.keys():
    print(f"            checking bag: {bag}")
    check_shiny(bag)

