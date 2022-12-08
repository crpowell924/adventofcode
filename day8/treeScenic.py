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
    sscore = 0
    for i in reversed(range(0, x)):
        if (tree > arr[y][i]):
            sscore += 1 
        elif (tree <= arr[y][i]):
            sscore += 1 
            return sscore
    return sscore

def checkRight (y, x, arr):
    tree = arr[y][x]
    rowLen = len(arr[y])
    sscore = 0
    for i in range(x+1, rowLen):
        if (tree > arr[y][i]):
            sscore += 1 
        elif (tree <= arr[y][i]):
            sscore += 1 
            return sscore
    return sscore

def checkDown (y, x, arr):
    tree = arr[y][x]
    colLen = len(arr)
    sscore = 0
    for i in range(y+1, colLen):
        if (tree > arr[i][x]):
            sscore += 1 
        elif (tree <= arr[i][x]):
            sscore += 1 
            return sscore
    return sscore

def checkUp (y, x, arr):
    tree = arr[y][x]
    sscore = 0
    for i in reversed(range(0, y)):
        if (tree > arr[i][x]):
            sscore += 1 
        elif (tree <= arr[i][x]):
            sscore += 1 
            return sscore
    return sscore

highScore = 0

for r, row in enumerate(trees):
    for t, tree in enumerate(row):
        score = checkLeft(r, t, trees) * checkRight(r, t, trees) * checkDown(r, t, trees) * checkUp(r, t, trees)
        if score > highScore:
            highScore = score

print(f"Highest Scenic Score: {highScore}")