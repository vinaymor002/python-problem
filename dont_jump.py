def find_sequence(N, P):
    seq = []
    stack = []
    current = 0
    for p in P:
        if p not in stack:
            stack.append(p)
        else:
            return -1
        if current < p:
            seq.append('C' * (p - current))
            
while True:
    N = raw_input()
    if not len(N):
        break
    P = raw_input()
    if not len(P):
        continue
    P = [int(i) for i in raw_input().split()]
    print find_sequence(N, P)




