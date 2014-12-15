import itertools


first_line = [int(x) for x in raw_input().split()]
N = first_line[0]

sequence = [int(x) for x in raw_input().split()]
Q = [int(x) for x in raw_input().split()][0]

sum_count_repo = [0] * pow(10, 5)
sum_repo = []
for i in range(1, N + 1):
    subsets = set(itertools.combinations(sequence, i))
    for sub_set in subsets:
        set_sum = sum(sub_set)
        if sum_count_repo[set_sum] == 0:
            sum_repo.append(set_sum)
        sum_count_repo[set_sum] += 1

while Q > 0:
    Q -= 1
    A = [int(x) for x in raw_input().split()][0]
    min_xor = float("inf")
    for set_sum in sum_repo:
        a_xor_set_sum = (set_sum ^ A)
        if min_xor > a_xor_set_sum:
            min_xor = a_xor_set_sum
            result_sum = set_sum
    print result_sum, sum_count_repo[result_sum]