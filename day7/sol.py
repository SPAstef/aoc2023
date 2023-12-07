from functools import cmp_to_key
from enum import IntEnum, auto


class CardKind(IntEnum):
    HIGH = auto()
    PAIR = auto()
    DOUBLE = auto()
    THREE = auto()
    FULL = auto()
    FOUR = auto()
    FIVE = auto()


CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

CARD_VALUES_PART2 = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                     '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}


def card_value1(c: str) -> int: return CARD_VALUES[c]


def hand_kind1(h: str) -> int:
    if h[0] == h[1]:
        if h[1] == h[2]:
            if h[2] == h[3]:
                if h[3] == h[4]:
                    return CardKind.FIVE
                return CardKind.FOUR
            if h[3] == h[4]:
                return CardKind.FULL
            return CardKind.THREE
        if h[2] == h[3]:
            if h[3] == h[4]:
                return CardKind.FULL
            return CardKind.DOUBLE
        if h[3] == h[4]:
            return CardKind.DOUBLE
        return CardKind.PAIR

    if h[1] == h[2]:
        if h[2] == h[3]:
            if h[3] == h[4]:
                return CardKind.FOUR
            return CardKind.THREE
        if h[3] == h[4]:
            return CardKind.DOUBLE
        return CardKind.PAIR

    if h[2] == h[3]:
        if h[3] == h[4]:
            return CardKind.THREE
        return CardKind.PAIR

    if h[3] == h[4]:
        return CardKind.PAIR

    return CardKind.HIGH


def cmp_values1(x: str, y: str) -> int:
    if card_value1(x[0]) > card_value1(y[0]):
        return 1
    if card_value1(x[0]) < card_value1(y[0]):
        return -1

    if card_value1(x[1]) > card_value1(y[1]):
        return 1
    if card_value1(x[1]) < card_value1(y[1]):
        return -1

    if card_value1(x[2]) > card_value1(y[2]):
        return 1
    if card_value1(x[2]) < card_value1(y[2]):
        return -1

    if card_value1(x[3]) > card_value1(y[3]):
        return 1
    if card_value1(x[3]) < card_value1(y[3]):
        return -1

    if card_value1(x[4]) > card_value1(y[4]):
        return 1
    if card_value1(x[4]) < card_value1(y[4]):
        return -1

    return 0


def cmp_hands1(x: tuple[str, int], y: tuple[str, int]) -> int:

    kx = hand_kind1(sorted(x[0]))
    ky = hand_kind1(sorted(y[0]))

    if kx > ky:
        return 1
    if kx < ky:
        return -1

    return cmp_values1(x[0], y[0])


def card_value2(c: str) -> int: return CARD_VALUES_PART2[c]


def hand_kind2(h: str) -> int:
    if h[0] == 'J':
        return CardKind.FIVE

    if h[1] == 'J':
        return CardKind.FIVE

    if h[0] == h[1]:
        if h[2] == 'J':
            return CardKind.FIVE
        if h[1] == h[2]:
            if h[3] == 'J':
                return CardKind.FIVE
            if h[2] == h[3]:
                if h[4] == 'J':
                    return CardKind.FIVE
                if h[3] == h[4]:
                    return CardKind.FIVE
                return CardKind.FOUR

            if h[4] == 'J':
                return CardKind.FOUR
            if h[3] == h[4]:
                return CardKind.FULL
            return CardKind.THREE

        if h[3] == 'J':
            return CardKind.FOUR
        if h[2] == h[3]:
            if h[4] == 'J':
                return CardKind.FULL
            if h[3] == h[4]:
                return CardKind.FULL
            return CardKind.DOUBLE

        if h[4] == 'J':
            return CardKind.THREE
        if h[3] == h[4]:
            return CardKind.DOUBLE
        return CardKind.PAIR

    if h[2] == 'J':
        return CardKind.FOUR
    if h[1] == h[2]:
        if h[3] == 'J':
            return CardKind.FOUR
        if h[2] == h[3]:
            if h[4] == 'J':
                return CardKind.FOUR
            if h[3] == h[4]:
                return CardKind.FOUR
            return CardKind.THREE

        if h[4] == 'J':
            return CardKind.THREE
        if h[3] == h[4]:
            return CardKind.DOUBLE
        return CardKind.PAIR

    if h[3] == 'J':
        return CardKind.THREE
    if h[2] == h[3]:
        if h[4] == 'J':
            return CardKind.THREE
        if h[3] == h[4]:
            return CardKind.THREE
        return CardKind.PAIR

    if h[4] == 'J':
        return CardKind.PAIR
    if h[3] == h[4]:
        return CardKind.PAIR

    return CardKind.HIGH


def cmp_values2(x: str, y: str) -> int:
    if card_value2(x[0]) > card_value2(y[0]):
        return 1
    if card_value2(x[0]) < card_value2(y[0]):
        return -1

    if card_value2(x[1]) > card_value2(y[1]):
        return 1
    if card_value2(x[1]) < card_value2(y[1]):
        return -1

    if card_value2(x[2]) > card_value2(y[2]):
        return 1
    if card_value2(x[2]) < card_value2(y[2]):
        return -1

    if card_value2(x[3]) > card_value2(y[3]):
        return 1
    if card_value2(x[3]) < card_value2(y[3]):
        return -1

    if card_value2(x[4]) > card_value2(y[4]):
        return 1
    if card_value2(x[4]) < card_value2(y[4]):
        return -1

    return 0


def cmp_hands2(x: tuple[str, int], y: tuple[str, int]) -> int:

    kx = hand_kind2(sorted(x[0], key=lambda c: ord(c) if c != 'J' else 128))
    ky = hand_kind2(sorted(y[0], key=lambda c: ord(c) if c != 'J' else 128))

    if kx > ky:
        return 1
    if kx < ky:
        return -1

    return cmp_values2(x[0], y[0])


def part1():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    hands = [line.split() for line in lines]
    hands = [(hand[0], int(hand[1])) for hand in hands]
    hands.sort(key=cmp_to_key(cmp_hands1))
    tot = 0

    for i in range(len(hands)):
        tot += (i + 1) * hands[i][1]

    print(tot)


def part2():
    with open("data.txt", "rt") as file:
        lines = file.readlines()

    hands = [line.split() for line in lines]
    hands = [(hand[0], int(hand[1])) for hand in hands]
    hands.sort(key=cmp_to_key(cmp_hands2))
    tot = 0

    for i in range(len(hands)):
        tot += (i + 1) * hands[i][1]

    print(tot)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
