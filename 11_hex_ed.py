cancelations = [['n', 's'], ['ne', 'sw'], ['se', 'nw']]
shortenings_from = [['ne', 's'], ['se', 'n'], ['nw', 's'], ['sw', 'n'],
                    ['se', 'sw'], ['ne', 'nw']]
shortening_to = ['se', 'ne', 'sw', 'nw', 's', 'n']

examples = [['ne', 'ne', 'ne'],
            ['ne', 'ne', 'sw', 'sw'],
            ['ne', 'ne', 's', 's'],
            ['se', 'sw', 'se', 'sw', 'sw']]

def reduce_path(path):
    can_reduce = True
    while(can_reduce):
        path_lenght = len(path)
        for c in cancelations:
            if c[0] in path and c[1] in path:
                path.remove(c[0])
                path.remove(c[1])
        for i, s in enumerate(shortenings_from):
            if s[0] in path and s[1] in path:
                path.remove(s[0])
                path.remove(s[1])
                path.append(shortening_to[i])
        can_reduce = len(path) != path_lenght
    return path


#for e in examples:
#    r = reduce_path(e)
#    print(r, len(r))

from input11 import path
r = reduce_path(path)
print(len(r))
