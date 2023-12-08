from math import lcm


def part1():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    cmds = [0 if c == 'L' else 1 for c in lines[0].strip()]
    table = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        pos = table[pos][cmds[steps % len(cmds)]]
        steps += 1

    print(steps)


def part2():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    cmds = [0 if c == 'L' else 1 for c in lines[0].strip()]
    table = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

    pos = [k for k in table.keys() if k[2] == 'A']
    print(pos)
    steps = 0
    min_steps = [0] * len(pos)
    while not all(min_steps):
        for i in range(len(pos)):
            pos[i] = table[pos[i]][cmds[steps % len(cmds)]]
        steps += 1
        for i in range(len(pos)):
            if pos[i][2] == 'Z':
                min_steps[i] = steps

    steps = lcm(*min_steps)
    print(steps)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()
