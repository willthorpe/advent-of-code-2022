from aocd import get_data

rawData = get_data(day=6, year=2022)
data = rawData.splitlines()[0]

def findPositionOfMarker(data, requiredDistinctCharacters):
    marker = data[0:requiredDistinctCharacters]
    foundMarker = False
    markerPosition = requiredDistinctCharacters

    for i in range(requiredDistinctCharacters, len(data)):
        if foundMarker == False:
            if len(set(marker)) == len(marker):
                foundMarker = True
                markerPosition = i
            else:
                marker = marker[1:requiredDistinctCharacters]
                marker += data[i]
    return markerPosition

print(findPositionOfMarker(data, 4))
#1953

print(findPositionOfMarker(data, 14))
#2301