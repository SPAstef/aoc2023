from joblib import Parallel, delayed


def part1():
    with open("data.txt") as file:
        lines = file.readlines()

    seeds = list(map(int, lines[0][lines[0].find(':')+1:].split()))

    tables = []
    l = 3
    while l < len(lines):
        tables.append([])
        while l < len(lines) and lines[l][0] != '\n':
            tables[-1].append(tuple(map(int, lines[l].split())))
            l += 1
        l += 2

    min_loc = -1

    for seed in seeds:
        x = seed
        for table in tables:
            for entry in table:
                if entry[1] <= x < entry[1] + entry[2]:
                    x = entry[0] + x - entry[1]
                    break

        if min_loc < 0 or x < min_loc:
            min_loc = x

    print(f"Best location = {min_loc}")


def process(i, seeds, tables):
    min_loc = -1
    beg, end = seeds[i]
    per = 0
    for seed in range(beg, beg + end):
        loc = seed
        for table in tables:
            for entry in table:
                if entry[1] <= loc < entry[1] + entry[2]:
                    loc = entry[0] + loc - entry[1]
                    break
        if min_loc < 0 or loc < min_loc:
            min_loc = loc
        if (seed + 1 - beg) * 100 // end > per:
            per += 1
            for _ in range(i):
                print(end="     ")
            print(f"{per:3.0f}% ", end="")
            for _ in range(i + 1, len(seeds)):
                print(end="     ")
            print()

    return min_loc


def part2():
    with open("data.txt") as file:
        lines = file.readlines()

    seeds = list(map(int, lines[0][lines[0].find(':')+1:].split()))
    seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    tables = []
    l = 3
    while l < len(lines):
        tables.append([])
        while l < len(lines) and lines[l][0] != '\n':
            tables[-1].append(tuple(map(int, lines[l].split())))
            l += 1
        l += 2

    min_locs = Parallel(n_jobs=len(seeds))(
        delayed(process)(i, seeds, tables) for i in range(len(seeds)))
    min_loc = min(min_locs)
    print()

    print(f"Best location = {min_loc}")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
