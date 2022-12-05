def getScoreSelectedShape(shape):
    return {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }[shape]


def getEnemySymbol(enemy_shape):
    return {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }[enemy_shape]


# X for Rock, Y for Paper, and Z for Scissors
def getScoreRound(enemy_shape, my_shape):
    winAgainst = {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    }
    if winAgainst[my_shape] == enemy_shape:
        result = 6
    elif my_shape == enemy_shape:
        result = 3
    else:
        result = 0
    return result

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
total = 0
with open("./input.txt") as file:
    for line in file:
        e, m = line.strip().split()
        round_score = getScoreSelectedShape(m) + getScoreRound(getEnemySymbol(e), m)
        total += round_score
print(total)
