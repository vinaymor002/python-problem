first_line = [int(x) for x in raw_input().split()]

N = first_line[0]
M = first_line[1]

matrix = []

while N > 0:
    N -= 1
    matrix.append([int(x) for x in raw_input().split()])

Q = int(raw_input())

while Q > 0:
    Q -= 1
    X = int(raw_input())
    column_index = -1
    row_index = -1

    for index, row in enumerate(matrix):
        if row[0] <= X <= row[-1]:
            if X in row:
                column_index = row.index(X)
                row_index = index
                break
        if row[0] > X:
            break

    print row_index, column_index