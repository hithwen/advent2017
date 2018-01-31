def parse_input(input_text):
    return eval('{%s}' % input_text.strip().replace('\n', ', '))

def severity(firewall_map):
    severity = 0
    scanners_position = {k: 0 for k in firewall_map.keys()}
    scanners_direction = {k: 1 for k in firewall_map.keys()}

    for picosecond in range(0, max(list(firewall_map.keys())) + 1):
        # nanosecond is also the layer the packet is entering
        for k in firewall_map.keys():
            # Did it get caught ?
            if picosecond == k and scanners_position[k] == 0:
                severity += k * firewall_map[k]
            # Move scanners
            if scanners_position[k] == (firewall_map[k] - 1):
                scanners_direction[k] = -1
            if scanners_position[k] == 0 and scanners_direction[k] == -1:
                scanners_direction[k] = 1
            scanners_position[k] += scanners_direction[k]
    return severity

example = '''
0: 3
1: 2
4: 4
6: 4
'''

problem_input = '''
0: 3
1: 2
2: 4
4: 6
6: 4
8: 6
10: 5
12: 8
14: 8
16: 6
18: 8
20: 6
22: 10
24: 8
26: 12
28: 12
30: 8
32: 12
34: 8
36: 14
38: 12
40: 18
42: 12
44: 12
46: 9
48: 14
50: 18
52: 10
54: 14
56: 12
58: 12
60: 14
64: 14
68: 12
70: 17
72: 14
74: 12
76: 14
78: 14
82: 14
84: 14
94: 14
96: 14
'''

print(severity(parse_input(problem_input)))
