from aocd import get_data
from treelib import Node, Tree
import copy

rawData = get_data(day=7, year=2022)
data = rawData.splitlines()

tree = Tree()
tree.create_node('/', 0)
currentDirectory = 0

def addSubDirectoryAmounts(directory, subDirectory):
    folderSizes.update({directory: folderSizes[directory] + folderSizes[subDirectory]})

def findOtherUsesOfSubDirectory(initialSubDirectory, subDirectoryToFind):
    for otherUsesOfSubDirectory in subDirectoriesToAdd:
        if otherUsesOfSubDirectory[0] == subDirectoryToFind:
            addSubDirectoryAmounts(initialSubDirectory, otherUsesOfSubDirectory[1])
            findOtherUsesOfSubDirectory(initialSubDirectory, otherUsesOfSubDirectory[1])

for idx, command in enumerate(data):
    if "$ cd" in command:
        if ".." not in command:
            subTree = tree.subtree(currentDirectory)
            for node in subTree.leaves():
                if node.tag == command.split()[-1]:
                    currentDirectory = node.identifier
        else:
            currentDirectory = tree.parent(currentDirectory).identifier
    elif "dir" in command:
        tree.create_node(command.split()[-1], idx, parent=currentDirectory)
    elif "$ ls" not in command:
        tree.create_node(command, idx, parent=currentDirectory)

folderSizes = {0: 0}
subDirectoriesToAdd = []

for i in tree.expand_tree():
    node = tree.get_node(i)
    parent = tree.parent(node.identifier)

    if (node.identifier != 0):
        folderSizes.setdefault(parent.identifier, 0)
        currentSize = folderSizes[parent.identifier]
        if " " in node.tag:
            currentSize += int(node.tag.split()[0])
            folderSizes.update({parent.identifier: currentSize})
        elif tree.children(node.identifier):
            subDirectoriesToAdd.append([parent.identifier, node.identifier])

for subdirectory in subDirectoriesToAdd:
    addSubDirectoryAmounts(subdirectory[0], subdirectory[1])
    findOtherUsesOfSubDirectory(subdirectory[0], subdirectory[1])

totalSumOfFoldersUnder100000 = 0

for index in folderSizes:
    if folderSizes[index] <= 100000:
        totalSumOfFoldersUnder100000 += folderSizes[index]

print(totalSumOfFoldersUnder100000)
#1667443

additionalSpaceNeeded = 30000000 - (70000000 - folderSizes[0])

folderToDeleteSize = folderSizes[0]
for index in folderSizes:
    if folderSizes[index] < folderToDeleteSize and folderSizes[index] > additionalSpaceNeeded:
        folderToDeleteSize = folderSizes[index]

print(folderToDeleteSize)
#8998590