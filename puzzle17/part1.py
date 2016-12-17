import md5

puzzle_input = "hhhxzeay"

def is_open(c):
    return c in ["b","c","d","e","f"]

def step(passcode):
    m = md5.new()
    m.update(passcode)
    new_code = m.hexdigest()[0:4]

    up = is_open(new_code[0])
    down = is_open(new_code[1])
    left = is_open(new_code[2])
    right = is_open(new_code[3])

    print new_code,up,down,left,right


def test():
    puzzle_input = "hijkl"

    step(puzzle_input)


test()
