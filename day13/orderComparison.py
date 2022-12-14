import ast

receiveInput = True

packets = []
while (receiveInput):
    packet = input()
    if (packet == 'done'):
        receiveInput = False
        break
    elif (packet != ''):
        packet = ast.literal_eval(packet)
        packets.append(packet)


print(f"packets {packets}")

def comparePacketsRecursively(p1, p2):
    print(f"comparing {p1}, {p2}")
    if (isinstance(p1, int) & isinstance(p2, int)):
        print('both ints', p1, p2)
        return p1 - p2
    elif (isinstance(p1, list) & isinstance(p2, list)):
        for i1, i2 in zip(p1, p2):
            n = comparePacketsRecursively(i1,i2)
            if n != 0:
                return n
        return len(p1) - len(p2)
    elif (isinstance(p1, list) & isinstance(p2, int)):
        return comparePacketsRecursively(p1, [p2])
    elif (isinstance(p1, int) & isinstance(p2, list)):
        return comparePacketsRecursively([p1], p2)


correctOrder = 0
for i in range(0,len(packets),2):
    comparison = comparePacketsRecursively(packets[i], packets[i+1])
    print(comparison)
    if comparison < 0:
        correctOrder += (i + 2) / 2

print(f"Packets in correct order: {correctOrder}")