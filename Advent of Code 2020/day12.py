
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

    print(coordinates)
print(max(coordinates['N'],coordinates['S'])+ 
        max(coordinates['E'],coordinates['W'])
        )

facing = 'E'
waypoint = {
    'N': 10,
    'E': 1,
    'S': -10,
    'W': -1
}

# Part Two:
file = open('day12input.txt',mode='r')
for line in file.read().split("\n"):
    action, value = [line[:1],int(line[1:])]
    print(f"{action}{value} - Facing: {facing} ")

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
            print(f"b {facing_index}")
            if facing_index > 3:
                facing_index = 0
            if facing_index < 0:
                facing_index = 3
            print(facing_index)
        print(f"originally {facing} turned {opposite[value]*opposite[action]}")
        facing = facing_array[facing_index]

    print(coordinates)
print(max(coordinates['N'],coordinates['S'])+ 
        max(coordinates['E'],coordinates['W'])
        )