N = int(raw_input())

while N > 0:
    pattern = raw_input()
    text = raw_input()
    found = 0
    pattern_dict = {}
    text_length = text.__len__()
    pattern_length = pattern.__len__()
    count = pattern_length

    if pattern_length > text_length:
        print 'NO'
        N -= 1
        continue

    for ch in pattern:
        if ch in pattern_dict:
            pattern_dict[ch] += 1
        else:
            pattern_dict[ch] = 1
    result = []
    index = 0

    for i in xrange(pattern_length):
        ch = text[i]
        if ch in pattern_dict:
            pattern_dict[ch] -= 1
            if pattern_dict[ch] >= 0:
                count -= 1

    for i in range(pattern_length, text_length):
        if found == 1:
            print 'YES'
        else:
            print 'NO'

        N -= 1
