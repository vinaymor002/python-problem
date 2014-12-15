import math

T = [long(x) for x in raw_input().split()][0]
mapper = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 2,
    5: 2,
    6: 3,
    7: 3,
    8: 4,
    9: 4
}


def get_magic_number_count(digits):
    if digits is 2:
        return 4
    return pow(10, digits - 2) * 4 + 6 * get_magic_number_count(digits - 1)


for i in range(T):
    N = [long(x) for x in raw_input().split()][0]
    total_count = 0
    digit_count = int(math.log10(N)) + 1
    magic_number_count = get_magic_number_count(digits=digit_count)

    divisor = pow(10, digit_count - 2)
    dividend = N / divisor
    while N > 0:
        if digit_count > 1:
            total_count += divisor * mapper.get(dividend) + magic_number_count * (dividend - mapper.get(dividend))
            N %= divisor
            if (N / 10) == 0:
                digit_count = 0
                divisor = 0
                dividend = N
            else:
                digit_count = int(math.log10(N))
                divisor = pow(10, digit_count)
                dividend = N / divisor
            magic_number_count = get_magic_number_count(digits=digit_count)

    print total_count