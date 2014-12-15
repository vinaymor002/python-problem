first_line = [int(x) for x in raw_input().split()]
N = first_line[0]
my_list = [0] * N
for x in raw_input().split():
    int_x = int(x)
    if my_list[int_x] == 1:
        duplicate = int_x
        break
    else:
        my_list[int_x] = 1

print duplicate, ' '.join(map(str, range(1, N)))