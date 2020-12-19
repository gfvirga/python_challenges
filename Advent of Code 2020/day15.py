
def speak(limit):
    file = open('./inputs/day15input.txt',mode='r')
    nums = [int(x) for x in file.read().split(",")]
    spoken = {}
    for turn, spoke in enumerate(nums):
        spoken[spoke] = [turn+1]

    turn += 2

    while turn < limit:
        if spoke in spoken:
            if len(spoken[spoke]) > 1:
                spoke = spoken[spoke][-2:][1] - spoken[spoke][-2:][0]    
            else:
                spoke = 0

            if spoke in spoken:
                spoken[spoke].append(turn)
            else:
                spoken[spoke] = [turn]

        turn += 1
    return spoke

print(f"Part One {speak(2021)}")
print(f"Part Two {speak(30000001)}")