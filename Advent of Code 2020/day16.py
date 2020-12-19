file = open('./inputs/day16input.txt',mode='r')
block =  file.read().split("\n\n")

# Parsing stuffs
fields= {}
all_nums=[]
for line in block[0].split("\n"):
    field, ranges = line.split(": ")
    ranges = ranges.split(" or ")
    ranges = [list(range(int(x[0]),int(x[1])+1)) for x in (nums.split("-") for nums in ranges)]
    fields[field] = ranges
    all_nums += ranges

your_ticket, values = block[1].split(":\n")
your_ticket = [int(x) for x in values.split(",")]

field, values = block[2].split(":\n")
fields[field] = []
for value in values.split("\n"):
    value = [int(x) for x in value.split(",")]
    fields[field].append(value)

# Part One
counter = 0
for nums in fields['nearby tickets']:
    for num in nums:
        if not any(num in sublist for sublist in all_nums):
            counter += num

print(f"Part One {counter}")

# Part two
valid_tickets = [your_ticket]
for nums in fields['nearby tickets']:
    if all(any(num in sublist for sublist in all_nums) for num in nums):
        valid_tickets.append(nums)
        
fields.pop('nearby tickets')

# Get all possible if the columns are in the ranges {'class': [1, 2], 'row': [0, 1, 2], 'seat': [2]}
field_idx = {}
for field, ranges in fields.items():
    for idx in range(len(valid_tickets[0])):
        if all(any(num[idx] in sublist for sublist in ranges) for num in valid_tickets):
            if field in field_idx:
                field_idx[field].append(idx)
            else:
                field_idx[field]=[idx]       

    

# Sort dict hack by len - A lot of columns returned all True and index will be based on least occurance
#  {'seat': [2], 'class': [1, 2], 'row': [0, 1, 2]}
field_idx = {k: v for k, v in sorted(field_idx.items(), key=lambda item: len(item[1]))}

# Cleanup dict and make sure that used field isn't reused
# {'seat': 2, 'class': 1, 'row': 0}
used = set()
for field, idxs in field_idx.items():
    for idx in idxs:
        if idx in used: continue
        field_idx[field] = idx
        used.add(idx)

# Do the Maths if field has "departure"
result = 1
for field, idx in field_idx.items():
    if 'departure' in field:
        result *= your_ticket[idx]

print(f"Part Two: {result}")