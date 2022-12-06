def issubset(r1, r2):
    return r1.start in r2 and r1[-1] in r2


if __name__ == "__main__":
    total = 0
    with open("input.txt") as file:
        for line in file:
            e1s, e1e, e2s, e2e = line.strip().replace(",", "-").split("-")
            e1r = range(int(e1s), int(e1e) + 1)
            e2r = range(int(e2s), int(e2e) + 1)
            if issubset(e1r, e2r) or issubset(e2r, e1r):
                total += 1
    print(total)
