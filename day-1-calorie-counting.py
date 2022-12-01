from aocd import get_data
import bisect

rawData = get_data(day=1, year=2022)
data = rawData.splitlines()

calories = []
caloriesForCurrentElf = 0

for n in data:
    if n != '':
        caloriesForCurrentElf += int(n)
    else:
        bisect.insort(calories, caloriesForCurrentElf)
        caloriesForCurrentElf = 0

print(calories[-1])
#70116

print(sum(calories[-3:]))
#206582
