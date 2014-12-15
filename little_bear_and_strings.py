while True:
    try:
        S = raw_input()
    except EOFError:
        break

    T1 = raw_input()
    T2 = raw_input()
    stack = []
    result = []
    for i in range(len(S)):
        if S[i:i + T1.__len__()] == T1:
            stack.append(i)
        if S[i:i + T2.__len__()] == T2:
            for index in stack:
                if i == index:
                    continue
                if S[index:i] not in result:
                    result.append(S[index:i])

    print result.__len__()