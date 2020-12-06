# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.

# Part one
highest = 0
with open('day5input.txt') as f:
    for line in f:
        row = [x for x in range(0,128)]
        col = [x for x in range(0,8)]
        for i,char in enumerate(line):
            if char == "F":
                row = row[:(len(row)//2)]
            elif char == "B":
                row = row[(len(row)//2):]
            elif char == "L":
                col = col[:(len(col)//2)]
            elif char == "R":
                col = col[(len(col)//2):]
        highest = max(highest, (row[0] * 8 + col[0]))

print(highest)

# Part Two
highest = 0
seats = {}
ids = []
with open('day5input.txt') as f:
    for line in f:
        row = [x for x in range(0,128)]
        col = [x for x in range(0,8)]
        for i,char in enumerate(line):
            if char == "F":
                row = row[:(len(row)//2)]
            elif char == "B":
                row = row[(len(row)//2):]
            elif char == "L":
                col = col[:(len(col)//2)]
            elif char == "R":
                col = col[(len(col)//2):]
        ids.append(row[0] * 8 + col[0])

# Find the open seat.     
for r, pass_id in zip(range(min(ids),max(ids)), sorted(ids)):
    if r != pass_id:
        print(r)
        break
