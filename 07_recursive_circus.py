class program:
    def __init__(self, name, weight, programs_above={}):
        self.name = name
        self.weight = weight
        self.programs_above = programs_above

    def __str__(self):
        return "%s %s -> %s" % (self.name, self.weight, str(self.programs_above))

    def remove_above(self, above):
        if above in self.programs_above:
            self.programs_above.remove(above)


class tree_node:
    def __init__(self, program, programs_above):
        self.program = program_list
        self.programs_above = programs_above


example = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''

def parse_line(input_line):
    tokens = input_line.strip().split('->')
    try:
        name, weight = tokens[0].strip().split(' ')
    except ValueError as e:
        print(tokens)
        raise(e)

    if len(tokens) > 1:
        programs_above = {x.strip() for x in tokens[1].split(',')}
        return program(name.strip(), weight, programs_above)
    else:
        return program(name.strip(), weight)

def parse_text(input_text):
    return [parse_line(line) for line in input_text.strip().split('\n')]

def trim_programs(program_list):
    trimmed_programs = [p for p in program_list if p.programs_above]
    leaf_programs = {p.name for p in program_list if not p.programs_above}
    if len(trimmed_programs) == 1:
        return trimmed_programs[0].name
    for p in trimmed_programs:
        p.programs_above.difference_update(leaf_programs)
    return trim_programs(trimmed_programs)

print(trim_programs(parse_text(example)))
programs = []
with open('07_input.txt','r') as input_file:
    programs = parse_text(input_file.read())
print(trim_programs(programs))
