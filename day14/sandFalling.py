# import ast

receiveInput = True

packets = []
while (receiveInput):
    packet = str(input())
    if (packet == 'done'):
        receiveInput = False
        break
    packets.append(packet)