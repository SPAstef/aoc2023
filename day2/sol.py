def part1():
    MAX = {'r': 12, 'g': 13, 'b': 14}

    with open("data.txt", "rt") as file:
        lines = file.readlines()
        v = 0
        for i in range(len(lines)):
            j = 0
            valid = True

            while not lines[i][j].isdecimal():
                j += 1

            k = j
            while lines[i][j].isdecimal():
                j += 1
            id = int(lines[i][k:j])

            while not lines[i][j].isdecimal():
                j += 1

            while j < len(lines[i]):
                k = j
                while lines[i][j].isdecimal():
                    j += 1
                q = int(lines[i][k:j])
                j += 1

                if q > MAX[lines[i][j]]:
                    valid = False

                while j < len(lines[i]) and not lines[i][j].isdecimal():
                    j += 1

            if valid:
                v += id

    print(v)


def part2():
    with open("data.txt", "rt") as file:
        lines = file.readlines()
        sum = 0
        for i in range(len(lines)):
            j = 0
            min_power = {'r': 0, 'g': 0, 'b': 0}

            while lines[i][j] != ':':
                j += 1
            j += 2

            while j < len(lines[i]):
                k = j
                while lines[i][j].isdecimal():
                    j += 1
                q = int(lines[i][k:j])

                j += 1
                if q > min_power[lines[i][j]]:
                    min_power[lines[i][j]] = q

                while j < len(lines[i]) and not lines[i][j].isdecimal():
                    j += 1

            sum += min_power['r'] * min_power['g'] * min_power['b']

    print(sum)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
