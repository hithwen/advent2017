from collections import defaultdict

def parse_input(text):
    talk_to = defaultdict(set)
    for line in text.strip().splitlines():
        origin, dest = line.split('<->')
        origin = int(origin.strip())
        dest = eval('{%s}' % dest)
        talk_to[origin].update(dest)
        for d in dest:
            talk_to[d].add(origin)
    return talk_to

def group_0(talk_to):
    programs = talk_to[0]
    new_programs = programs
    while len(new_programs) > 0:
        added_programs = set()
        for p in new_programs:
            added_programs.update(talk_to[p])
        new_programs = added_programs.difference(programs)
        programs.update(new_programs)
    return programs


example = '''
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''

with open('12_input.txt','r') as input_file:
    print(len(group_0(parse_input(input_file.read()))))
#print(len(group_0(parse_input(example))))
