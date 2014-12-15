import timeit


def prime(limit):
    l = []
    for x in range(limit):
        l.append(x)
    return l


print (timeit.timeit(stmt="sum(prime(pow(10,5)))", setup="from __main__ import prime", number=1000))