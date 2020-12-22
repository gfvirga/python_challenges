from copy import deepcopy
file = open('./inputs/day22input.txt',mode='r')
# Print players parses to {1: [9, 2, 6, 3, 1], 2: [5, 8, 4, 7, 10]}
players = {int(k.split(' ')[1]): [int(x) for x in (v.split("\n")[1:] )] for k, v in [line.split(":") for line in file.read().split("\n\n")]}
original_players = deepcopy(players)

counter = 0
while all(len(v) > 0 for v in players.values()):
    highest = max(players[1][0], players[2][0])
    k = 1 if (highest in players[1]) else 2
    k_o = 1 if k == 2 else 2
    value_helper = [players[k][0],players[k_o][0]]
    for key in players.keys():
        players[key].pop(0)

    players[k] += (value_helper)    

print(f"Part One: {sum(x*(i+1) for i, x in enumerate(reversed(players[k])))}")