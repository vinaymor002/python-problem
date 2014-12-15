from math import sqrt


first_line = [int(x) for x in raw_input().split()]

pp = 2
ep = [pp]
pp += 1
tp = [pp]
ss = [2]
lim = pow(10, 5)
while pp < int(lim):
    pp += ss[0]
    test = True
    sqrtpp = sqrt(pp)
    for a in tp:
        if a > sqrtpp:
            break
        if pp % a == 0:
            test = False
            break
    if test:
        tp.append(pp)
ep.reverse()
[tp.insert(0, a) for a in ep]

for i in range(first_line[0]):
    next_input = [int(x) for x in raw_input().split()]
    result = []
    if next_input[0] is 1:
        result.append(str(1))
    else:
        for j in range(next_input[0]):
            result.append(str(tp[j]))

    print ' '.join(result)