from aocd import get_data

rawData = get_data(day=3, year=2022)
data = rawData.splitlines()

def findPriorityForChar(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

sumPartAPriorities = 0
sumPartBPriorities = 0

for i in range(0, len(data), 3):
    chunk = data[i:i+3]
    (char,) = set(chunk[0]) & set(chunk[1]) & set(chunk[2])
    sumPartBPriorities += findPriorityForChar(char)

    for backpack in chunk:
        n = len(backpack)
        (char,) = set(backpack[0:n//2]) & set(backpack[n//2:])
        sumPartAPriorities += findPriorityForChar(char)


print(sumPartAPriorities)
#8105

print(sumPartBPriorities)
#2363
