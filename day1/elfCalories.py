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
  

mostCals = 0
currElfCals = 0
for cal in calArray:
    if cal != 0:
        currElfCals += cal
        if currElfCals > mostCals:
            mostCals = currElfCals
    else:
        currElfCals = 0

print(f"Most calories {mostCals}")