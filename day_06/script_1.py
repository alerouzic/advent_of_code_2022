from collections import deque

def isPacketStart(list):
    return len(set(list)) == 4


if __name__ == "__main__":
    f = open("input.txt")
    data = f.read()

    last_four = deque(maxlen=4)
    index=0
    for c in data:
        last_four.append(c)
        index+=1
        if isPacketStart(list(last_four)):
            print(f"found at {index}")
            break
