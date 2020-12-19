import re

counter = 0
with open('./inputs/day2input.txt') as f:
    for line in f:
        mininum, maximum, char, password = re.split('-| |: ', line)
        if int(mininum) <= password.count(char) <= int(maximum):
            #print(f" {int(mininum)} <= {password.count(char)} <= {int(maximum)}")
            counter += 1

print(f"part one: {counter}")

counter = 0
with open('./inputs/day2input.txt') as f:
    for line in f:
        position_one, position_two, char, password = re.split('-| |: ', line)
        if (char == password[int(position_one)-1]) ^ (char ==  password[int(position_two)-1]):
            counter += 1
        
print(f"part Two: {counter}")

