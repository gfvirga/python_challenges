
facing = 'E'
coordinates = {
    'N': 0,
    'E': 0,
    'S': 0,
    'W': 0
}
opposite = {'N':'S','S':'N','E':'W','W':'E','R': 1 ,'L': -1,90:1,180:2,270:3,360:4}

#Part One:
file = open('day12input.txt',mode='r')
for line in file.read().split("\n"):
    action, value = [line[:1],int(line[1:])]

    if action in "F":
        coordinates[facing] += value
        coordinates[opposite[facing]] -= value
    elif action in "NESW":
        coordinates[action] += value
        coordinates[opposite[action]] -= value
    elif action in "RL":
        facing_array = list(coordinates.keys())
        facing_index = facing_array.index(facing)
        for i in range(opposite[value]):
            facing_index += 1 * opposite[action]
            if facing_index > 3:
                facing_index = 0
            if facing_index < 0:
                facing_index = 3
        facing = facing_array[facing_index]

print(max(coordinates['N'],coordinates['S']) + 
        max(coordinates['E'],coordinates['W'])
        )

facing = 'E'
waypoint = {
    'N': 1,
    'E': 10,
}
coordinates = {
    'N': 0,
    'E': 0
}

# Part Two - PLAGIARISM Alert:
file = open('day12input.txt',mode='r')
for line in file.read().split("\n"):
    action, value = [line[:1],int(line[1:])]
    print(f"{action}{value} waypoint = {waypoint}")
    if action in 'SW':
        waypoint[opposite[action]] -= value
    if action in "NE":
        waypoint[action] += value
    elif action in "F":
        coordinates['N'] += waypoint['N'] * value
        coordinates['E'] += waypoint['E'] * value

    # I looked up how other did this and I thought this was cleaver! PLAGIARISM area
    elif action in "L":
        while value:
            waypoint['N'], waypoint['E'] = waypoint['E'], -waypoint['N']
            value -= 90
    elif action in "R":
        while value:
            waypoint['N'], waypoint['E'] = -waypoint['E'], waypoint['N']
            print(waypoint)
            value -= 90

    print(coordinates)
print(abs(coordinates['N']) + abs(coordinates['E']))