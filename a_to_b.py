N = [int(x) for x in raw_input().split()][0]
A = [int(x) for x in raw_input().split()]
Q = [int(x) for x in raw_input().split()][0]


# def generate_B():
#     for i in range(N):
#         B[i] = 1
#         for j in range(N):
#             if i != j:
#                 B[i] *= A[j]
product = 1


def generate_B():
    global product
    zero_count = 0
    product = 1
    for i in A:
        if i == 0:
            zero_count += 1
            if zero_count > 1:
                break
            continue
        else:
            product *= i

    if zero_count > 1:
        return [0] * N
    elif zero_count == 1:
        tmp = []
        for i in A:
            if i == 0:
                tmp.append(product)
            else:
                tmp.append(0)
        return tmp
    else:
        return [(product / i) for i in A]


B = generate_B()

dirty_A = False
while Q > 0:
    Q -= 1
    query = [int(x) for x in raw_input().split()]

    if query.__len__() == 3:
        product *=
        A[query[1] - 1] = query[2]
        dirty_A = True
    else:
        if dirty_A:
            B = generate_B()
            dirty_A = False
        print '{0:.0f}'.format(B[query[1] - 1] % (pow(10, 9) + 7))