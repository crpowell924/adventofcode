
# Key:
#     A | X = rock 1pt
#     B | Y = paper 2pt
#     C | Z = scissors 3pt

receiveInput = True
score = 0
while (receiveInput):
    played = str(input())
    if (played == 'done'):
        receiveInput = False
        print(f"Final score: {score}")
        break
    played = played.split(' ')
    opp = played[0]
    resp = played[1]

    if resp == 'X':
        score += 1
        if opp == 'A':
            score += 3
        elif opp == 'B':
            score += 0
        elif opp == 'C':
            score += 6
    elif resp == 'Y':
        score += 2
        if opp == 'A':
            score += 6
        elif opp == 'B':
            score += 3
        elif opp == 'C':
            score += 0
    elif resp  == 'Z':
        score += 3
        if opp == 'A':
            score += 0
        elif opp == 'B':
            score += 6
        elif opp == 'C':
            score += 3
    print(f"Current score: {score}")
