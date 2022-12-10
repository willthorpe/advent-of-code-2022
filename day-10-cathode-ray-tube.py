from aocd import get_data

rawData = get_data(day=10, year=2022)
data = rawData.splitlines()

def checkWhatHappensDuringCycle(cycle):
    currentCRTRow = int(cycle / 40)
    spritePositions = [spriteMiddlePosition - 1, spriteMiddlePosition, spriteMiddlePosition + 1]

    positionToLookFor = cycle - (currentCRTRow * 40)

    if positionToLookFor in spritePositions:
        cRTRows[currentCRTRow].append('#')
    else:
        cRTRows[currentCRTRow].append('.')

    if cycle in importantCycles:
        importantStrengths.append(spriteMiddlePosition)
        cRTRows.append([])
        currentCRTRow += 1

cycle = 0
spriteMiddlePosition = 1
addDict = {}

importantStrengths = []
importantCycles = [19, 59, 99, 139, 179, 219]

cRTRows = [[]]
currentCRTRow = 0

for index, instruction in enumerate(data):
    if "addx" in instruction:
        addDict[cycle + 2] = instruction[5:]

    if cycle in addDict:
        spriteMiddlePosition += int(addDict[cycle])
        del(addDict[cycle])

    checkWhatHappensDuringCycle(cycle)
    cycle += 1

    if "addx" in instruction:
        checkWhatHappensDuringCycle(cycle)
        cycle += 1

if len(addDict) > 0:
    for cycle in addDict:
        spriteMiddlePosition += int(addDict[cycle])

totalImportantStrength = 0

for idx, strength in enumerate(importantStrengths):
    totalImportantStrength += strength * (importantCycles[idx] + 1)

print(totalImportantStrength)
#16020

print(cRTRows[0])
print(cRTRows[1])
print(cRTRows[2])
print(cRTRows[3])
print(cRTRows[4])
print(cRTRows[5])
#ECZUZALR