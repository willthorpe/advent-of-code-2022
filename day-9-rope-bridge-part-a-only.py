from aocd import get_data
import numpy as np

rawData = get_data(day=9, year=2022)
data = rawData.splitlines()

data = [
  'R 5',
  'U 8',
  'L 8',
  'D 3',
  'R 17',
  'D 10',
  'L 25',
  'U 20',
]

maxHeight = 1
maxWidth = 1

height = [maxHeight, maxHeight]
width = [maxWidth, maxWidth]

for instruction in data:
    if "L" in instruction:
        width[0] += int(instruction[2:])
    if "R" in instruction:
        width[1] += int(instruction[2:])
    if "U" in instruction:
        height[0] += int(instruction[2:])
    if "D" in instruction:
        height[1] += int(instruction[2:])
maxHeight = max(height)
maxWidth = max(width)

grid = np.full((maxHeight, maxWidth), '')
hPosition = [0, 0]
tPosition = hPosition
grid[hPosition[0], hPosition[1]] = 'T'

def gapOfMoreThanOneBetweenHandT(tPosition, oldHPosition, newHPosition,  direction):
    oldGap = np.linalg.norm(np.array(oldHPosition) - np.array(tPosition))
    gap = np.linalg.norm(np.array(newHPosition) - np.array(tPosition))
    if gap > 2:
        tPosition = oldHPosition
    elif gap > 1.4142135623730951:
        if direction == "L":
            tPosition = [int(tPosition[0]), tPosition[1] - 1]
        if direction == "R":
            tPosition = [int(tPosition[0]), tPosition[1] + 1]
        if direction == "U":
            tPosition = [int(tPosition[0]) + 1, tPosition[1]]
        if direction == "D":
            tPosition = [int(tPosition[0]) - 1, tPosition[1]]

    grid[tPosition[0]][tPosition[1]] = 'T'

    return tPosition

for idx, instruction in enumerate(data):
    if "L" in instruction:
        for i in range(hPosition[1] - int(instruction[2:]), hPosition[1]):
            newHPosition = [int(hPosition[0]), int(hPosition[1]) - 1]
            tPosition = gapOfMoreThanOneBetweenHandT(tPosition, hPosition, newHPosition, "L")
            hPosition = newHPosition
    if "R" in instruction:
        for i in range(hPosition[1], hPosition[1] + int(instruction[2:])):
            newHPosition = [int(hPosition[0]), int(hPosition[1]) + 1]
            tPosition = gapOfMoreThanOneBetweenHandT(tPosition, hPosition, newHPosition, "R")
            hPosition = newHPosition
    if "U" in instruction:
        for i in range(hPosition[0], hPosition[0] + int(instruction[2:])):
            newHPosition = [int(hPosition[0]) + 1, int(hPosition[1])]
            tPosition = gapOfMoreThanOneBetweenHandT(tPosition, hPosition, newHPosition, "U")
            hPosition = newHPosition
    if "D" in instruction:
        for i in range(hPosition[0] - int(instruction[2:]), hPosition[0]):
            newHPosition = [int(hPosition[0]) - 1, int(hPosition[1])]
            tPosition = gapOfMoreThanOneBetweenHandT(tPosition, hPosition, newHPosition, "D")
            hPosition = newHPosition

print(np.count_nonzero(grid == 'T'))
#6642