T = int(raw_input())


def ignore_count(i_square, X, Y, ignored_numbers):
    starting_multiplier = X / i_square if X % i_square is 0 else X / i_square + 1
    ending_multiplier = Y / i_square
    for j in range(starting_multiplier, ending_multiplier + 1):
        _number = j * i_square
        if _number not in ignored_numbers:
            ignored_numbers.append(_number)


def ignore_perfect_squares(i_square, X, Y, ignored_i):
    counter = 1
    while True:
        _ignore_number = i_square * counter
        if _ignore_number <= Y:
            ignored_i.append(_ignore_number)
            counter += 1
        else:
            break


while T > 0:
    i = 2
    ignored_i = []
    ignored_numbers = []
    T -= 1
    input_line = [int(x) for x in raw_input().split()]

    X = input_line[0]
    Y = input_line[1]

    count = 0

    while True:
        if i in ignored_i:
            i += 1
            continue
        i_square = i * i
        if i_square > Y:
            break
        ignore_count(i_square, X, Y, ignored_numbers)
        ignore_perfect_squares(i_square, X, Y, ignored_i)
        i += 1

    print Y - X + 1 - ignored_numbers.__len__()


