T = int(raw_input())
repo = {}

i = 2
ignored_is = []


def find_numbers(i_i, X, Y, ignored_numbers):
    for i in range(X / i_i, Y / i_i + 1):
        ignore_number = i * i_i
        if X <= ignore_number <= Y:
            if ignore_number not in ignored_numbers:
                ignored_numbers.append(ignore_number)


def ignore_i(i_i, Y, ignored_is):
    for i in range(2, Y / i_i):
        _ignore_i = i * i_i
        if _ignore_i not in ignored_is:
            ignored_is.append(_ignore_i)


while T > 0:
    T -= 1
    input_line = [int(x) for x in raw_input().split()]
    i = 2
    X = input_line[0]
    Y = input_line[1]
    ignored_numbers = []
    count = 0
    ignored_numbers_count = 0
    while True:
        if i in ignored_is:
            i += 1
            continue
        i_i = i * i
        ignore_i(i_i, Y, ignored_is)
        if i_i <= Y:
            find_numbers(i_i, X, Y, ignored_numbers)
            i += 1
        else:
            break

    print Y - X + 1 - ignored_numbers.__len__()

