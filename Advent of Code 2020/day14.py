file = open('./inputs/day14input.txt',mode='r')
mem = {}
for line in file.read().split("\n"):
    if "mask" in line:
        mask = line.split(" = ")[1]
        continue
    else:
        mem_helper, value = line.split(" = ")
        mem_helper = mem_helper.replace("[",",")
        mem_helper = mem_helper.replace("]","")
    # Convert Value to binary 36b
    value = f'{int(value):036b}'

    # Verify if mask modifies value
    for i in range(len(value)):
        if mask[i] == 'X' or mask[i] == value[i]: continue
        else:
            value = value[:i] + mask[i] + value[i+1:]
    # Allocate to Memory
    mem[mem_helper.split(",")[1]] = int(str(value),2)
    
print(f"Part One: {sum(mem.values())}")


# Part Two
mem = {}
file = open('./inputs/day14input.txt',mode='r')
for line in file.read().split("\n"):
    if "mask" in line:
        mask = line.split(" = ")[1]
        continue
    else:
        mem_helper, value = line.split(" = ")
        mem_helper = mem_helper.replace("[",",")
        mem_helper = mem_helper.replace("]","")
        value = int(value)
    # Convert Value to binary 36b
    address = f'{int(mem_helper.split(",")[1]):036b}'
    address_helper = []
    for a, m in zip(address,mask):
        if m == 'X' or m == a:
            address_helper.append(m)
        else: 
            address_helper.append("1")
    
    # print(mask)

    first_x = address_helper.index('X') -1
    replaces = ["1","0"]
    clean_address = address_helper.copy()
    for num in range(0, 2**address_helper.count('X')):
        bin_num = bin(num)[2:].zfill(address_helper.count('X'))
        
        for char in bin_num:
            address_helper[address_helper.index('X')] = char
        
        mem[(''.join(address_helper))] = value
        address_helper = clean_address.copy()
        

# print('\n'.join(mem.keys()))
print(f"Part Two: {sum(mem.values())}")