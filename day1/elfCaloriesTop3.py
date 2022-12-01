import numpy as np

def checkTopThree(currCals, top):
    lowest = min(top)
    print(top, currCals)
    if lowest < currCals:
        top[top.index(lowest)] = currCals
        print(f"swapping {currCals} for {lowest}")
    return top

receiveInput = True
calArray = []

while (receiveInput):
    inp = str(input())
    if inp == "done":
        receiveInput = False
    elif inp == "":
        calArray.append(0)
    else:
        calArray.append(int(inp))
  

topThree = [0,0,0]
currElfCals = 0
for index, cal in enumerate(calArray):
    currElfCals += cal
    if cal == 0 or index == len(calArray) - 1:
        top = checkTopThree(currElfCals, topThree)
        currElfCals = 0

topThreeTotal = topThree[0] + topThree[1] + topThree[2]
print(f"Top three calories: {topThreeTotal}")