
class State8080():
    def __init__():
        self.sp = 0
        self.pc = 0
        self.memory = []
        self.int_enable = 0
        self.cc = ConditionCodes()

    def do_instruction():
        pass
        #TODO: Input hexcode and do the instruction


class ConditionCodes():
    '''Contains different flags to help the program
    '''
    def __init__():
        self.z = 1 # (zero) set to 1 when the result is equal to zero
        self.s = 1 # (sign) set to 1 when bit 7 (the most significant bit or MSB) of the math instruction is set
        self.p = 1 # (parity) is set when the answer has even parity, clear when odd parity
        self.cy = 1 # (carry) set to 1 when the instruction resulted in a carry out or borrow into the high order bit
        self.ac = 1 # Space Invaders doesnt use this
        self.pad = 3 # Dunno yet

def emulate_8080(state):
    opcode = state.memory[state.pc]

    if opcode == 0x00: # NOP
        pass
    if opcode == 0x01: # B <- byte 3, C <- byte 2
        state.c = opcode[1]
        state.b = opcode[2]
        state.pc += 2
        pass
    if opcode == 0x41:
        state.b = state.c #MOV B,C
    if opcode == 0x42:
        state.b = state.d #MOV B,D
    if opcode == 0x43:
        state.b = state.e #MOV B,E
    if opcode == 0x80: # ADD B
        answer = state.a + state.b
        # If answer is zero set flag to zero, else clear flag
        if (answer and 0xff) == 0:
            state.cc.z = 1
        else:
            state.cc.z = 0
 

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
        elif opCode == 0xc3:
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

