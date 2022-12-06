import string

priorities = {c: i + 1 for i, c in enumerate(list(string.ascii_letters))}


def grouped(l, n):
    return [l[k : k + n] for k in range(0, len(l), n)]


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = [line.strip() for line in file]

    groups = grouped(lines, 3)
    total = 0

    for [bp1, bp2, bp3] in groups:
        char_c = list(set(bp1) & set(bp2) & set(bp3))
        total += priorities[char_c[0]]
    print(total)
