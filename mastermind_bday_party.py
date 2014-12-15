import math

first_line = [int(x) for x in raw_input().split()]
T = first_line[0]


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


prime_no = []
while T > 0:
    second_line = [int(x) for x in raw_input().split()]
    start = second_line[0]
    end = second_line[1]
    total = end - start + 1
    for i in range(start, end + 1):
        if i == 1:
            continue
        elif i in prime_no or is_prime(i):
            if i not in prime_no:
                prime_no.append(i)
            total -= 1
        elif i == 4:
            total -= 1

    print total
    T -= 1