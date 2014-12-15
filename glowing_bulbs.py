first_line = [int(x) for x in raw_input().split()]
T = first_line[0]
on_switches = []


def find_k_for(x):
    result = 0
    on_switch_count = on_switches.__len__()
    for i in range(1, pow(2, on_switch_count)):
        product = 1
        bit_count = 0
        for j in range(on_switch_count):
            if (i >> j) & 1:
                product *= on_switches[j]
                bit_count += 1
        if bit_count.__mod__(2) != 0:
            result += x.__div__(product)
        else:
            result -= x.__div__(product)
    return result


for i in range(T):
    line = raw_input()
    next_line = [int(x) for x in raw_input().split()]
    K = next_line[0]

    on_switches = [i + 1 for i in range(line.__len__()) if line[i] == '1']
    low = 1
    high = on_switches[-1] * pow(10, 15)

    while low <= high:
        mid = (low + high) / 2
        if K > find_k_for(mid):
            low = mid + 1
        else:
            high = mid - 1
            res = mid
    print res