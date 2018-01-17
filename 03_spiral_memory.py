
def find_current_position(n, side):
    x, y = [side - 1, side -1]
    current_value = pow(side, 2)
    for i in range(0, x+1):
        #print("[%d, %d] = %d", x-i, y, current_value)
        if n == current_value:
            return [x-i, y]
        current_value -= 1

    for i in range(1, y+1):
        #print("[%d, %d] = %d", 0, y-i, current_value)
        if n == current_value:
            return [0, y-i]
        current_value -= 1

    for i in range(1, x+1):
        #print("[%d, %d] = %d", 0, i, current_value)
        if n == current_value:
            return [0, i]
        current_value -= 1

    for i in range(1, y+1):
        #print("[%d, %d] = %d", x, i, current_value)
        if n == current_value:
            return [x, i]
        current_value -= 1



def steps_in_spiral(n):
    square_side = 1
    while n > pow(square_side, 2):
        square_side += 2
    spiral_centre = square_side//2
    x, y = find_current_position(n, square_side)
    steps_required = abs(x-spiral_centre) + abs(y-spiral_centre)
    print("Request data ",n , " situated in: ", [x, y],
            ". Square centre in ", spiral_centre, 
            ". Steps required: ", steps_required)

examples = [1, 12, 23, 1024, 277678]
#steps_in_spiral(examples[2])
for e in examples:
    steps_in_spiral(e)
