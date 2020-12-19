import re
bags = {}
seen = set()
count = 0
file = open('./inputs/day7input.txt',mode='r')
for line in file.read().split(".\n"):
    line = re.sub("(bags|bag)","",line)
    line = line.replace(".","")
    key, values = line.split(" contain ")
    if 'no other' in values:
        bags[key.strip()] = {}
    else:
        bags[key.strip()] = {bag: int(time) for time, bag in (value.strip().split(" ", 1) for value in values.split(", "))}

# Part One:
def check_shiny(key):
    for k in bags[key].keys():
        #print(k + ".")
        if 'shiny gold' == k:
            seen.add(bag)
            break
        check_shiny(k)

for bag in bags.keys():
    #print(f"            checking bag: {bag}")
    check_shiny(bag)

print(f"Part One: {len(seen)}")


count = 0
# Part Two
def count_shiny(key):
    global count
    count += sum(bags[key].values())
    for bag, times in bags[key].items():
        for _ in range(times):
            count_shiny(bag)

count_shiny('shiny gold')
print(f"Part Two: {count}")
