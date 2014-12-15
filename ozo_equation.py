import math

T = [int(x) for x in raw_input().split()][0]


def find_sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s


while T > 0:
    T -= 1
    N = [int(x) for x in raw_input().split()][0]
    sqrt_of_N = long(math.sqrt(N))
    sqrt_of_half_N = long(math.sqrt(N / 2))

    for x in xrange(sqrt_of_half_N, sqrt_of_N + 1):
        b = find_sum_of_digits(x)
        lhs = (x * (x + b))
        if lhs == N:
            print x
            break
    else:
        print -1