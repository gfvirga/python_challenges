import copy
file = open('day11input.txt',mode='r')
seats = [list(line) for line in file.read().split("\n")]
directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def visualize(matrix):
    for row in range(len(matrix)):
        print(''.join(matrix[row]))

def count_adj(x, y, max_row, max_col):
    cockupy = 0
    for direction in directions:
        dx, dy = direction
        sum_x = sum([x,dx])
        sum_y = sum([y,dy])
        #print(f"[{sum_x}][{sum_y}]")
        if sum_x < 0  or sum_y < 0: 
            # print(f"0")
            continue
        if sum_x > max_row or sum_y > max_col:
            # print(f"0")
            continue
        # print(f"[{sum_x}][{sum_y}] {seats[sum_x][sum_y]}")
        if seats[sum_x][sum_y] == "#":
            # print(f" #")
            cockupy += 1
    # print(cockupy)
    return cockupy

# Everyone came in to seat
for _ in range(2):
    seats_helper = copy.deepcopy(seats)
    visualize(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == ".": continue
            count = count_adj(row,col,len(seats)-1,len(seats[0])-1)
            # print(f"r {row}c {col} count {count}")
            if seats[row][col] == "#" and count > 3:
                seats_helper[row][col] = "L"
            if count == 0 and seats[row][col] == "L":
                seats_helper[row][col] = "#"
    visualize(seats)
    print("yo")
    visualize(seats_helper)
    print('--end-')
    
    seats = copy.deepcopy(seats_helper)



