def main():
    s = 0
    digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    with open("data.txt") as f:
        lines = f.readlines()
        for l in lines:
            i = 0
            n = 0
            while not (l[i].isdigit() or l[i:].startswith(digits)):
                i += 1
            
            if l[i].isdigit():
                n += int(l[i])
            else:
                if l[i] == 'o':
                    n += 1
                elif l[i] == 'e':
                    n += 8
                elif l[i] == 'n':
                    n += 9
                elif l[i + 1] == 'w':
                    n += 2
                elif l[i] == 't':
                    n += 3
                elif l[i + 1] == 'o':
                    n += 4
                elif l[i] == 'f':
                    n += 5
                elif l[i + 1] == 'i':
                    n += 6
                else:
                    n += 7
            
            n *= 10

            i = len(l) - 1
            while not (l[i].isdigit() or l[:i+1].endswith(digits)):
                i -= 1

            if l[i].isdigit():
                n += int(l[i])
            else:
                if l[i] == 'o':
                    n += 2
                elif l[i] == 'r':
                    n += 4
                elif l[i] == 'x':
                    n += 6
                elif l[i] == 'n':
                    n += 7
                elif l[i] == 't':
                    n += 8
                elif l[i - 2] == 'o':
                    n += 1
                elif l[i - 2] == 'r':
                    n += 3
                elif l[i - 1] == 'v':
                    n += 5
                else:
                    n += 9
            
            print(n)

            s += int(n)

    print(s)


if __name__ == "__main__":
    main()
