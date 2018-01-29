def knot(list_size=256, lenghts=[]):
    numbers=list(range(list_size))
    current_pos = 0
    skip_size = 0
    for lenght in lenghts:
        section = []
        for i in range(current_pos, current_pos + lenght):
            section.append(numbers[i % list_size])

        for i, n in zip(range(current_pos, current_pos + lenght), reversed(section)):
            numbers[i % list_size] = n
        current_pos = (current_pos + lenght + skip_size) % list_size
        skip_size = (skip_size + 1) % list_size
    return numbers

#knoted = knot(5, [3, 4 ,1 ,5])
knoted = knot(256,[192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12])
print(knoted[0]*knoted[1])
