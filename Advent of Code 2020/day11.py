import copy
file = open('day11input.txt',mode='r')
seats = [list(line) for line in file.read().split("\n")]
directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def visualize(matrix):
    occupied_total = 0
    for row in range(len(matrix)):
        print(''.join(matrix[row]))
        occupied_total += matrix[row].count('#')
    print("\n")
    return occupied_total

# Part One
def count_adj(x, y, max_row, max_col):
    cockupy = 0
    for direction in directions:
        dx, dy = direction
        sum_x = sum([x,dx])
        sum_y = sum([y,dy])
        if sum_x < 0  or sum_y < 0: 
            continue
        if sum_x > max_row or sum_y > max_col:
            continue
        if seats[sum_x][sum_y] == "#":
            cockupy += 1
    return cockupy

# Everyone taking seats
while True:
    seats_helper = copy.deepcopy(seats)
    # visualize(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == ".": continue
            count = count_adj(row,col,len(seats)-1,len(seats[0])-1)
            if seats[row][col] == "#" and count > 3:
                seats_helper[row][col] = "L"
            if count == 0 and seats[row][col] == "L":
                seats_helper[row][col] = "#"

    if seats_helper == seats:
        print(f"Part One: {visualize(seats)}")
        break
    seats = copy.deepcopy(seats_helper)

# Part Two NOT SOLVED YET

file = open('day11input.txt',mode='r')
seats = [list(line) for line in file.read().split("\n")]

# Everyone taking seats
while True:
    seats_helper = copy.deepcopy(seats)
    # visualize(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == ".": continue
            count = count_adj(row,col,len(seats)-1,len(seats[0])-1)
            if seats[row][col] == "#" and count > 4:
                seats_helper[row][col] = "L"
            if count == 0 and seats[row][col] == "L":
                seats_helper[row][col] = "#"
    visualize(seats)
    if seats_helper == seats:
        print(f"Part Two: {visualize(seats)}")        
        break
    seats = copy.deepcopy(seats_helper)