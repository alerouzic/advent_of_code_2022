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


outcomes = {
    "X": {"winA": "Z", "loseA": "Y", "drawA": "X"},
    "Y": {"winA": "X", "loseA": "Z", "drawA": "Y"},
    "Z": {"winA": "Y", "loseA": "X", "drawA": "Z"},
}

# X for Rock, Y for Paper, and Z for Scissors
def getScoreRound(enemy_shape, my_shape):
    if outcomes[my_shape]["winA"] == enemy_shape:
        result = 6
    elif my_shape == enemy_shape:
        result = 3
    else:
        result = 0
    return result


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def shapeToPlay(enemy_shape, action):
    symbolToChose = {"X": "winA", "Y": "drawA", "Z": "loseA"}
    return outcomes[getEnemySymbol(enemy_shape)][symbolToChose[action]]


total = 0
with open("./input.txt") as file:
    for line in file:
        enemy_shape, outcome = line.strip().split()
        my_shape = shapeToPlay(enemy_shape, outcome)
        # print(f"{getEnemySymbol(enemy_shape)} > {outcome} > {my_shape}")
        round_score = getScoreSelectedShape(my_shape) + getScoreRound(getEnemySymbol(enemy_shape), my_shape)
        total += round_score
print(total)
