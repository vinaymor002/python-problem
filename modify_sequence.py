numbers = [int(x) for x in raw_input().split()][0]
integer_list = [int(x) for x in raw_input().split()]

yes = True
for i in range(numbers - 1):
    integer_list[i + 1] -= integer_list[i]
    if integer_list[i + 1] < 0:
        yes = False

if yes is False or integer_list[numbers - 1] != 0:
    print 'NO'
else:
    print 'YES'