import operator
file = open('day13input.txt',mode='r')
timestamp, buses = file.read().split("\n")
timestamp = int(timestamp)
buses = { int(x) :i for i, x in enumerate(buses.split(",")) if x.isdigit()}

closest_times = {}
for bus in buses.keys():
    bus_time = 0
    while True:
        bus_time += bus
        if bus_time >= timestamp:
            closest_times[bus] = bus_time
            break

next_bus = min(closest_times.items(), key=operator.itemgetter(1))[0]
print(f"Part One: {(closest_times[next_bus] - timestamp) * next_bus}" )

t = 0
next_time = {bus:0 for bus in buses.keys()}
while True:
    for bus in buses.keys():
        if t == next_time[bus]:
            next_time[bus] += bus
    t = min(next_time.values())
    if all(next_time[bus] == t + buses[bus] for bus in buses.keys() ):
        print(f"Part Two: {t}")
        break