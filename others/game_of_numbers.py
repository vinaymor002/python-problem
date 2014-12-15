import fileinput


def special(x, y):
    out = [1 for i in range(x, y + 1)]

    sqrt = int(y ** .5)
    j = 2
    while j <= sqrt:
        square = j * j
        start = x + (square - x % square) % square
        for k in range(start, y + 1, square):
            out[k - x] = 0
        j += 1
    return out

#print sys.getsizeof([0])
#print sys.getsizeof([0]*2)

lines = [l for l in fileinput.input()]

xmin = 999999
ymax = 0
for line in lines[1:]:
    x, y = [int(i) for i in line.split(' ')]
    xmin = min(x, xmin)
    ymax = max(y, ymax)

if ymax - xmin < (100 * 1024 * 1024 - 72) / 4:

    info = special(xmin, ymax)
    for line in lines[1:]:
        x, y = [int(i) for i in line.split(' ')]
        print sum(info[x - xmin:y - xmin + 1])

else:
    for line in lines[1:]:
        x, y = [int(i) for i in line.split(' ')]
        print sum(special(x, y))

