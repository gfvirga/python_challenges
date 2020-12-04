array = []

with open('day1input.txt') as f:
    for line in f:
        array.append(int(line))


left = 0
right = len(array)-1
array.sort()

#Two Sum
while left < right:
    sum = array[right] + array[left] 
    if sum == 2020:
        print(array[right] * array[left])
        break

    if sum > 2020:
        right -= 1
    else:
        left += 1

# Three Sum
for i in range(len(array) - 2):
    left = i + 1
    right = len(array)-1
    while left < right:
        sum = array[i] + array[right] + array[left] 
        if sum == 2020:
            print(array[i] * array[right] * array[left])
            break

        if sum > 2020:
            right -= 1
        elif sum < 2020:
            left += 1