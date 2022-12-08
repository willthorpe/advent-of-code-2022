from aocd import get_data
import itertools
import math

rawData = get_data(day=8, year=2022)
data = rawData.splitlines()

matrixData = []
countVisible = 0
highestScenicScore = 0

for row in data:
    matrixData.append(list(row))

transposedMatrixData = list(map(list, itertools.zip_longest(*matrixData, fillvalue=0)))

def findLargerTrees(tree, rowOfTrees):
    firstMatchingIndex = None
    lastMatchingIndex = None

    for index, item in enumerate(rowOfTrees):
        if int(item) >= int(tree):
            if firstMatchingIndex is None:
                firstMatchingIndex = int(index)
            lastMatchingIndex = int(index)

    return [firstMatchingIndex, lastMatchingIndex]

for idx, row in enumerate(matrixData):
    if idx == 0 or idx == len(matrixData) - 1:
        countVisible += len(row)
    else:
        for rowIdx, tree in enumerate(row):
            if rowIdx == 0 or rowIdx == len(row) - 1:
                countVisible += 1
            else:
                scenicScores = [0, 0, 0, 0]
                transposedRow = transposedMatrixData[rowIdx]

                if all(i < tree for i in row[:rowIdx]):
                    countVisible += 1
                elif all(i < tree for i in row[rowIdx + 1:]):
                    countVisible += 1
                elif all(i < tree for i in transposedRow[:idx]):
                    countVisible += 1
                elif all(i < tree for i in transposedRow[idx + 1:]):
                    countVisible += 1

                horizontalLeftLargerTrees = findLargerTrees(tree, row[:rowIdx])
                horizontalRightLargerTrees = findLargerTrees(tree, row[rowIdx + 1:])
                verticalUpLargerTrees = findLargerTrees(tree, transposedRow[:idx][::-1])
                verticalDownLargerTrees = findLargerTrees(tree, transposedRow[idx + 1:])

                if verticalUpLargerTrees[0] is not None:
                    if verticalUpLargerTrees[0] > 0:
                        scenicScores[0] += verticalUpLargerTrees[0] + 1
                else:
                    scenicScores[0] += len(transposedRow[:idx])
                if horizontalLeftLargerTrees[1] is not None:
                     if horizontalLeftLargerTrees[1] > 0:
                        scenicScores[1] += abs(rowIdx - horizontalLeftLargerTrees[1])
                else:
                    scenicScores[1] += len(row[:rowIdx])
                if verticalDownLargerTrees[0] is not None:
                    scenicScores[2] += verticalDownLargerTrees[0] + 1
                else:
                    scenicScores[2] += len(transposedRow[idx + 1:])
                if horizontalRightLargerTrees[0] is not None:
                   scenicScores[3] += horizontalRightLargerTrees[0] + 1
                else:
                    scenicScores[3] += len(row[rowIdx + 1:])

                if math.prod(scenicScores) > highestScenicScore:
                    highestScenicScore = math.prod(scenicScores)

print(countVisible)
#1803

print(highestScenicScore)
#268912