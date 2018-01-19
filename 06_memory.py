example = [0, 2, 7, 0]
examples = [[2, 4, 1, 2],
            [3, 1, 2, 3],
            [0, 2, 3, 4],
            [1, 3, 4, 1]]
test = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]

def redistribute(original_banks):
    banks = list(original_banks)
    i = banks.index(max(banks))
    blocks = banks[i]
    banks[i] = 0
    while blocks > 0:
        i = (i+1) % len(banks)
        banks[i] += 1
        blocks -= 1
    return banks

def all_redistributions(initial_bank):
    combinations = {str(initial_bank)}
    new_combination = redistribute(initial_bank)
    while str(new_combination) not in combinations:
        combinations.add(str(new_combination))
        new_combination = redistribute(new_combination)
    return combinations

combinations = all_redistributions(test)
#print(combinations)
print(len(combinations))
