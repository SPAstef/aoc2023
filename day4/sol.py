def part1():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    s = 0
    for line in lines:
        j = 0
        winning = set()
        mine = set()

        while line[j] != ':':
            j += 1
        j += 1
        while line[j] == ' ':
            j += 1

        while line[j] != '|':
            k = j
            while line[j].isdigit():
                j += 1
            winning.add(int(line[k:j]))
            while line[j] == ' ':
                j += 1

        j += 1
        while line[j] == ' ':
            j += 1

        while line[j] != '\n':
            k = j
            while line[j].isdigit():
                j += 1
            mine.add(int(line[k:j]))
            while line[j] == ' ':
                j += 1

        n = len(winning & mine) - 1
        s += 0 if n < 0 else 1 << n

    print(s)


def part2():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    s = 0
    mult = [1] * len(lines)

    for i in range(len(lines)):
        j = 0
        winning = set()
        mine = set()

        while lines[i][j] != ':':
            j += 1
        j += 1
        while lines[i][j] == ' ':
            j += 1

        while lines[i][j] != '|':
            k = j
            while lines[i][j].isdigit():
                j += 1
            winning.add(int(lines[i][k:j]))
            while lines[i][j] == ' ':
                j += 1

        j += 1
        while lines[i][j] == ' ':
            j += 1

        while lines[i][j] != '\n':
            k = j
            while lines[i][j].isdigit():
                j += 1
            mine.add(int(lines[i][k:j]))
            while lines[i][j] == ' ':
                j += 1

        n = len(winning & mine)
        for j in range(i + 1, min(len(mult), i + n + 1)):
            mult[j] += mult[i]

    s = sum(mult)
    print(s)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
