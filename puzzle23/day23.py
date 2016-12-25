
import sys

DEBUG = True

data = open("input.txt","r").readlines()
import string
data = map(string.strip,data)

class State:
    def __init__(self):
        self.pc = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.output = []
    def cpy(self):
        s = State()
        s.pc = self.pc
        s.a = self.a
        s.b = self.b
        s.c = self.c
        s.d = self.d
        for i in range(len(self.output)):
            s.output.append(self.output[i])
        return s
    def __repr__(self):
        return "pc:{} a:{} b:{} c:{} d:{}".format(self.pc,self.a,self.b,self.c,self.d)

def is_int(s):
    try:
        val = int(s)
        return True
    except:
        return False

def set_register_to_int(state,new_state,register,val):
    if register == "a":
        new_state.a = val
    elif register == "b":
        new_state.b = val
    elif register == "c":
        new_state.c = val
    elif register == "d":
        new_state.d = val
    else:
        print "INVALID dst", state,new_state,register,val
        sys.exit(0)

def get_val_from_state(state,register):
    if register =="a":
        return state.a
    elif register == "b":
        return state.b
    elif register =="c":
        return state.c
    elif register =="d":
        return state.d
    else:
        print "INVALID src",state,register
        sys.exit(0)

def i_cpy(instr,state):
    data = instr.split()
    if DEBUG:
        print "i_cpy called"
        print "src first, dst second", data
    src_arg = data[1]
    dst_arg = data[2]
    # should be src then dst
    new_state = state.cpy()
    if is_int(src_arg):
        set_register_to_int(state,new_state,dst_arg,int(src_arg))
    else:
        src_val = get_val_from_state(state, src_arg)
        set_register_to_int(state,new_state,dst_arg,int(src_val))

    new_state.pc = new_state.pc+1
    return new_state

def i_inc(instr,state):
    if DEBUG:
        print "i_inc called"
    data = instr.split()
    src_arg = data[1]
    new_state = state.cpy()
    val_to_inc = get_val_from_state(state,src_arg)
    val_to_inc = val_to_inc + 1
    set_register_to_int(state,new_state,src_arg,val_to_inc)
    new_state.pc = new_state.pc + 1
    return new_state

def i_dec(instr,state):
    data = instr.split()
    src_arg = data[1]
    if DEBUG:
        print "i_dec called", src_arg

    new_state = state.cpy()
    val_to_inc = get_val_from_state(state,src_arg)
    val_to_inc = val_to_inc - 1
    set_register_to_int(state,new_state,src_arg,val_to_inc)
    new_state.pc = new_state.pc + 1
    return new_state

def i_jnz(instr,state):
    data = instr.split()
    argx = data[1]
    argy = data[2]
    if DEBUG:
        print "i_jnz called", argx, argy

    new_state = state.cpy()

    if is_int(argx):
        xval = int(argx)
    else:
        xval = int(get_val_from_state(state,argx))

    if is_int(argy):
        yval = int(argy)
    else:
        yval = int(get_val_from_state(state,argy))

    if xval != 0:
        if DEBUG:
            print "XVAL IS", xval, "bumping pc by", yval
        new_state.pc = new_state.pc + yval
    else:
        if DEBUG:
            print "no jump"
        new_state.pc = new_state.pc+1

    return new_state

def i_out(instr,state):
    if DEBUG:
        print "i_out called"
    data = instr.split()
    arg = data[1]

    outval = None
    if is_int(arg):
        outval = int(arg)
    else:
        outval = int(get_val_from_state(state,arg))

    new_state = state.cpy()
    new_state.pc = new_state.pc + 1

    # print outval,
    # sys.stdout.flush()
    new_state.output.append(outval)

    return new_state

def i_tgl(instr,state,program):
    if DEBUG:
        print "i_tgl called"
    data = instr.split()
    arg = data[1]
    if is_int(arg):
        outval = int(arg)
    else:
        outval = int(get_val_from_state(state,arg))

    try:
        program[state.pc+outval]
    except:
        new_state = state.cpy()
        new_state.pc = new_state.pc + 1
        return new_state

    if DEBUG:
        print "tgl", state.pc, outval, program[state.pc+outval]
        print "tgl",program

    cs = program[state.pc+outval]
    if cs.startswith("tgl") or cs.startswith("dec"):
        # need to change this to an inc!
        junk = program[state.pc+outval].split()
        junk[0] = "inc"
        program[state.pc+outval] = " ".join(junk)
        print "tgl changed!", program[state.pc+outval]
    elif cs.startswith("inc"):
        junk = program[state.pc+outval].split()
        junk[0] = "dec"
        program[state.pc+outval] = " ".join(junk)
        print "tgl changed!", program[state.pc+outval]
    elif cs.startswith("cpy"):
        junk = program[state.pc+outval].split()
        junk[0] = "jnz"
        program[state.pc+outval] = " ".join(junk)
        print "tgl changed!", program[state.pc+outval]
    elif cs.startswith("jnz"):
        junk = program[state.pc+outval].split()
        junk[0] = "cpy"
        program[state.pc+outval] = " ".join(junk)
        print "tgl changed!", program[state.pc+outval]


    new_state = state.cpy()
    new_state.pc = new_state.pc + 1

    return new_state


def execute(program,state):
    instr = program[state.pc]
    if DEBUG:
        print "execute",instr
        print "state",state
    if instr.startswith("cpy"):
        new_state = i_cpy(instr,state)
    elif instr.startswith("inc"):
        new_state = i_inc(instr,state)
    elif instr.startswith("dec"):
        new_state = i_dec(instr,state)
    elif instr.startswith("jnz"):
        new_state = i_jnz(instr,state)
    elif instr.startswith("out"):
        new_state = i_out(instr,state)
    elif instr.startswith("tgl"):
        new_state = i_tgl(instr,state,program)
    else:
        print "ERR: instr not known", instr
        import sys
        sys.exit(0)
    return new_state


print "len of state",len(data)
state = State()
state.a = 7
count = 0
while True:
    if DEBUG:
        print "------------ state->",state
    new_state = execute(data,state)
    state = new_state

    if DEBUG:
        print "**********  state ->",state
    count = count + 1
    if count == 8:
        # break
        pass

    if  DEBUG:
        print "PC dbg", state.pc, len(data)

    #if state.pc == 16:
    #    if DEBUG:
    #        print "state.pc was 16 stopping"
    #        break

    if state.pc >= len(data):
        if DEBUG:
            print "state.pc is too large halting"
            break

print "final data",data
print "final state", state
