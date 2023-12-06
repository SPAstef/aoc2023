def part1():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    times = list(map(int, lines[0][lines[0].find(':')+1:].split()))
    distances = list(map(int, lines[1][lines[1].find(':')+1:].split()))
    tot_ways = 1

    for i in range(len(times)):
        ways = 0
        for j in range(times[i]):
            if j * (times[i] - j) > distances[i]:
                ways = j
                break

        for j in range(times[i], 0, -1):
            if j * (times[i] - j) > distances[i]:
                ways = j - ways + 1
                break
        tot_ways *= ways

    print(tot_ways)


def part2():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    time = int(''.join(map(lambda x: x.strip(),
               lines[0][lines[0].find(':')+1:].split())))
    dist = int(''.join(map(lambda x: x.strip(),
               lines[1][lines[1].find(':')+1:].split())))
    ways = 0

    for j in range(time):
        if j * (time - j) > dist:
            ways = j
            break

    for j in range(time, 0, -1):
        if j * (time - j) > dist:
            ways = j - ways + 1
            break

    print(ways)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
