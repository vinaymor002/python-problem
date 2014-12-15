T = int(raw_input())

while T > 0:
    n_k = raw_input()
    N = int(n_k.split()[0])
    K = int(n_k.split()[1])
    numbers = [int(i) for i in raw_input().split()]
    best = 0
    for index, n in enumerate(numbers):
        i = index
        _sum = 0
        while i < numbers.__len__():
            if numbers[i] > 0:
                _sum += numbers[i]
                i += (K + 1)
            else:
                i += 1
        best = max(best, _sum)
    print best

    T -= 1
