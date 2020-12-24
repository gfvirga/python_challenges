from copy import deepcopy
file = open('./inputs/day22input.txt',mode='r')
# Print players parses to {1: [9, 2, 6, 3, 1], 2: [5, 8, 4, 7, 10]}
original_players = {int(k.split(' ')[1]): [int(x) for x in (v.split("\n")[1:] )] for k, v in [line.split(":") for line in file.read().split("\n\n")]}
players = deepcopy(original_players)

# k == winner
def game(players):
    while all(len(v) > 0 for v in players.values()):
        highest = max(players[1][0], players[2][0])
        k = 1 if (highest in players[1]) else 2
        k_o = 1 if k == 2 else 2
        value_helper = [players[k][0],players[k_o][0]]
        for key in players.keys():
            players[key].pop(0)

        players[k] += (value_helper)    
    return k, players

k, result = game(players)
print(f"Part One: {sum(x * i for i, x in enumerate(reversed(result[k]), 1))}")

players = deepcopy(original_players)
def recursive(players):
    seen = set()
    while all(len(v) > 0 for v in players.values()):
        highest = max(players[1][0], players[2][0])
        k = 1 if (highest in players[1]) else 2
        k_o = 1 if k == 2 else 2

        # Learned from sophie https://github.com/sophiebits/adventofcode/blob/main/2020/day22.py#L30
        kk = (tuple(players[1]), tuple(players[2]))
        if kk in seen:
            return 1, players
        seen.add(kk)

        value_helper = {k: players[k][0], k_o: players[k_o][0]}
        for key in players.keys():
            players[key].pop(0)
        if all(len(v) > 1 for v in players.values()):
            # Verify if it needs to recursive
            if len(players[k]) >= value_helper[k] and len(players[k_o]) >= value_helper[k_o]:
                players_helper = {k: players[k][:value_helper[k]], k_o: players[k_o][:value_helper[k_o]]}
                k, _ = recursive(players_helper)
                k_o = 1 if k == 2 else 2
                value_helper = {k: value_helper[k], k_o: value_helper[k_o]}
        players[k] += (value_helper.values())    
    return k, players

k , result = recursive(players)
print(f"Part Two: {sum(x * i for i, x in enumerate(reversed(result[k]), 1))}")