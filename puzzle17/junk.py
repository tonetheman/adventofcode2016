
import md5

inp = "hhhxzeay"
OPEN = "bcdef"

def get_valid_for_spot(state):
    y = state[1]
    x = state[0]
    path = state[2]

    m = md5.new()
    m.update(inp +  "".join(path))
    h =m.hexdigest()
    my_dirs = []
    if y > 0 and h[0] in OPEN:
        my_dirs.append((state[0],state[1]-1,path+tuple("U")))
    if y < 3 and h[1] in OPEN:
        my_dirs.append((state[0],state[1]+1,path+tuple("D")))
    if x > 0 and h[2] in OPEN:
        my_dirs.append((state[0]-1,state[1],path+tuple("L")))
    if x < 3 and h[3] in OPEN:
        my_dirs.append((state[0]+1,state[1],path+tuple("R")))

    return my_dirs

valid = set()
# pos, pos, must be 3 3 to find a spot
stack = [(0,0,())]
print stack
while stack:
    state = stack.pop()
    print "popped", state, state[0], state[1]
    if state[0] == state[1] == 3:
        valid.add("".join(state[2]))
        continue
    m = get_valid_for_spot(state)
    for myd in m:
        stack.append(myd)

print(sorted(valid, key=len)[0])
