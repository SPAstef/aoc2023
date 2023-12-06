def issymbol(c: str) -> bool:
    return not (c.isdecimal() or c == '.' or c == '\n')


def part1():
    with open("data.txt", "rt") as file:
        lines = file.readlines()
        sum = 0
        h = len(lines)
        for i in range(h):
            w = len(lines[i])
            j = 0
            while j < w:
                while j < w and not lines[i][j].isdecimal():
                    j += 1
                if j == w:
                    continue
                k = j
                isvalid = False
                while j < w and lines[i][j].isdecimal():
                    j += 1
                for l in range(max(0, k - 1), min(w, j+1)):
                    if i > 0:
                        isvalid |= issymbol(lines[i - 1][l])
                    isvalid |= issymbol(lines[i][l])
                    if i < h - 1:
                        isvalid |= issymbol(lines[i+1][l])
                if isvalid:
                    n = int(lines[i][k:j])
                    sum += n

    print(sum)


def part2():
    index_map = {0b101_00_000: (-1, -1, -1, +1),
                 0b100_10_000: (-1, -1, +0, -1),
                 0b100_01_000: (-1, -1, +0, +1),
                 0b100_00_100: (-1, -1, +1, -1),
                 0b100_00_010: (-1, -1, +1, +0),
                 0b100_00_001: (-1, -1, +1, +1),
                 0b010_10_000: (-1, +0, +0, -1),
                 0b010_01_000: (-1, +0, +0, +0),
                 0b010_00_100: (-1, +0, +1, -1),
                 0b010_00_010: (-1, +0, +1, +0),
                 0b010_00_001: (-1, +0, +1, +1),
                 0b001_10_000: (-1, +1, +0, -1),
                 0b001_01_000: (-1, +1, +0, +0),
                 0b001_00_100: (-1, +1, +1, -1),
                 0b001_00_010: (-1, +1, +1, +0),
                 0b001_00_001: (-1, +1, +1, +1),
                 0b000_11_000: (+0, -1, +0, +1),
                 0b000_10_100: (+0, -1, +1, -1),
                 0b000_10_010: (+0, -1, +1, +0),
                 0b000_10_001: (+0, -1, +1, +1),
                 0b000_01_100: (+0, +1, +1, -1),
                 0b000_01_010: (+0, +1, +1, +0),
                 0b000_01_001: (+0, +1, +1, +1),
                 0b000_00_101: (+1, -1, +1, +1),
                 }

    with open("data.txt", "rt") as file:
        lines = file.readlines()
        sum = 0
        n = 0
        h = len(lines)
        for i in range(h):
            w = len(lines[i])
            j = 0
            while j < w:
                while j < w and lines[i][j] != '*':
                    j += 1
                if j == w:
                    continue

#fmt: off
                adj = \
                    (i > 0      and j > 0       and lines[i - 1][j - 1].isdecimal()) << 7 | \
                    (i > 0                      and lines[i - 1][j + 0].isdecimal()) << 6 | \
                    (i > 0      and j < w - 1   and lines[i - 1][j + 1].isdecimal()) << 5 | \
                    (j > 0                      and lines[i + 0][j - 1].isdecimal()) << 4 | \
                    (               j < w - 1   and lines[i + 0][j + 1].isdecimal()) << 3 | \
                    (i < h - 1  and j > 0       and lines[i + 1][j - 1].isdecimal()) << 2 | \
                    (i < h - 1                  and lines[i + 1][j + 0].isdecimal()) << 1 | \
                    (i < h - 1  and j < w - 1   and lines[i + 1][j + 1].isdecimal()) << 0
#fmt: on
                if (adj >> 0) & 1 == (adj >> 1) & 1:
                    adj &= ~(1 << 0)
                if (adj >> 1) & 1 == (adj >> 2) & 1:
                    adj &= ~(1 << 1)
                if (adj >> 5) & 1 == (adj >> 6) & 1:
                    adj &= ~(1 << 5)
                if (adj >> 6) & 1 == (adj >> 7) & 1:
                    adj &= ~(1 << 6)

                if adj not in index_map:
                    j += 1
                    continue

                i1, j1, i2, j2 = index_map[adj]
                i1 = i + i1
                j1 = j + j1
                i2 = i + i2
                j2 = j + j2

                while i1 >= 0 and lines[i1][j1].isdecimal():
                    j1 -= 1
                j1 += 1
                k1 = j1
                while j1 < w and lines[i1][j1].isdecimal():
                    j1 += 1

                while j2 >= 0 and lines[i2][j2].isdecimal():
                    j2 -= 1
                j2 += 1
                k2 = j2
                while j2 < w and lines[i2][j2].isdecimal():
                    j2 += 1

                l = int(lines[i1][k1:j1])
                r = int(lines[i2][k2:j2])
                n += 1

                sum += l * r
                j += 1

    print(sum)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
