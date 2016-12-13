
maze=[]
OPEN_SPACE = " "
WALL = "#"

def compute(x,y,designer_number):
    res = x*x + 3*x + 2*x*y + y + y*y
    res = res + designer_number

    # print "res",bin(res)
    BIG = 0xfffffffe

    def check(var,pos):
        # this was harder for me than it should have
        # been have not been bit twiddles in a while
        # http://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit-in-c-c
        # print "check",pos, (var >> pos) & 1;
        return (var >> pos) & 1

    # print "len of res in bits", res.bit_length()
    one_count = 0
    for i in range(res.bit_length()):
        if check(res,i)==1:
            one_count = one_count + 1
    # print "one count", one_count
    if one_count%2==0:
        return OPEN_SPACE
    else:
        return WALL

def set_value(x,y,value):
    maze[y][x] = value

# maze in puzzle is at least 31 x 39
# since that is target
def setup_maze():
    for i in range(42):
        tmp = []
        for j in range(42):
            tmp.append(0)
        maze.append(tmp)

def print_maze():
    for i in range(40):
        this_x = maze[i]
        for j in range(40):
            print this_x[j],
        print


DESIGNER_NUMBER = 1362

START_X = 1
START_Y = 1
TARGET_X = 31
TARGET_Y = 39

setup_maze()
print_maze()

for i in range(40):
    for j in range(40):
        x = j
        y = i
        res = compute(x,y,DESIGNER_NUMBER)
        # print x,y,res
        set_value(x,y,res)

set_value(TARGET_X,TARGET_Y,"T")

print_maze()
