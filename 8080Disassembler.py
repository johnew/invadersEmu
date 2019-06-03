

def loadBinaryFile():
    # load file.
    with open("rom/invaders", "rb") as f:
        fileBuffer = f.read()

    # convert binary list to hex.
    hexList = []
    for i in fileBuffer:
        hexList.append(hex(i))
    return hexList


def test(hexList):
    ''' fuck det her tar for lang tid...
    '''
    counter = 0
    while hexList.__len__() >= 1:
        opCode = hexList.pop(0)

        if opCode == hex(0):
            prettyPrint(opCode, ["NOP"], counter)
        elif opCode == "0x01":
            prettyPrint(opCode, ["LXI B,D16", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xf":
            prettyPrint(opCode, ["RRC"], counter)
        elif opCode == "0x21":
            prettyPrint(opCode, ["LXI H,D16", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0x27":
            prettyPrint(opCode, ["DAA"], counter)
        elif opCode == "0x32":
            prettyPrint(opCode, ["STA adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0x35":
            prettyPrint(opCode, ["DCR M"], counter)
        elif opCode == "0x3a":
            prettyPrint(opCode, ["LDA adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0x3e":
            prettyPrint(opCode, ["MVI A,D8", hexList.pop(0)], counter)
        elif opCode == "0xa7":
            prettyPrint(opCode, ["ANA A"], counter)
        elif opCode == "0xaf":
            prettyPrint(opCode, ["XRA A"], counter)
        elif opCode == "0xc1":
            prettyPrint(opCode, ["POP B"], counter)
        elif opCode == "0xc2":
            prettyPrint(opCode, ["JNZ adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xc3":
            prettyPrint(opCode, ["JMP", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xc5":
            prettyPrint(opCode, ["PUSH B"], counter)
        elif opCode == "0xc6":
            prettyPrint(opCode, ["ADI D8", hexList.pop(0)], counter)
        elif opCode == "0xc9":
            prettyPrint(opCode, ["RET"], counter)
        elif opCode == "0xca":
            prettyPrint(opCode, ["JZ adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xcd":
            prettyPrint(opCode, ["CALL adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xd1":
            prettyPrint(opCode, ["POP D"], counter)
        elif opCode == "0xd2":
            prettyPrint(opCode, ["JNC adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xd5":
            prettyPrint(opCode, ["PUSH D"], counter)
        elif opCode == "0xda":
            prettyPrint(opCode, ["JC adr", hexList.pop(0), hexList.pop(0)], counter)
        elif opCode == "0xdb":
            prettyPrint(opCode, ["IN D8", hexList.pop(0)], counter)
        elif opCode == "0xe1":
            prettyPrint(opCode, ["POP H"], counter)
        elif opCode == "0xe5":
            prettyPrint(opCode, ["PUSH H"], counter)
        elif opCode == "0xf1":
            prettyPrint(opCode, ["POP PSW"], counter)
        elif opCode == "0xf5":
            prettyPrint(opCode, ["PUSH PSW"], counter)
        elif opCode == "0xfb":
            prettyPrint(opCode, ["EI"], counter)
        elif opCode == "0xfe":
            prettyPrint(opCode, ["CPI D8", hexList.pop(0)], counter)
        else:
            print("its this: ", opCode)
            break

        counter += 1

def prettyPrint(OpCode, instructions, counter):
    if (instructions.__len__() == 3):
        print(hex(counter), OpCode, "\t", instructions[0], instructions[1], instructions[2])
    elif (instructions.__len__() == 2):
        print(hex(counter), OpCode, "\t", instructions[0], instructions[1])
    else:
        print(hex(counter), OpCode, "\t", instructions[0])

    counter += (instructions.__len__()-1)

def strip0x(s):
    return s[:2]

if __name__ == "__main__":
    hexList = loadBinaryFile()
    test(hexList)
