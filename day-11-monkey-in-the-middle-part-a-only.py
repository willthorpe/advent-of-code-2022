from aocd import get_data
import math

rawData = get_data(day=11, year=2022)
data = rawData.splitlines()

monkeyData = []
inspectionsByMonkeys = []

for i in range(0, len(data), 7):
    monkeyData.append({})
    inspectionsByMonkeys.append(0)
    chunk = data[i:i+7]
    currentMonkey = len(monkeyData) - 1
    monkeyData[currentMonkey]['monkey'] = chunk[0][-2:-1]
    monkeyData[currentMonkey]['startingItems'] = chunk[1].split(':')[1].split(',')
    monkeyData[currentMonkey]['startingItems'] = [x.strip(' ') for x in monkeyData[currentMonkey]['startingItems']]
    monkeyData[currentMonkey]['operation'] = chunk[2].split('new = ')[1]
    monkeyData[currentMonkey]['test'] = chunk[3].split(':')[1]
    monkeyData[currentMonkey]['true'] = chunk[4][-1]
    monkeyData[currentMonkey]['false'] = chunk[5][-1]

for i in range(0, 20):
    for idx, monkey in enumerate(monkeyData):
        while len(monkey['startingItems']) > 0:
            item = monkey['startingItems'][0]
            inspectionsByMonkeys[idx] += 1
            worryLevel = int(item)
            if "old + " in monkey['operation']:
                worryLevel += int(monkey['operation'].split('+ ')[1])
            elif "old * " in monkey['operation']:
                amount = monkey['operation'].split('* ')[1]
                if "old" == amount:
                    worryLevel *= worryLevel
                else:
                    worryLevel = worryLevel * int(amount)
            worryLevel = int(int(worryLevel) / 3)

            if "divisible by" in monkey['test']:
                divisor = monkey['test'].split('divisible by ')[1]
                if worryLevel % int(divisor) == 0:
                    monkeyData[int(monkey['true'])]['startingItems'].append(worryLevel)
                else:
                    monkeyData[int(monkey['false'])]['startingItems'].append(worryLevel)
            monkey['startingItems'].remove(item)

sortedInspections = sorted(inspectionsByMonkeys, reverse=True)
print(math.prod(sortedInspections[:2]))
#51075