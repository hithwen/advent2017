examples = [
'{}', #score of 1.
'{{{}}}', #score of 1 + 2 + 3 = 6.
'{{},{}}', #score of 1 + 2 + 2 = 5.
'{{{},{},{{}}}}', #score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
'{<a>,<a>,<a>,<a>}', #score of 1.
'{{<ab>},{<ab>},{<ab>},{<ab>}}', #score of 1 + 2 + 2 + 2 + 2 = 9.
'{{<!!>},{<!!>},{<!!>},{<!!>}}', #score of 1 + 2 + 2 + 2 + 2 = 9.
'{{<a!>},{<a!>},{<a!>},{<ab>}}'
]

def find_groups(input_stream):
    open_groups = 0
    open_garbage = False
    cancel_next = False
    score = 0
    for c in input_stream:
        if cancel_next:
            cancel_next = False
        elif c == '!':
            cancel_next = True
        elif not open_garbage:
            if c == '<':
                open_garbage = True
            elif c == '{':
                open_groups += 1
            elif c == '}':
                score += open_groups
                open_groups -= 1
        elif c == '>':
            open_garbage = False
    return score


#for e in examples:
#    print(e, find_groups(e))
input_stream = ''
with open('09_input.txt','r') as input_file:
    input_stream = input_file.read().strip()
print(find_groups(input_stream))
