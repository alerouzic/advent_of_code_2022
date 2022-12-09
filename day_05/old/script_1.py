import functools

columns = [1, 5, 9, 13, 17, 21, 25, 29, 33]
lines = list(range(1, 9))


def getDict(line):
    return [line[e] for i, e in enumerate(columns)]


if __name__ == "__main__":
    f = open("input.txt")
    data = f.read()

    crates_levels = data.split("\n")[:8]
    l = [getDict(line) for line in crates_levels]

    stacks = functools.reduce(lambda acc, x: [m + n for m, n in zip(acc, x)], l)
    stacks = list(map(lambda x: x.strip()[::-1], stacks))
    stacks_dict = {i + 1: list(e) for i, e in enumerate(stacks)}

    print(stacks_dict)
