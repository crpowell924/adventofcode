receiveInput = True

trees = []
while (receiveInput):
    heights = str(input())
    if (heights == 'done'):
        receiveInput = False
        break
    trees.append(list(heights))


def checkLeft (y, x, arr):
    tree = arr[y][x]
    for i in range(0, x):
        if (tree <= arr[y][i]):
            return False
    return True

def checkRight (y, x, arr):
    tree = arr[y][x]
    rowLen = len(arr[y])
    for i in range(x+1, rowLen):
        if (tree <= arr[y][i]):
            return False
    return True

def checkDown (y, x, arr):
    tree = arr[y][x]
    colLen = len(arr)
    for i in range(y+1, colLen):
        if (tree <= arr[i][x]):
            return False
    return True

def checkUp (y, x, arr):
    tree = arr[y][x]
    for i in range(0, y):
        if (tree <= arr[i][x]):
            return False
    return True

totalVis = 0

for r, row in enumerate(trees):
    for t, tree in enumerate(row):
        visible = checkLeft(r, t, trees) or checkRight(r, t, trees) or checkDown(r, t, trees) or checkUp(r, t, trees)
        if visible:
            totalVis += 1
print(totalVis)