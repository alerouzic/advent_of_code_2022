import string

priorities = {c: i + 1 for i, c in enumerate(list(string.ascii_letters))}


if __name__ == "__main__":
    total = 0
    with open("input.txt") as file:
        for line in file:
            mid = int(len(line) / 2)
            bp1, bp2 = (line[:mid], line[mid:])
            char_c = list(set(bp1) & set(bp2))
            total += priorities[char_c[0]]
    print(total)
