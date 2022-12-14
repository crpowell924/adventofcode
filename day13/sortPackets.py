import ast
import functools

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

packets.append([[2]])
packets.append([[6]])
sorted_packets = sorted(packets, key=functools.cmp_to_key(comparePacketsRecursively))

decoder_key = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
print(decoder_key)