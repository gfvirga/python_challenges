

file = open('day8input.txt',mode='r')
line = [line.split() for line in  file.read().split("\n")]

accumulation = 0
visited = set()
i = 0
while i not in visited:
    visited.add(i)
    instruction, num = line[i]
    if instruction == 'nop': 
        i += 1
        continue
    elif instruction == 'jmp':
        i += int(num)
    elif instruction == 'acc':
        i += 1
        accumulation += int(num)
print(f"Part One: {accumulation}")

switch = 0
for switch in range(1,len(line)):
    accumulation = 0
    visited = set()
    i = 0
    broke = False
    while i not in visited:
        #print(line[i])
        visited.add(i)
        instruction, num = line[i]
        if switch == i:
            if instruction == 'jmp':
                instruction = 'nop'
            elif instruction == 'nop':
                instruction = 'jmp'
        if instruction == 'nop': 
            i += 1
            continue
        elif instruction == 'jmp':
            i += int(num)
        elif instruction == 'acc':
            i += 1
            accumulation += int(num)
        if i == len(line):
            broke = True
            break
    if broke:
        break

print(f"Part Part Two: {accumulation}")