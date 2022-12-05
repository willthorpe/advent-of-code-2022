from aocd import get_data
import copy

rawData = get_data(day=5, year=2022)
data = rawData.splitlines()

stacks = {}
instructions = []
finishSplitting = False

def getTopElementsInStacks(stacks):
    topElementsInStacks = ''
    for stack in sorted(stacks.items()):
        topElementsInStacks += stack[1][-1]

    return topElementsInStacks

for datum in data:
    if "[" not in datum:
        finishSplitting = True
    if finishSplitting == False:
        n = 4
        startingStacks = [datum[i:i+n] for i in range(0, len(datum), n)]
        for i, stack in enumerate(startingStacks):
            stack = stack.strip().strip(']').strip('[')
            if len(stack) == 1:
                stacks.setdefault(i,[]).insert(0, stack)

    elif "move" in datum:
        instructions.append(datum)

partAStacks = copy.deepcopy(stacks)
partBStacks = copy.deepcopy(stacks)

for instruction in instructions:
    moveKeyword, amount, fromKeyword, stackFrom, toKeyword, stackTo = instruction.split(' ')
    for i in range(0, int(amount)):
        firstElementInFromStack = partAStacks[int(stackFrom) - 1].pop()
        partAStacks[int(stackTo) - 1].append(firstElementInFromStack)
    elementsToMove = partBStacks[int(stackFrom) - 1][-int(amount):]
    del(partBStacks[int(stackFrom) - 1][-int(amount):])
    partBStacks[int(stackTo) - 1].extend(elementsToMove)

topElementsInStacksA = getTopElementsInStacks(partAStacks)
topElementsInStacksB = getTopElementsInStacks(partBStacks)

print(topElementsInStacksA)
#TQRFCBSJJ

print(topElementsInStacksB)
#RMHFJNVFP