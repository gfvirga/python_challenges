# Part One
skip = 1
position = 3
counter = 0
projector = 1
with open('day3input.txt') as f:
    for line in f:
        line = list(line.strip())
        if skip < 0:
            skip -= 1
            #print((''.join(line)))
            continue
        if position >= len(line):
            position -= len(line)
        if line[position] == ".":
           line[position] = "X"
        elif line[position] == "#":
            line[position] = "O"
            counter += 1
        position += 3
        #print(''.join(line))
print(counter)




# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.


#Part Two
counter = 0
result = 1
for position, skip in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    position_helper = position
    skip_helper = skip
    with open('day3input.txt') as f:
        for line in f:
            line = list(line.strip())
            if skip > 0:
                skip -= 1
                print((''.join(line)))
                continue
            else:
                skip = skip_helper -1
            if position >= len(line):
                position -= len(line)
            if line[position] == ".":
               line[position] = "X"
            elif line[position] == "#":
                line[position] = "O"
                counter += 1
            position += position_helper
            print(''.join(line))
    result *= counter
    print(counter)
    counter = 0
print(result)

