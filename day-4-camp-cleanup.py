from aocd import get_data

rawData = get_data(day=4, year=2022)
data = rawData.splitlines()

countSubsets = 0
countOverlap = 0

def findRangeForSection(section):
    sectionStart, sectionEnd = section.split('-')
    sectionAssignments = range(int(sectionStart), int(sectionEnd) + 1)
    return set(sectionAssignments)

for n in data:
    sectionA, sectionB = n.split(',')
    sectionASet = findRangeForSection(sectionA)
    sectionBSet = findRangeForSection(sectionB)
    if sectionASet.issubset(sectionBSet) or sectionBSet.issubset(sectionASet):
        countSubsets += 1
    if (sectionASet & sectionBSet):
        countOverlap += 1

print(countSubsets)
#494

print(countOverlap)
#833