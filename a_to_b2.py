from math import fmod

N = [int(x) for x in raw_input().split()][0]
A = [int(x) for x in raw_input().split()]
Q = [int(x) for x in raw_input().split()][0]


def generate_B():
    product = 1
    for i in A:
        product *= i
    return [(product / i) for i in A]


B = generate_B()

dirty_A = False
while Q > 0:
    Q -= 1
    query = [int(x) for x in raw_input().split()]

    if query.__len__() == 3:
        A[query[1] - 1] = query[2]
        dirty_A = True
    else:
        if dirty_A:
            B = generate_B()
            dirty_A = False
        print '{0:.0f}'.format(fmod(B[query[1] - 1], pow(10, 9) + 7))




