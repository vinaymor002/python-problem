first_line = [int(x) for x in raw_input().split()]

T = first_line[0]

for i in range(T):
    line = [int(x) for x in raw_input().split()]
    index = line[0]
    N = line[1]
    if N == 0 and index == 2:
        print 2
    elif (N % 2 == 0 and index == 1) or (N % 2 == 1 and index in (0, 2)):
        print 1
    elif (N % 2 == 1 and index == 1) or (N % 2 == 0 and index in (0, 2)):
        print 0
