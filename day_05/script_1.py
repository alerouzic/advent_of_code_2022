import functools

columns = [1, 5, 9, 13, 17, 21, 25, 29, 33]
lines = list(range(0, 8))

if __name__ == "__main__":
    f = open("input.txt")
    data = f.read()
    crates_lines = data.split("\n")[:8]

    stacks = [[crates_lines[l][c] for l in lines[::-1] if crates_lines[l][c] != " "] for c in columns]
    stacks = {i + 1: e for i, e in enumerate(stacks)}

    for line in data.split("\n")[10:]:
        l_s = line.split()
        n, a, b = [int(l_s[i]) for i in (1, 3, 5)]
        for _ in range(n):
            stacks[b].append(stacks[a].pop())

    print([v[-1] for k, v in stacks.items()])
