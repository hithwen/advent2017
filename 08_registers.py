
from collections import defaultdict

registers = defaultdict(int)
def eval_line(code):
    try:
        var, op, modifier, *condition = code.strip().split(' ')
    except ValueError as e:
        print(code)
        raise e

    #print('%s = %s' % (var, registers[var]), end=' ')
    if eval('%s %s %s' % (registers[condition[1]], condition[2], condition[3])):
        if op == 'inc':
            registers[var] += int(modifier)
        else:
            registers[var] -= int(modifier)
    #print('%s = %s' % (var, registers[var]))

example = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''

code = []
with open('08_input.txt','r') as input_file:
    code = input_file.readlines()
for line in code:
    eval_line(line.strip())

#for line in example.strip().splitlines():
#    eval_line(line)
print(max(list(registers.values())))
