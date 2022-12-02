from aocd import get_data

rawData = get_data(day=2, year=2022)
data = rawData.splitlines()

THEIR_ROCK = 'A'
THEIR_PAPER = 'B'
THEIR_SCISSORS = 'C'

OUR_ROCK = 'X'
OUR_PAPER = 'Y'
OUR_SCISSORS = 'Z'

#For Part A when the X/Y/Z are the moves we play
scorePerPieceDict = {OUR_ROCK: 1, OUR_PAPER: 2, OUR_SCISSORS: 3}

scorePerMoveDict = {
    OUR_ROCK: {THEIR_ROCK: 3, THEIR_PAPER: 0, THEIR_SCISSORS: 6},
    OUR_PAPER: {THEIR_ROCK: 6, THEIR_PAPER: 3, THEIR_SCISSORS: 0},
    OUR_SCISSORS: {THEIR_ROCK: 0, THEIR_PAPER: 6, THEIR_SCISSORS: 3}
}

partAScore = 0

#For Part B when the X/Y/Z are whether to lose/draw/win
moveToPlayDict = {
    'X': {THEIR_ROCK: OUR_SCISSORS, THEIR_PAPER: OUR_ROCK, THEIR_SCISSORS: OUR_PAPER},
    'Y': {THEIR_ROCK: OUR_ROCK, THEIR_PAPER: OUR_PAPER, THEIR_SCISSORS: OUR_SCISSORS},
    'Z': {THEIR_ROCK: OUR_PAPER, THEIR_PAPER: OUR_SCISSORS, THEIR_SCISSORS: OUR_ROCK}
}
scorePerDecisionDict = {'X': 0, 'Y': 3, 'Z': 6}

partBScore = 0

for n in data:
    opponentMove, ourMove = n.split(' ')

    partAScore += scorePerPieceDict[ourMove]
    partAScore += scorePerMoveDict[ourMove][opponentMove]

    partBScore += scorePerDecisionDict[ourMove]
    partBScore += scorePerPieceDict[moveToPlayDict[ourMove][opponentMove]]

print(partAScore)
#13809

print(partBScore)
#12316