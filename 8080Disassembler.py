

def loadBinaryFile():
    # load file.
    with open("rom\invaders.h", "rb") as f:
        fileBuffer = f.read()

    # convert binary list to hex.
    hexList = []
    for i in fileBuffer:
        hexList.append(hex(i))
    return hexList


def test(hexList):
    counter = 0
    while hexList.__len__() >= 1:
        opCode = hexList.pop(0)
        #print(byte)

        if opCode == hex(0):
            prettyPrint(opCode, "NOP", 1, counter)
        elif opCode == "0xc3":
            prettyPrint(opCode, "JMP", 3, counter)
        else:
            print("its not")
            break

        counter += 1

def prettyPrint(OpCode, instruction, size, counter):
    print(hex(counter), OpCode, "\t", instruction)

def strip0x(s):
    return s[:2]


if __name__ == "__main__":
    hexList = loadBinaryFile()

    test(hexList)

