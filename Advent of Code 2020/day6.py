# Part one
questions_count = 0
file = open('./inputs/day6input.txt',mode='r')
for line in  file.read().split("\n\n"):
    line = line.replace("\n", "")
    questions_count += len(set(line))
    
print("Part One")
print(f"Questions Count: {questions_count}\n")


# Part Two
questions_count = 0
file = open('./inputs/day6input.txt',mode='r')
for line in  file.read().split("\n\n"):
    line = line.split("\n")
    line.sort()
    for char in line[-1]:
        if all(char in question for question in line):
            questions_count += 1    
print("Part Two")
print(f"Questions Count: {questions_count}\n")


# Part Two using set()
questions_count = 0
file = open('./inputs/day6input.txt',mode='r')
for line in  file.read().split("\n\n"):
    line = line.split("\n")
    for char in set(s for x in line for s in x):
        if all(char in question for question in line):
            questions_count += 1    
print("Part Two")
print(f"Questions Count: {questions_count}\n")
