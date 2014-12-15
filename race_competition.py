T = int(raw_input())


def calculate(fuel_left, done, races):
    best = 0
    if fuel_left is 0:
        return best
    for index, race in enumerate(races):
        _done = done[:]
        count = 0
        if race[0] <= fuel_left and done[index] is False:
            _done[index] = True
            count = calculate(fuel_left - race[0] + race[1], _done, races) + 1

        best = max(best, count)
    return best


while T > 0:
    F, N = raw_input().split()
    N = int(N)
    F = int(F)
    races = []
    done = []
    while N > 0:
        races.append([int(i) for i in raw_input().split()])
        done.append(False)
        N -= 1
    print calculate(F, done, races)
    T -= 1
