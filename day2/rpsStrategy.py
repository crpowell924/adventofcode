
# Key:
#     A = rock 1pt
#     B = paper 2pt
#     C = scissors 3pt
#     X = lose 0pt
#     Y = draw 3pt
#     Z = win 6pt


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
    strat = played[1]

    if strat == 'X':
        if opp == 'A':
            score += 3
        elif opp == 'B':
            score += 1
        elif opp == 'C':
            score += 2
    elif strat == 'Y':
        score += 3
        if opp == 'A':
            score += 1
        elif opp == 'B':
            score += 2
        elif opp == 'C':
            score += 3
    elif strat  == 'Z':
        score += 6
        if opp == 'A':
            score += 2
        elif opp == 'B':
            score += 3
        elif opp == 'C':
            score += 1
    print(f"Current score: {score}")
