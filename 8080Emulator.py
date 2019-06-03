
class State8080():
    def __init__(self):
        '''
        A is called an accumulator
        BC, DE and HL are pairs which can do 16 bit instructions. 
        '''

        # registers
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.h = 0
        self.l = 0

        # stack pointer.
        self.sp = 0

        # program counter.
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
    def __init__(self):
        self.z = 1 # (zero) set to 1 when the result is equal to zero
        self.s = 1 # (sign) set to 1 when bit 7 (the most significant bit or MSB) of the math instruction is set
        self.p = 1 # (parity) is set when the answer has even parity, clear when odd parity
        self.cy = 1 # (carry) set to 1 when the instruction resulted in a carry out or borrow into the high order bit
        self.ac = 1 # Space Invaders doesnt use this
        self.pad = 3 # Dunno yet

def emulate_8080(state):
    #opcode = state.memory[state.pc]
    opcode = "0x81"
    if opcode == "0x0": # NOP
        print(opcode)
        pass
    if opcode == "0x01": # B <- byte 3, C <- byte 2
        print(opcode)
        state.c = opcode[1]
        state.b = opcode[2]
        state.pc += 2
        pass
    if opcode == "0x41":
        print(opcode)
        state.b = state.c #MOV B,C
    if opcode == "0x42":
        print(opcode)
        state.b = state.d #MOV B,D
    if opcode == "0x43":
        print(opcode)
        state.b = state.e #MOV B,E
    if opcode == "0x80": # ADD B
        print(opcode)    
        answer = state.a + state.b
        # ZERO FLAG: if answer is zero set flag to ONE, else clear flag
        if (answer and 0xff) == 0:
            state.cc.z = 1
        else:
            state.cc.z = 0
        # SIGN FLAG: if bit 7 is set, set the sign flag, else clear it
        if (answer and 0x80):
            state.cc.s = 1
        else:
            state.cc.s = 0
        # CARRY FLAG:
        if (answer > 0xff):  
            state.cc.cy = 1;    
        else:    
            state.cc.cy = 0;    
        # Parity is handled by a subroutine    
        #state.cc.p = Parity(answer & 0xff)
        state.a = answer & 0xff
    if opcode == "0x81":
            answer = state.a + state.c    
            state.cc.z = 1 if ((answer & 0xff) == 0) else 0
            state.cc.s = 1 if ((answer & 0x80) != 0) else 0   
            state.cc.cy = 1 if (answer > 0xff) else 0
            #state.cc.p = Parity(answer&0xff)  
            state.a = answer & 0xff   
    if opcode == "0xc6": # A <- A + byte
        answer = state.a + opcode[1]
        state.cc.z = 1 if ((answer & 0xff) == 0) else 0
        state.cc.s = 1 if ((answer & 0x80) != 0) else 0   
        state.cc.cy = 1 if (answer > 0xff) else 0

def loadBinaryFile(state):
    # load file.
    with open("rom/invaders", "rb") as f:
        fileBuffer = f.read()

    # convert binary list to hex.
    hexList = []
    for i in fileBuffer:
        hexList.append(hex(i))
    state.memory = hexList
    return hexList


if __name__ == "__main__":
    state = State8080()
    hexList = loadBinaryFile(state)
    emulate_8080(state)
    print(state.cc.z)

