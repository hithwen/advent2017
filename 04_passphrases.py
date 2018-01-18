def is_valid_passphrase(passphrase):
    words = passphrase.strip().split(' ')
    word_set = set()
    for w in words:
        if w in word_set:
            return False
        word_set.add(w)
    return True
    
examples = ['aa bb cc dd ee',
            'aa bb cc dd aa',
            'aa bb cc dd aaa']

#for e in examples:
#    print(e, ": ", is_valid_passphrase(e))

valid_pass = 0
with open('04_input.txt','r') as input_file:
    for passphrase in input_file.readlines():
        if is_valid_passphrase(passphrase):
            valid_pass += 1
            if not is_valid_passphrase2(passphrase):
                print("!!!!!! ", passphrase)
print(valid_pass)