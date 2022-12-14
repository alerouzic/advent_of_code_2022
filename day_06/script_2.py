from collections import deque

CHARS_PER_PATTERN = 14


def isPacketStart(list):
    return len(set(list)) == CHARS_PER_PATTERN


if __name__ == "__main__":
    f = open("input.txt")
    data = f.read()

    last_four = deque(maxlen=CHARS_PER_PATTERN)
    index = 0
    for c in data:
        last_four.append(c)
        index += 1
        if isPacketStart(list(last_four)):
            print(f"found at {index}")
            break
